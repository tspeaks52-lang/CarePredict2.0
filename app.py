import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="CARE Predict",
    page_icon="logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# SESSION STATE
# ==========================================================

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "results" not in st.session_state:
    st.session_state.results = {}

# ==========================================================
# COLORS
# ==========================================================

PRIMARY = "#0F5A63"
PRIMARY_LIGHT = "#77C9C1"
ACCENT = "#E9F7F6"

BACKGROUND = "#F4F7FA"

CARD = "#FFFFFF"

TEXT = "#1F2937"

BORDER = "#DCE5EA"

GREEN = "#2E7D32"

YELLOW = "#F9A825"

RED = "#C62828"

# ==========================================================
# LOCAL TIME
# ==========================================================

LOCAL_TIME = datetime.now(
    ZoneInfo("America/New_York")
)
# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(f"""
<style>

/* ===========================
   MAIN APP
=========================== */

.stApp {{
    background-color: {BACKGROUND};
    color: {TEXT};
}}

.main .block-container {{
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1200px;
}}

/* ===========================
   SIDEBAR
=========================== */

section[data-testid="stSidebar"] {{
    background: linear-gradient(180deg, {PRIMARY} 0%, #0B4248 100%);
    border-right: none;
}}

section[data-testid="stSidebar"] * {{
    color: white;
}}

section[data-testid="stSidebar"] img {{
    margin-bottom: 20px;
}}

hr {{
    border-color: rgba(255,255,255,.20);
}}

/* ===========================
   HERO CARD
=========================== */

.hero-card {{

    background: linear-gradient(135deg, {PRIMARY} 0%, #16727D 100%);

    color: white;

    border-radius: 24px;

    padding: 40px;

    box-shadow: 0 10px 25px rgba(0,0,0,.12);

    margin-bottom: 30px;

}}

.hero-card h1 {{

    font-size: 42px;

    margin-bottom: 8px;

}}

.hero-card h3 {{

    font-weight:400;

    opacity:.95;

}}

.hero-card p {{

    font-size:18px;

    margin-top:20px;

}}

/* ===========================
   WHITE CARDS
=========================== */

div[data-testid="stVerticalBlock"] div:has(> div[data-testid="stVerticalBlock"]) {{

    border-radius:18px;

}}

[data-testid="stMetric"] {{

    background:white;

    border-radius:18px;

    padding:18px;

    border:1px solid {BORDER};

    box-shadow:0 4px 12px rgba(0,0,0,.05);

}}

.stAlert {{

    border-radius:15px;

}}

.stTextInput input,

.stSelectbox div[data-baseweb="select"],

.stMultiSelect div[data-baseweb="select"] {{

    border-radius:12px;

}}

/* ===========================
   BUTTONS
=========================== */

.stButton>button {{

    background:{PRIMARY};

    color:white;

    border:none;

    border-radius:14px;

    height:54px;

    font-size:17px;

    font-weight:600;

    transition:.25s;

}}

.stButton>button:hover {{

    background:{PRIMARY_LIGHT};

    color:{PRIMARY};

    transform:translateY(-2px);

}}

/* ===========================
   RECOMMENDATION CARD
=========================== */

.result-card {{

    border-radius:22px;

    padding:35px;

    color:white;

    text-align:center;

    box-shadow:0 12px 30px rgba(0,0,0,.15);

}}

.summary-card {{

    background:white;

    border-radius:18px;

    padding:25px;

    border:1px solid {BORDER};

    box-shadow:0 4px 12px rgba(0,0,0,.05);

}}

/* ===========================
   FOOTER
=========================== */

.footer {{

    text-align:center;

    color:#6B7280;

    font-size:13px;

    margin-top:45px;

}}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.image(
    "logo.png",
    use_container_width=True
)

st.sidebar.markdown("# CARE Predict")

st.sidebar.caption(
    "Clinical Assessment and Risk Evaluation Predict"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Daily Assessment",
        "About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("Version 4.0")

st.sidebar.caption("Graduate Internship Capstone")

st.sidebar.caption("Developed for Your Health")

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "Home":

    st.markdown(f"""
    <div class="hero-card">

    <h1>CARE Predict</h1>

    <h3>Clinical Assessment and Risk Evaluation Predict</h3>

    <p>
    Supporting earlier intervention through standardized
    Remote Patient Monitoring assessments.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Assessment Time",
            "2–3 Minutes"
        )

        st.caption(
            "Daily patient assessment"
        )

    with col2:

        st.metric(
            "Conditions",
            "3"
        )

        st.caption(
            "COPD • CHF • Diabetes"
        )

    with col3:

        st.metric(
            "Recommendation",
            "3 Levels"
        )

        st.caption(
            "Stable • Follow-Up • Immediate Care"
        )

    st.write("")

    with st.container(border=True):

        st.subheader("How CARE Predict Works")

        st.write("""
**Step 1**

Complete today's Daily Assessment.

---

**Step 2**

CARE Predict evaluates your responses.

---

**Step 3**

A recommendation is generated immediately after submission.

---

**Step 4**

Follow the recommended next steps.
""")

    st.info(
        "Select **Daily Assessment** from the navigation menu to begin."
    )
    # ==========================================================
# DAILY ASSESSMENT
# ==========================================================

elif page == "Daily Assessment":

    st.markdown("""
    <div class="hero-card">

    <h2>Daily Remote Patient Monitoring Assessment</h2>

    <p>
    Please complete today's assessment.
    CARE Predict will evaluate your responses
    and generate a recommendation.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ------------------------------------------------------
    # PATIENT INFORMATION
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("Patient Information")

        col1, col2 = st.columns(2)

        with col1:

            patient = st.text_input(
                "Patient Name (Optional)"
            )

        with col2:

            condition = st.selectbox(
                "Primary Chronic Condition",
                [
                    "COPD",
                    "Congestive Heart Failure (CHF)",
                    "Diabetes"
                ]
            )

    st.write("")

    # ------------------------------------------------------
    # GENERAL HEALTH
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader("General Health")

        feeling = st.radio(
            "1. How are you feeling today compared to yesterday?",
            [
                "Much Better",
                "About the Same",
                "A Little Worse",
                "Much Worse"
            ],
            index=None
        )

        symptoms = st.multiselect(
            "2. Have you experienced any of the following today? (Select all that apply)",
            [
                "Dizziness or confusion",
                "Fever or chills",
                "New or worsening pain"
            ]
        )

        events = st.multiselect(
            "3. Since your last assessment, have you experienced any of the following? (Select all that apply)",
            [
                "Fall or injury",
                "Emergency Room or Urgent Care visit",
                "New symptom that concerns you"
            ]
        )

        medication = st.radio(
            "4. Did you take all of your medications today?",
            [
                "Yes",
                "No"
            ],
            index=None
        )

        eating = st.radio(
            "5. Were you able to eat and drink normally today?",
            [
                "Yes",
                "No"
            ],
            index=None
        )

        contact = st.radio(
            "6. Would you like a member of your care team to contact you today?",
            [
                "Yes",
                "No"
            ],
            index=None
        )

    st.write("")
        # =====================================================
    # CONDITION-SPECIFIC ASSESSMENT
    # =====================================================

    with st.container(border=True):

        st.subheader(f"{condition} Assessment")

        st.write(
            "Please select any symptoms you are experiencing today."
        )

        disease_answers = []

        # --------------------------------------------------
        # COPD
        # --------------------------------------------------

        if condition == "COPD":

            if st.checkbox("More trouble breathing than usual"):
                disease_answers.append("Trouble Breathing")

            if st.checkbox("More coughing than usual"):
                disease_answers.append("More Coughing")

            if st.checkbox("Using my rescue inhaler more often"):
                disease_answers.append("Rescue Inhaler")

            if st.checkbox("My mucus has changed color"):
                disease_answers.append("Mucus Change")

            if st.checkbox("Trouble completing my normal daily activities"):
                disease_answers.append("Activity Limitation")

        # --------------------------------------------------
        # CHF
        # --------------------------------------------------

        elif condition == "Congestive Heart Failure (CHF)":

            if st.checkbox("More swelling in my feet or legs"):
                disease_answers.append("Swelling")

            if st.checkbox("Weight gain (2 pounds overnight or 5 pounds this week)"):
                disease_answers.append("Weight Gain")

            if st.checkbox("More short of breath than usual"):
                disease_answers.append("Shortness of Breath")

            if st.checkbox("Needed more pillows than usual to sleep"):
                disease_answers.append("Orthopnea")

            if st.checkbox("More tired than usual"):
                disease_answers.append("Fatigue")

        # --------------------------------------------------
        # DIABETES
        # --------------------------------------------------

        elif condition == "Diabetes":

            sugar_low = st.radio(
                "Have you had a blood sugar reading below 70 mg/dL today?",
                [
                    "Yes",
                    "No",
                    "I Don't Know"
                ],
                index=None
            )

            sugar_high = st.radio(
                "Have you had a blood sugar reading above 250 mg/dL today?",
                [
                    "Yes",
                    "No",
                    "I Don't Know"
                ],
                index=None
            )

            st.write("**Have you experienced any of the following today?**")

            if st.checkbox("Blurred vision"):
                disease_answers.append("Blurred Vision")

            if st.checkbox("Feeling more thirsty than usual"):
                disease_answers.append("Increased Thirst")

            if st.checkbox("Urinating more often"):
                disease_answers.append("Frequent Urination")

            if st.checkbox("Shaking, sweating, or dizziness (possible low blood sugar)"):
                disease_answers.append("Low Blood Sugar Symptoms")

            if sugar_low == "Yes":
                disease_answers.append("Blood Sugar Below 70")

            if sugar_high == "Yes":
                disease_answers.append("Blood Sugar Above 250")

    st.write("")

    # =====================================================
    # SUBMIT
    # =====================================================

    submitted = st.button(
        "Submit Daily Assessment",
        use_container_width=True
    )

    if submitted:

        import time

        with st.spinner("CARE Predict is analyzing your assessment..."):

            time.sleep(2)

        st.session_state.submitted = True

        st.session_state.results = {

            "patient": patient,

            "condition": condition,

            "feeling": feeling,

            "symptoms": symptoms,

            "events": events,

            "medication": medication,

            "eating": eating,

            "contact": contact,

            "disease": disease_answers

        }
    st.success("Assessment submitted successfully.")

    st.write("")

    st.caption(
        "Your recommendation will appear below."
    )
        # =====================================================
    # CARE PREDICT RECOMMENDATION ENGINE
    # =====================================================

    if st.session_state.submitted:

        data = st.session_state.results

        score = 0

        reasons = []

        # --------------------------------------------------
        # AUTOMATIC FOLLOW-UP RULE
        # --------------------------------------------------

        concerning_response = False

        # Feeling worse
        if data["feeling"] in ["A Little Worse", "Much Worse"]:
            concerning_response = True

        # General symptoms
        if len(data["symptoms"]) > 0:
            concerning_response = True

        # Recent events
        if len(data["events"]) > 0:
            concerning_response = True

        # Medication
        if data["medication"] == "No":
            concerning_response = True

        # Eating / Drinking
        if data["eating"] == "No":
            concerning_response = True

        # Disease-specific symptoms
        if len(data["disease"]) > 0:
            concerning_response = True
                # --------------------------------------------------
        # GENERAL HEALTH SCORING
        # --------------------------------------------------

        if data["feeling"] == "A Little Worse":

            score += 2

            reasons.append("You reported feeling a little worse today.")

        elif data["feeling"] == "Much Worse":

            score += 4

            reasons.append("You reported feeling much worse today.")

        # --------------------------------------------------
        # GENERAL SYMPTOMS
        # --------------------------------------------------

        if "Dizziness or confusion" in data["symptoms"]:

            score += 2

            reasons.append("Dizziness or confusion reported.")

        if "Fever or chills" in data["symptoms"]:

            score += 2

            reasons.append("Fever or chills reported.")

        if "New or worsening pain" in data["symptoms"]:

            score += 1

            reasons.append("New or worsening pain reported.")

        # --------------------------------------------------
        # RECENT EVENTS
        # --------------------------------------------------

        if "Fall or injury" in data["events"]:

            score += 3

            reasons.append("Recent fall or injury.")

        if "Emergency Room or Urgent Care visit" in data["events"]:

            score += 5

            reasons.append("Recent Emergency Room or Urgent Care visit.")

        if "New symptom that concerns you" in data["events"]:

            score += 2

            reasons.append("A new concerning symptom was reported.")

        # --------------------------------------------------
        # MEDICATION
        # --------------------------------------------------

        if data["medication"] == "No":

            score += 2

            reasons.append("You reported not taking your medications today.")

        # --------------------------------------------------
        # EATING / DRINKING
        # --------------------------------------------------

        if data["eating"] == "No":

            score += 2

            reasons.append("You reported being unable to eat or drink normally.")
                # --------------------------------------------------
        # DISEASE-SPECIFIC SCORING
        # --------------------------------------------------

        for symptom in data["disease"]:

            if symptom in [

                "Trouble Breathing",
                "Shortness of Breath",
                "Blood Sugar Below 70",
                "Blood Sugar Above 250",
                "Low Blood Sugar Symptoms"

            ]:

                score += 3

            else:

                score += 1

            reasons.append(symptom)

        # --------------------------------------------------
        # DETERMINE RECOMMENDATION
        # --------------------------------------------------

        if score >= 10:

            status = "IMMEDIATE CARE RECOMMENDED"

            color = RED

            recommendation = (
                "Your assessment indicates that immediate follow-up is recommended."
            )

        elif concerning_response or score > 0:

            status = "FOLLOW-UP RECOMMENDED"

            color = YELLOW

            recommendation = (
                "Your assessment indicates that follow-up with your care team is recommended."
            )

        else:

            status = "STABLE"

            color = GREEN

            recommendation = (
                "No immediate concerns were identified during today's assessment."
            )
                    # =====================================================
        # ASSESSMENT SUMMARY
        # =====================================================

        st.divider()

        st.subheader("Assessment Summary")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("**Patient Name**")

            if data["patient"]:
                st.write(data["patient"])
            else:
                st.write("Not Provided")

            st.markdown("**Primary Condition**")

            st.write(data["condition"])

        with col2:

            st.markdown("**Assessment Date**")

            st.write(
                LOCAL_TIME.strftime("%B %d, %Y")
            )

            st.markdown("**Assessment Time**")

            st.write(
                LOCAL_TIME.strftime("%I:%M %p")
            )

        st.write("")

        with st.container(border=True):

            st.subheader("Assessment Results")

            st.metric(
                "CARE Predict Risk Score",
                score
            )

            st.markdown("**Recommendation**")

            st.markdown(
                f"<h3 style='color:{color};'>{status}</h3>",
                unsafe_allow_html=True
            )

            st.write(recommendation)

        st.write("")
                # =====================================================
        # WHY THIS RECOMMENDATION
        # =====================================================

        st.subheader("Why did I receive this recommendation?")

        if reasons:

            for reason in reasons:

                st.write(f"• {reason}")

        else:

            st.success(
                "No concerning symptoms or responses were identified during today's assessment."
            )

        st.write("")

        # =====================================================
        # RECOMMENDED NEXT STEPS
        # =====================================================

        st.subheader("Recommended Next Steps")

        if status == "STABLE":

            st.success(
                "Continue taking your medications as prescribed."
            )

            st.success(
                "Continue monitoring your health and complete another assessment tomorrow."
            )

            st.success(
                "If you develop new or worsening symptoms, contact your healthcare provider."
            )

        elif status == "FOLLOW-UP RECOMMENDED":

            st.warning(
                "Continue monitoring your symptoms closely."
            )

            st.warning(
                "A member of your care team may contact you."
            )

            st.warning(
                "If your symptoms worsen before you are contacted, contact your healthcare provider."
            )

        else:

            st.error(
                "Contact the Your Health Care Team Triage Line immediately."
            )

            st.error(
                "Call: 1-800-491-0909"
            )

            st.error(
                "Press 9"
            )

            st.error(
                "If this is a life-threatening emergency, call 911 immediately."
            )

        # =====================================================
        # CARE TEAM CONTACT REQUEST
        # =====================================================

        if data["contact"] == "Yes":

            st.info(
                "You requested that a member of your care team contact you today."
            )

        # =====================================================
        # CLINICAL DISCLAIMER
        # =====================================================

        st.divider()

        st.info("""
**Clinical Disclaimer**

CARE Predict is a clinical decision support prototype developed for Your Health as part of a graduate internship capstone project.

This application is intended to support Remote Patient Monitoring (RPM) by helping identify patients who may benefit from earlier follow-up.

CARE Predict does not diagnose medical conditions and should not replace the clinical judgment of licensed healthcare professionals.

If you believe you are experiencing a life-threatening emergency, call **911 immediately**.
""")
        # ==========================================================
# ABOUT PAGE
# ==========================================================

elif page == "About":

    st.title("About CARE Predict")

    with st.container(border=True):

        st.subheader("Clinical Assessment and Risk Evaluation Predict")

        st.write("""
CARE Predict is a clinical decision support prototype developed for **Your Health** as part of a graduate internship capstone project.

The application was created to support **Remote Patient Monitoring (RPM)** by helping identify patients who may benefit from earlier follow-up based on standardized daily assessments.

CARE Predict currently supports patients with:

• Chronic Obstructive Pulmonary Disease (COPD)

• Congestive Heart Failure (CHF)

• Diabetes
""")

    st.write("")

    with st.container(border=True):

        st.subheader("How CARE Predict Works")

        st.write("""
1. Complete the Daily Assessment.

2. CARE Predict evaluates patient responses.

3. A clinical recommendation is generated.

4. Patients follow the recommended next steps.

5. Care teams can intervene earlier when appropriate.
""")

    st.write("")

    with st.container(border=True):

        st.subheader("CARE Predict Recommendations")

        st.write("""
**Stable**

No immediate concerns identified.

---

**Follow-Up Recommended**

One or more responses suggest that follow-up with the care team is appropriate.

---

**Immediate Care Recommended**

High-risk responses indicate that immediate follow-up is recommended.
""")

    st.write("")

    with st.container(border=True):

        st.subheader("Future Enhancements")

        st.write("""
• Electronic Health Record (EHR) Integration

• Artificial Intelligence Risk Prediction

• Secure Patient Login

• Provider Dashboard

• Population Health Analytics

• Mobile Application

• Automated Remote Patient Monitoring Alerts
""")

    st.write("")

    st.info("""
CARE Predict is intended to support—not replace—the clinical judgment of licensed healthcare professionals.
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
<div class="footer">

CARE Predict Version 4.0 • Graduate Internship Capstone

Developed for Your Health

</div>
""",
unsafe_allow_html=True
)