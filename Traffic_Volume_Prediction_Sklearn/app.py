import os
import sys
from pathlib import Path
import streamlit as st
import pandas as pd
import joblib

# Set Page Config
st.set_page_config(
    page_title="Traffic Volume Prediction",
    page_icon="🚦",
    layout="wide"
)

# Robust Base Directory Resolution
BASE_DIR = Path(__file__).resolve().parent
if not (BASE_DIR / "traffic_volume_model.pkl").exists() and (BASE_DIR / "Traffic_Volume_Prediction_Sklearn" / "traffic_volume_model.pkl").exists():
    BASE_DIR = BASE_DIR / "Traffic_Volume_Prediction_Sklearn"

st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.2rem;
    }
    .traffic-green {
        background: linear-gradient(135deg, #10B981 0%, #059669 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.3);
    }
    .traffic-amber {
        background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(245, 158, 11, 0.3);
    }
    .traffic-red {
        background: linear-gradient(135deg, #EF4444 0%, #DC2626 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 10px 15px -3px rgba(239, 68, 68, 0.3);
    }
    .traffic-banner {
        font-size: 2.8rem;
        font-weight: 800;
        margin: 0.3rem 0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🚦 Intelligent Traffic Volume & Congestion Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Forecast urban arterial traffic flow (vehicles/hour) using a trained <b>RandomForestRegressor</b> based on time of day, weather, and holiday events.</div>', unsafe_allow_html=True)

model_path = BASE_DIR / "traffic_volume_model.pkl"
csv_path = BASE_DIR / "data" / "traffic_volume.csv"
chart_path = BASE_DIR / "feature_importance.png"

if not model_path.exists():
    st.error(f"Model file not found at `{model_path}`! Please run 'python train_model.py' first.")
    st.stop()

@st.cache_resource
def get_model():
    return joblib.load(str(model_path))

model = get_model()

tab1, tab2, tab3 = st.tabs(["🔮 Real-Time Traffic Flow Predictor", "📈 Feature Importance & Trends", "📋 Historical Traffic Flow Logs"])

days_map = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

with tab1:
    col_input, col_result = st.columns([1.1, 0.9])
    
    with col_input:
        st.subheader("Transit & Environmental Conditions")
        
        scenario = st.selectbox(
            "⚡ Quick Traffic Scenario Preset",
            ["Custom Conditions", "🚗 Morning Rush Hour (8 AM)", "🌆 Evening Peak Gridlock (18:00)", "🌧️ Rainy Midday Traffic", "🌙 Midnight Free-Flow Highway", "🎉 Public Holiday Leisure Flow"]
        )
        
        if scenario == "🚗 Morning Rush Hour (8 AM)":
            def_hr, def_dow, def_temp, def_rain, def_hol = 8, 1, 24.0, 0.0, 0
        elif scenario == "🌆 Evening Peak Gridlock (18:00)":
            def_hr, def_dow, def_temp, def_rain, def_hol = 18, 4, 29.0, 1.5, 0
        elif scenario == "🌧️ Rainy Midday Traffic":
            def_hr, def_dow, def_temp, def_rain, def_hol = 13, 2, 21.0, 22.0, 0
        elif scenario == "🌙 Midnight Free-Flow Highway":
            def_hr, def_dow, def_temp, def_rain, def_hol = 1, 3, 19.0, 0.0, 0
        elif scenario == "🎉 Public Holiday Leisure Flow":
            def_hr, def_dow, def_temp, def_rain, def_hol = 15, 6, 31.0, 0.5, 1
        else:
            def_hr, def_dow, def_temp, def_rain, def_hol = 17, 0, 27.0, 2.0, 0
            
        with st.form("traffic_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                hour = st.slider("Hour of Day (24h clock)", 0, 23, int(def_hr), format="%d:00")
                day_selected = st.selectbox(
                    "Day of the Week",
                    options=list(days_map.keys()),
                    index=int(def_dow),
                    format_func=lambda x: f"{days_map[x]} (Day {x})"
                )
                temperature = st.slider("Ambient Temperature (°C)", 10.0, 45.0, float(def_temp), step=0.5)
            with col_b:
                rain = st.slider("Rainfall Rate (mm)", 0.0, 50.0, float(def_rain), step=0.5)
                holiday = st.radio("Calendar / Public Holiday?", [0, 1], index=int(def_hol), format_func=lambda x: "No (Regular Working Day)" if x == 0 else "Yes (Holiday)")
                
            submit_btn = st.form_submit_button("🚀 Predict Traffic Flow", use_container_width=True)
            
    with col_result:
        st.subheader("Traffic Flow & Congestion Assessment")
        if submit_btn:
            sample = pd.DataFrame([{
                "hour": hour,
                "day_of_week": day_selected,
                "temperature_c": temperature,
                "rain_mm": rain,
                "holiday": holiday
            }])
            
            raw_vol = model.predict(sample)[0]
            vehicles = max(0, round(raw_vol))
            
            if vehicles >= 650:
                css_class = "traffic-red"
                tier = "🔴 HEAVY CONGESTION / GRIDLOCK"
            elif vehicles >= 400:
                css_class = "traffic-amber"
                tier = "🟡 MODERATE DENSITY TRAFFIC"
            else:
                css_class = "traffic-green"
                tier = "🟢 FREE-FLOWING TRAFFIC"
                
            st.markdown(f"""
            <div class="{css_class}">
                <div style="font-size: 0.95rem; opacity: 0.9;">Projected Corridor Volume</div>
                <div class="traffic-banner">{vehicles:,} Vehicles / Hr</div>
                <div style="font-size: 1.1rem; font-weight: 600;">{tier}</div>
            </div>
            """, unsafe_allow_html=True)
            
            st.write("")
            st.markdown("### 🚦 ITS Operational Recommendations")
            if vehicles >= 650:
                st.error("🚨 **Gridlock Mitigation**: Extend green-phase traffic signal duration by +20s on arterial corridors; enable variable message signs (VMS) suggesting detour routes.")
            elif vehicles >= 400:
                st.warning("⚡ **Standard Peak Routing**: Coordinated green wave signal timing recommended.")
            else:
                st.success("🟢 **Normal Flow**: Maintenance and roadwork permits safe to operate during this window.")
                
            if rain >= 15.0:
                st.info("🌧️ **Heavy Rain Warning**: Wet roads increase braking distance. Enforce reduced 50 km/h advisory speed limit.")
                
            with st.expander("🔍 Model Input Payload"):
                st.json(sample.to_dict(orient="records")[0])
        else:
            st.info("👈 Select traffic conditions and click **'Predict Traffic Flow'**.")
            
    st.write("---")
    st.subheader("📈 24-Hour Diurnal Traffic Curve (0:00 - 23:00)")
    if st.button("Generate 24-Hour Traffic Curve"):
        hours_all = list(range(24))
        day_val = day_selected if 'day_selected' in locals() else 1
        temp_val = temperature if 'temperature' in locals() else 27.0
        rain_val = rain if 'rain' in locals() else 0.0
        hol_val = holiday if 'holiday' in locals() else 0
        
        sim_df = pd.DataFrame([{
            "hour": h,
            "day_of_week": day_val,
            "temperature_c": temp_val,
            "rain_mm": rain_val,
            "holiday": hol_val
        } for h in hours_all])
        
        preds = model.predict(sim_df)
        chart_data = pd.DataFrame({
            "Hour": [f"{h:02d}:00" for h in hours_all],
            "Projected Volume (Veh/hr)": [round(p) for p in preds]
        }).set_index("Hour")
        st.line_chart(chart_data)

with tab2:
    st.subheader("Feature Importance Breakdown")
    if chart_path.exists():
        st.image(str(chart_path), caption="Top Factors Influencing Traffic Volume", use_container_width=True)
    else:
        st.info("Chart will appear after running train_model.py")

with tab3:
    st.subheader("Traffic Volume Logs (traffic_volume.csv)")
    if csv_path.exists():
        df = pd.read_csv(csv_path)
        col1, col2, col3 = st.columns(3)
        col1.metric("Logged Observations", f"{len(df):,}")
        col2.metric("Average Volume", f"{df['traffic_volume'].mean():.0f} veh/hr")
        col3.metric("Peak Record Volume", f"{df['traffic_volume'].max():.0f} veh/hr")
        st.dataframe(df.head(100), use_container_width=True)
    else:
        st.warning("Dataset not found.")
