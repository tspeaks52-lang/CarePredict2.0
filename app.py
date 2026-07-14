import streamlit as st
from datetime import datetime

# ==========================================================
# PAGE CONFIG
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
# CARE PREDICT COLORS
# ==========================================================

PRIMARY = "#105560"
SECONDARY = "#77C9C1"
BACKGROUND = "#F5F7FA"
TEXT = "#1F2937"

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown(f"""
<style>

.stApp {{
    background-color: {BACKGROUND};
}}

section[data-testid="stSidebar"] {{
    background: {PRIMARY};
}}

section[data-testid="stSidebar"] * {{
    color: white;
}}

.block-container {{
    padding-top: 2rem;
}}

.hero {{
    background: {PRIMARY};
    color: white;
    padding: 45px;
    border-radius: 18px;
    text-align: center;
}}

.footer {{
    text-align: center;
    color: gray;
    margin-top: 40px;
    font-size: 13px;
}}

.stButton > button {{
    background: {SECONDARY};
    color: {PRIMARY};
    border: none;
    border-radius: 10px;
    font-weight: bold;
    height: 50px;
    width: 100%;
}}

.stButton > button:hover {{
    background: {PRIMARY};
    color: white;
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

st.sidebar.markdown("## CARE Predict")

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

st.sidebar.caption("Version 3.1")

st.sidebar.caption("Graduate Internship Capstone")

st.sidebar.caption("Developed for Your Health")

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "Home":

    st.markdown(f"""
    <div class="hero">

    <h1>CARE Predict</h1>

    <h3>Clinical Assessment and Risk Evaluation Predict</h3>

    <p>
    Supporting earlier intervention through
    Remote Patient Monitoring.
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

    with col2:
        st.metric(
            "Questions",
            "11"
        )

    with col3:
        st.metric(
            "Recommendation",
            "Green | Yellow | Red"
        )

    st.write("")

    with st.container(border=True):

        st.subheader("How CARE Predict Works")

        st.write("""
1. Complete the Daily Assessment.

2. CARE Predict evaluates your responses.

3. A recommendation is generated.

4. Follow the recommended next steps.
""")

    st.info(
        "Select **Daily Assessment** from the navigation menu to begin."
    )

# ==========================================================
# DAILY ASSESSMENT
# ==========================================================
# ==========================================================
# DAILY ASSESSMENT
# ==========================================================

elif page == "Daily Assessment":

    st.title("Daily Remote Patient Monitoring Assessment")

    st.write(
        "Please complete today's assessment. CARE Predict will analyze your responses and generate a recommendation."
    )

    st.divider()

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
                    "CHF",
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

    # ------------------------------------------------------
    # CONDITION-SPECIFIC ASSESSMENT
    # ------------------------------------------------------

    with st.container(border=True):

        st.subheader(f"{condition} Assessment")

        st.write(
            "Please select any symptoms you are experiencing today."
        )

        disease_answers = []

        if condition == "COPD":

            if st.checkbox("More trouble breathing than usual"):
                disease_answers.append("Trouble Breathing")

            if st.checkbox("More coughing than usual"):
                disease_answers.append("More Coughing")

            if st.checkbox("Using my rescue inhaler more often"):
                disease_answers.append("Rescue Inhaler")

            if st.checkbox("My mucus has changed color"):
                disease_answers.append("Mucus Change")

            if st.checkbox("Trouble doing my normal daily activities"):
                disease_answers.append("Activity Limitation")

        elif condition == "CHF":

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

            st.write(
                "**Have you experienced any of the following today? (Select all that apply)**"
            )

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
        # ==========================================================
# CARE PREDICT RECOMMENDATION ENGINE
# ==========================================================

if st.session_state.submitted:

    data = st.session_state.results

    score = 0

    reasons = []

    # ------------------------------------------------------
    # GENERAL HEALTH SCORING
    # ------------------------------------------------------

    if data["feeling"] == "A Little Worse":

        score += 2

        reasons.append("You reported feeling a little worse today.")

    elif data["feeling"] == "Much Worse":

        score += 4

        reasons.append("You reported feeling much worse today.")

    # ------------------------------------------------------
    # GENERAL SYMPTOMS
    # ------------------------------------------------------

    if "Dizziness or confusion" in data["symptoms"]:

        score += 2

        reasons.append("Dizziness or confusion reported.")

    if "Fever or chills" in data["symptoms"]:

        score += 2

        reasons.append("Fever or chills reported.")

    if "New or worsening pain" in data["symptoms"]:

        score += 1

        reasons.append("New or worsening pain reported.")

    # ------------------------------------------------------
    # EVENTS
    # ------------------------------------------------------

    if "Fall or injury" in data["events"]:

        score += 3

        reasons.append("Recent fall or injury.")

    if "Emergency Room or Urgent Care visit" in data["events"]:

        score += 5

        reasons.append("Recent Emergency Room or Urgent Care visit.")

    if "New symptom that concerns you" in data["events"]:

        score += 2

        reasons.append("A new concerning symptom was reported.")

    # ------------------------------------------------------
    # MEDICATION
    # ------------------------------------------------------

    if data["medication"] == "No":

        score += 2

        reasons.append("You did not take your medications today.")

    # ------------------------------------------------------
    # EATING / DRINKING
    # ------------------------------------------------------

    if data["eating"] == "No":

        score += 2

        reasons.append("You were unable to eat or drink normally today.")

    # ------------------------------------------------------
    # DISEASE-SPECIFIC SCORING
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # DETERMINE STATUS
    # ------------------------------------------------------

    if score <= 4:

        status = "STABLE"

        color = "#2E7D32"

        recommendation = (
            "Based on today's assessment, no immediate concerns were identified."
        )

    elif score <= 9:

        status = "FOLLOW-UP RECOMMENDED"

        color = "#F9A825"

        recommendation = (
            "Some responses indicate that follow-up with your care team may be appropriate."
        )

    else:

        status = "IMMEDIATE CARE RECOMMENDED"

        color = "#C62828"

        recommendation = (
            "Your responses indicate that immediate follow-up is recommended."
        )

    # ======================================================
    # ASSESSMENT SUMMARY
    # ======================================================

    st.divider()

    st.subheader("Assessment Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.write("**Patient Name**")

        if data["patient"]:

            st.write(data["patient"])

        else:

            st.write("Not Provided")

        st.write("**Primary Condition**")

        st.write(data["condition"])

    with col2:

        st.write("**Assessment Date**")

        st.write(datetime.now().strftime("%B %d, %Y"))

        st.write("**Assessment Time**")

        st.write(datetime.now().strftime("%I:%M %p"))
            # ======================================================
    # CARE PREDICT RECOMMENDATION
    # ======================================================

    st.divider()

    st.markdown(f"""
    <div style="
        background:{color};
        color:white;
        padding:30px;
        border-radius:15px;
        text-align:center;
    ">

    <h2>CARE Predict Recommendation</h2>

    <h1>{status}</h1>

    <p style="font-size:18px;">
        {recommendation}
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.metric(
        "CARE Predict Risk Score",
        score
    )

    # ======================================================
    # WHY THIS RECOMMENDATION
    # ======================================================

    st.divider()

    st.subheader("Why did I receive this recommendation?")

    if reasons:

        for reason in reasons:

            st.write(f"• {reason}")

    else:

        st.success(
            "No concerning symptoms were identified during today's assessment."
        )

    # ======================================================
    # NEXT STEPS
    # ======================================================

    st.divider()

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
            "Continue monitoring your symptoms."
        )

        st.warning(
            "A member of your care team may contact you."
        )

        st.warning(
            "If your symptoms worsen before you are contacted, contact your healthcare provider."
        )

    else:

        st.error(
            "Contact the Your Health Care Team Triage Line."
        )

        st.error(
            "Call 1-800-491-0909"
        )

        st.error(
            "Press 9"
        )

        st.error(
            "If this is a life-threatening emergency, call 911 immediately."
        )

    # ======================================================
    # PATIENT REQUESTED CONTACT
    # ======================================================

    if data["contact"] == "Yes":

        st.info(
            "You requested that a member of your care team contact you today."
        )

    # ======================================================
    # DISCLAIMER
    # ======================================================

    st.divider()

    st.info("""
**Clinical Disclaimer**

CARE Predict is a clinical decision support prototype developed for Your Health as part of a graduate internship capstone project.

This application is intended to support Remote Patient Monitoring by helping identify patients who may benefit from earlier follow-up.

CARE Predict does **not** diagnose medical conditions or replace the clinical judgment of licensed healthcare professionals.

If you believe you are experiencing a life-threatening emergency, call **911 immediately**.
""")

# ==========================================================
# ABOUT
# ==========================================================

elif page == "About":

    st.title("About CARE Predict")

    with st.container(border=True):

        st.subheader("Clinical Assessment and Risk Evaluation Predict")

        st.write("""
CARE Predict is a clinical decision support prototype developed for **Your Health**
as part of a graduate internship capstone project.

The application was designed to support **Remote Patient Monitoring (RPM)**
by providing a standardized daily assessment for patients with chronic
conditions including:

• Chronic Obstructive Pulmonary Disease (COPD)

• Congestive Heart Failure (CHF)

• Diabetes

Based on patient responses, CARE Predict generates one of three
recommendations:

• Stable

• Follow-Up Recommended

• Immediate Care Recommended

The goal of the application is to encourage earlier intervention,
improve communication between patients and care teams, and support
clinical decision-making.
""")

    st.write("")

    with st.container(border=True):

        st.subheader("Clinical Workflow")

        st.write("""
1. Patient completes the Daily Assessment.

2. CARE Predict evaluates patient responses.

3. A recommendation is generated.

4. The patient follows the recommended next steps.

5. When appropriate, the care team follows up with the patient.
""")

    st.write("")

    with st.container(border=True):

        st.subheader("Future Enhancements")

        st.write("""
• Electronic Health Record (EHR) Integration

• Artificial Intelligence Risk Prediction

• Provider Dashboard

• Population Health Analytics

• Secure Patient Login

• Automated RPM Alerts

• Mobile Application
""")

    st.write("")

    st.info("""
CARE Predict is intended to support—not replace—the clinical judgment of licensed healthcare professionals.
""")

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    f"CARE Predict Version 3.1 | Developed for Your Health | {datetime.now().strftime('%B %d, %Y')}"
)