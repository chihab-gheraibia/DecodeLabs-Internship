# app.py - Optimized Production AI-Driven Intrusion Detection Dashboard
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- Page Layout & Theme Configurations ---
st.set_page_config(
    page_title="Digital Mind IDS | Threat Telemetry",
    page_icon="🛡️",
    layout="wide"
)

# Dark Minimalist Terminal Styling
st.markdown("""
    <style>
    .main { background-color: #0A0A12; color: #E0E0E6; }
    h1, h2, h3 { color: #FF3366 !important; font-family: 'Consolas', monospace; font-weight: bold; }
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #FF3366, #C70039);
        color: white; border: none; font-weight: bold; width: 100%;
        border-radius: 4px; padding: 10px; transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 15px rgba(255, 51, 102, 0.6); transform: scale(1.01);
    }
    .panel-card { background-color: #141424; padding: 20px; border-radius: 6px; margin-bottom: 15px; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Digital Mind: Network Intrusion Detection Engine")
st.markdown("##### Enterprise Security Operations Dashboard | **Context: UNSW-NB15 Cybersecurity Core**")
st.write("---")

# --- Dynamic Path Resolution (Senior Engineering Practice) ---
# This automatically anchors the application to its current folder location
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
MODEL_PATH = os.path.join(CURRENT_DIR, "ids_random_forest.pkl")
SCALER_PATH = os.path.join(CURRENT_DIR, "ids_scaler.pkl")

@st.cache_resource
def load_ids_pipeline():
    if not os.path.exists(MODEL_PATH) or not os.path.exists(SCALER_PATH):
        return None, None
    try:
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        return model, scaler
    except Exception as e:
        st.sidebar.error(f"Error loading model assets: {e}")
        return None, None

model, scaler = load_ids_pipeline()

# Exact numerical features layout used during your training phase in IDS_system.ipynb
NUM_COLS = ['dur', 'sbytes', 'dbytes', 'sttl', 'dttl', 'sload', 'dload']

if model is None:
    st.error("### ❌ Core Security Artifacts Missing")
    st.markdown(f"""
    The application cannot bind execution vectors because the pipeline elements are missing from the current working directory:
    * **Expected Folder Path:** `{CURRENT_DIR}`
    * **Looking for Model:** `ids_random_forest.pkl`
    * **Looking for Scaler:** `ids_scaler.pkl`
    
    👉 **Action Required:** Make sure you have downloaded `ids_random_forest.pkl` and `ids_scaler.pkl` from your Colab runtime and placed them directly inside the folder `C:\\Users\\chihab12\\Documents\\DecodeLabs-IDS`.
    """)
else:
    # --- UI Grid Generation ---
    col_inputs, col_telemetry = st.columns([5, 7], gap="large")
    
    with col_inputs:
        st.markdown("<div class='panel-card'>", unsafe_allow_html=True)
        st.subheader("🎛️ Packet Ingestion Interface")
        
        # Categorical String Parameters
        proto = st.selectbox("Protocol Layer (proto)", ['tcp', 'udp', 'sctp', 'icmp', 'arp'])
        state = st.selectbox("Transaction State (state)", ['FIN', 'INT', 'CON', 'REQ', 'RST'])
        service = st.selectbox("Service Context (service)", ['undefined', 'http', 'dns', 'ftp', 'smtp', 'ssh'])
        
        st.write("---")
        
        # Continuous Volumetric Vectors
        dur = st.number_input("Connection Duration (dur)", min_value=0.0, value=0.001, format="%.6f")
        sbytes = st.number_input("Source Bytes (sbytes)", min_value=0, value=120)
        dbytes = st.number_input("Destination Bytes (dbytes)", min_value=0, value=140)
        
        # TTL Controls
        sttl = st.slider("Source TTL (sttl)", 0, 255, 31)
        dttl = st.slider("Destination TTL (dttl)", 0, 255, 29)
        
        # Traffic Network Loads
        sload = st.number_input("Source Bits/Sec (sload)", min_value=0.0, value=150000.0)
        dload = st.number_input("Destination Bits/Sec (dload)", min_value=0.0, value=180000.0)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_telemetry:
        st.markdown("<div class='panel-card'>", unsafe_allow_html=True)
        st.subheader("📊 Live Threat Assessment")
        
        # Construct raw numeric inputs matrix for evaluation
        raw_numeric_data = pd.DataFrame([{
            'dur': dur, 'sbytes': sbytes, 'dbytes': dbytes,
            'sttl': sttl, 'dttl': dttl, 'sload': sload, 'dload': dload
        }])
        
        if st.button("⚡ Inspect Active Traffic Payload"):
            try:
                # Enforce statistical scaling vector conversions
                scaled_numerical = scaler.transform(raw_numeric_data[NUM_COLS])
                scaled_df = pd.DataFrame(scaled_numerical, columns=NUM_COLS)
                
                # Predict the signature classification array (0 = Safe, 1 = Incident)
                is_anomaly = model.predict(scaled_df)[0]
                probs = model.predict_proba(scaled_df)[0]
                threat_metric = probs[1] * 100
                
                st.write("---")
                
                if is_anomaly == 0:
                    st.success(f"### ✅ TRAFFIC SANITIZED: PASSED")
                    st.markdown(f"**Confidence Matrix:** System evaluates a `{probs[0]*100:.2f}%` structural probability of normal state traffic.")
                    st.info("💡 **Policy Advisory:** Metric signatures match baseline communication parameters. Standard firewall rules apply.")
                else:
                    st.error(f"### 🚨 EXPLOIT VECTOR DETECTED: UNCLEAN")
                    st.markdown(f"**Threat Index:** System calculates a `{threat_metric:.2f}%` operational probability of malicious activity.")
                    
                    # Dynamic Security Incident Response Output
                    st.markdown("#### 🛠️ Immediate Mitigating Actions")
                    if sttl > 64:
                        st.warning("⚠️ **Signature Match:** Deep telemetry structures identify high-magnitude Time-to-Live variables matching known **Reconnaissance & Network Scans**.")
                        st.code(f"Router-ACL# deny ip host [SOURCE_IP] any", language="bash")
                    else:
                        st.warning("⚠️ **Signature Match:** Volumetric feature load analysis identifies patterns corresponding to link **Denial of Service (DoS)** saturations.")
                        st.code(f"Traffic-Shaper# policy rate-limit 10000", language="bash")
            except Exception as e:
                st.error(f"Execution Error during feature inference: {e}")
        else:
            st.write("Awaiting pipeline injection stream command...")
        st.markdown("</div>", unsafe_allow_html=True)