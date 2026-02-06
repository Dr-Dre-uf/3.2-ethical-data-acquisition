import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Ethical Data Acquisition", layout="wide")

st.markdown("""
<style>
    .narrator-box {
        background-color: #f4f6f7; 
        border-left: 5px solid #2c3e50; 
        padding: 20px; 
        border-radius: 4px; 
        font-style: italic; 
        font-family: 'Georgia', serif;
        margin-bottom: 25px;
        color: #333;
    }
    .header-box {
        background-color: #eaf2f8; 
        border: 1px solid #d5d8dc; 
        padding: 15px; 
        border-radius: 5px; 
        margin-bottom: 20px;
    }
    .toolkit-step {
        background-color: #fdfefe;
        border: 1px solid #eaecee;
        padding: 15px;
        border-radius: 5px;
        margin-bottom: 10px;
    }
    h2 { color: #1a5276; border-bottom: 1px solid #eee; padding-bottom: 10px; }
    h4 { color: #2c3e50; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR: TRACK & CONFIGURATION ---
st.sidebar.title("Course Configuration")

track = st.sidebar.radio(
    "Select Research Track:",
    ["Clinical Track (IC3 COVID-19)", "Basic Science Track (ImmPort)"]
)

# Set Variables based on Track
if "Clinical" in track:
    dataset_name = "IC3 UF Public COVID-19 Dataset"
    dataset_link = "https://ic3.center.ufl.edu/research/resources/datasets/"
    subject_term = "Patient"
    sample_term = "Electronic Health Record (EHR)"
    underserved_example = "Rural populations with limited hospital access"
else:
    dataset_name = "ImmPort (Immunology Database)"
    dataset_link = "https://www.immport.org/shared/home"
    subject_term = "Donor"
    sample_term = "Biological Specimen"
    underserved_example = "Donors of non-European ancestry"

st.sidebar.markdown("---")
st.sidebar.info(f"**Current Context:**\nDataset: {dataset_name}\nSubject: {subject_term}")

# Navigation
section = st.sidebar.radio(
    "Select Module:",
    [
        "1. Intro: The Four Pillars",
        "2. Autonomy: Informed Consent",
        "3. Justice: REP-EQUITY Toolkit",
        "4. Privacy: Security Protocols",
        "5. Beneficence: Closing the Loop"
    ]
)

# --- 3. HELPER FUNCTIONS ---
def narrator(text):
    st.markdown(f'<div class="narrator-box">🎙️ <b>Narrator:</b> "{text}"</div>', unsafe_allow_html=True)

# --- 4. APP CONTENT ---

# === SECTION 1: INTRO ===
if section == "1. Intro: The Four Pillars":
    st.title("Module MS2: Acquiring Ethically Sourced Biomedical Data")
    
    narrator(
        "Welcome to this educational journey... Today, we embark on an exploration of practices that honor patient autonomy, "
        "ensure societal justice, and promote the beneficence of improving human health. Our journey will focus on four key pillars."
    )
    
    st.markdown(f"""
    <div class="header-box">
        <h4>Selected Dataset for this Session:</h4>
        <p><b>{dataset_name}</b> (<a href="{dataset_link}" target="_blank">Link</a>)</p>
        <p>As we move through the four pillars, apply the concepts to this specific data source.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.info("**1. Autonomy**\n\nInformed Consent & Control")
    with col2: st.info("**2. Justice**\n\nEquitable Representation")
    with col3: st.info("**3. Privacy**\n\nData Security & Encryption")
    with col4: st.info("**4. Beneficence**\n\nReturning Value to Society")

# === SECTION 2: AUTONOMY ===
elif section == "2. Autonomy: Informed Consent":
    st.header("Pillar 1: Autonomy & Informed Consent")
    
    narrator(
        "Informed consent is a critical component of respecting patient autonomy. It transcends a simple signature on a document; "
        "it is a dynamic, ongoing dialogue... Simplifying complex medical jargon is crucial."
    )
    
    st.subheader(f"Exercise: Tailoring Consent for {dataset_name}")
    st.write(f"Refine the consent language for a {subject_term} contributing to this dataset.")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("#### Option A: Legal Standard")
        st.warning(
            f"The undersigned {subject_term} hereby grants permissions for the indefinite utilization of "
            f"{sample_term}s and associated metadata, waiving all rights to future claims..."
        )
        st.write("**Outcome:** Low comprehension. Participants may feel alienated.")

    with col2:
        st.markdown("#### Option B: Tailored Communication")
        literacy = st.select_slider("Target Health Literacy Level:", ["Medical Jargon", "Standard", "Simplified & Empowering"], value="Medical Jargon")
        
        if literacy == "Medical Jargon":
            st.warning("Please adjust the slider to simplify the language.")
        elif literacy == "Simplified & Empowering":
            st.success(
                f"**Revised Text:** 'We are asking for your permission to use your {sample_term} to help researchers understand disease. "
                "You can say no without affecting your care. You can also withdraw later. We want you to be a partner in this science.'"
            )
            st.caption("Matches Script: 'Patients should feel empowered... understanding they have the right to withdraw.'")

# === SECTION 3: JUSTICE (REP-EQUITY TOOLKIT) ===
elif section == "3. Justice: REP-EQUITY Toolkit":
    st.header("Pillar 2: Justice & Health Equity")
    
    narrator(
        "Societal justice... requires a commitment to equitable practices. This means diversifying the recruitment for studies... "
        "Achieving health equity demands robust community engagement."
    )
    
    st.markdown(f"""
    <div class="header-box">
        <h4>Tool Application: REP-EQUITY Toolkit</h4>
        <p><b>Reference:</b> Retzer A, et al. Nat Med. 2023.</p>
        <p>Use the 7 steps below to ensure the <b>{dataset_name}</b> is representative.</p>
    </div>
    """, unsafe_allow_html=True)

    # --- REP-EQUITY SIMULATION ---
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown('<div class="toolkit-step"><b>Step 1: Define Underserved Groups</b></div>', unsafe_allow_html=True)
        st.text_input(f"Which group is historically missing from {dataset_name}?", value=underserved_example)

        st.markdown('<div class="toolkit-step"><b>Step 2: Set Equity Aims</b></div>', unsafe_allow_html=True)
        st.checkbox("Equity is a primary aim of this study", value=True)

        st.markdown('<div class="toolkit-step"><b>Steps 3 & 4: Recruitment Goals</b></div>', unsafe_allow_html=True)
        goal = st.slider(f"Target % for Underserved {subject_term}s", 0, 100, 30)
        baseline = 5 # Fixed baseline for demo
        
    with c2:
        st.markdown('<div class="toolkit-step"><b>Step 5: Manage External Factors (Strategies)</b></div>', unsafe_allow_html=True)
        st.write("Select strategies to improve recruitment:")
        s1 = st.checkbox("Community Liaisons (+10%)")
        s2 = st.checkbox("Translated Materials (+5%)")
        s3 = st.checkbox("Logistical Support (+10%)")
        
        # Calculate Logic
        current = baseline + (10 if s1 else 0) + (5 if s2 else 0) + (10 if s3 else 0)
        
        st.markdown('<div class="toolkit-step"><b>Step 6: Evaluate Representation</b></div>', unsafe_allow_html=True)
        
        df = pd.DataFrame({
            "Stage": ["Baseline", "With Strategies", "Goal"],
            "Percentage": [baseline, current, goal]
        })
        fig = px.bar(df, x="Stage", y="Percentage", color="Stage", 
                     color_discrete_map={"Baseline":"#95a5a6", "With Strategies":"#27ae60", "Goal":"#2c3e50"})
        fig.update_layout(height=250, showlegend=False)
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    st.markdown('**Step 7: Legacy**')
    if current >= goal:
        st.success(f"Result: By meeting these goals, the {dataset_name} will serve as a resource for reducing health disparities.")
    else:
        st.warning("Result: Additional strategies are needed to prevent bias in future research.")

# === SECTION 4: PRIVACY ===
elif section == "4. Privacy: Security Protocols":
    st.header("Pillar 3: Privacy & Security")
    
    narrator(
        "Protecting patient privacy is not merely a legal obligation — it's a moral imperative... "
        "Employ multi-layered security protocols, including state-of-the-art encryption and routine security audits."
    )
    
    st.subheader(f"Security Audit for {dataset_name}")
    st.write("Select the layers of defense you will implement:")

    c1, c2, c3, c4 = st.columns(4)
    l1 = c1.checkbox("End-to-End Encryption")
    l2 = c2.checkbox("Role-Based Access Control")
    l3 = c3.checkbox("De-identification")
    l4 = c4.checkbox("Regular Audits")
    
    score = sum([l1, l2, l3, l4])
    
    if st.button("Run Security Simulation"):
        if score == 4:
            st.success("🛡️ **Secure:** Your multi-layered protocols successfully protected the data.")
        else:
            st.error("🚨 **Vulnerable:** Missing protocols detected. The script emphasizes 'Multi-layered security protocols' are required.")

# === SECTION 5: BENEFICENCE ===
elif section == "5. Beneficence: Closing the Loop":
    st.header("Pillar 4: Beneficence & Availability")
    
    narrator(
        "To maximize beneficence... researchers must cultivate an ethical framework that integrates continuous patient feedback... "
        "Outcomes from research should be made accessible to the contributing communities."
    )
    
    st.subheader("The Ethical Data Cycle")
    
    col1, col2, col3 = st.columns(3)
    col1.info(f"1. Acquisition\n({subject_term} provides data)")
    col2.info("2. Research\n(Analysis of patterns)")
    
    if col3.button("3. Return Value (Click to Close Loop)"):
        col3.success("3. Beneficence\n(Findings returned to community)")
        st.markdown(f"""
        **Impact Statement:**
        * {subject_term}s receive actionable health insights.
        * Community trust is restored.
        * The legacy of the {dataset_name} is positive.
        """)
    else:
        col3.warning("3. [Waiting for Action]... \n(If ignored, the process is extractive, not beneficial.)")

# --- FOOTER ---
st.markdown("---")
st.caption("Module MS2 | Course Materials | Based on REP-EQUITY Toolkit & IC3/ImmPort Datasets")
