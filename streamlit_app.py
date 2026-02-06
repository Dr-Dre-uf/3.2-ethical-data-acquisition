import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. CONFIGURATION & STYLE ---
st.set_page_config(page_title="Ethical Data Acquisition Demo", layout="wide", page_icon="⚖️")

st.markdown("""
<style>
    .narrator-box {
        background-color: #f0f4f8; 
        border-left: 5px solid #2c3e50; 
        padding: 20px; 
        border-radius: 5px; 
        font-style: italic; 
        font-family: 'Georgia', serif;
        margin-bottom: 25px;
        color: #333;
    }
    .instruction-box {
        background-color: #e8f8f5;
        border: 1px solid #2ecc71;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-weight: 500;
        color: #145a32;
    }
    .universal-header { 
        color: #2c3e50; 
        border-bottom: 2px solid #eee; 
        padding-bottom: 10px; 
        margin-top: 20px;
    }
    .concept-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        height: 100%;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
st.sidebar.title("🧭 Demo Navigation")
section = st.sidebar.radio(
    "Select Module:",
    [
        "1. Intro: The Four Pillars",
        "2. Autonomy: Consent Demo",
        "3. Justice: Sampling Demo",
        "4. Privacy: Security Demo",
        "5. Beneficence: Impact Demo",
        "6. Summary"
    ],
    help="Navigate through the different sections of the video script."
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Tip:** Hover over buttons and sliders to see definitions and extra context.")

# --- 3. HELPER FUNCTIONS ---
def narrator(text):
    """Displays the narrator text from the video script."""
    st.markdown(f'<div class="narrator-box">🎙️ <b>Narrator:</b> "{text}"</div>', unsafe_allow_html=True)

def instruction(text):
    """Displays user instructions for the demo."""
    st.markdown(f'<div class="instruction-box">👉 <b>Demo Instruction:</b> {text}</div>', unsafe_allow_html=True)

# --- 4. APP MODULES ---

# === SECTION 1: INTRO ===
if section == "1. Intro: The Four Pillars":
    st.title("Ethically Sourced Biomedical Data")
    
    narrator(
        "Welcome to this educational journey... Today, we embark on an exploration of practices that honor patient "
        "and donor autonomy, ensure societal justice, and promote the beneficence of improving human health."
    )
    
    st.markdown("### The Foundation of Ethical Science")
    st.write("These four pillars apply equally to **Clinical Science** (Patients) and **Foundational Science** (Donors/Samples).")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="concept-card">
        <h4>1. Autonomy</h4>
        <p><b>Respecting the Source.</b><br>
        Ensuring individuals maintain control over their personal health information and biological samples.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="concept-card">
        <h4>2. Justice</h4>
        <p><b>Equitable Representation.</b><br>
        Actively addressing health disparities by including historically underrepresented populations.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class="concept-card">
        <h4>3. Privacy</h4>
        <p><b>Data Security.</b><br>
        Employing multi-layered security protocols to protect sensitive genetic and medical data.</p>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="concept-card">
        <h4>4. Beneficence</h4>
        <p><b>Positive Impact.</b><br>
        Ensuring research outcomes align with community needs and provide actionable health insights.</p>
        </div>
        """, unsafe_allow_html=True)

# === SECTION 2: AUTONOMY ===
elif section == "2. Autonomy: Consent Demo":
    st.markdown('<h2 class="universal-header">Pillar 1: Autonomy & Informed Consent</h2>', unsafe_allow_html=True)
    
    narrator(
        "Informed consent... transcends a simple signature. It is a dynamic, ongoing dialogue... "
        "Simplifying complex medical jargon into clear, understandable language is crucial."
    )

    instruction("Move the slider below to observe how the phrasing of a consent form impacts a participant's understanding and autonomy.")

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔴 Low Autonomy (Legal Jargon)")
        st.info(
            "The undersigned grantor hereby authorizes the utilization of biological materials and associated phenotypic metadata "
            "for indefinite longitudinal analysis, waiving rights to pecuniary gain..."
        )
        st.error("Result: Participant is confused. They sign out of fear or pressure, not understanding their rights.")

    with col2:
        st.markdown("### 🟢 High Autonomy (Empowered)")
        
        # Interactive Slider
        clarity = st.select_slider(
            "Select Communication Style:", 
            options=["Standard Legalese", "Simplified Language", "Empowered Dialogue"], 
            value="Standard Legalese",
            help="See how changing the language level affects the 'Translation' below."
        )
        
        st.markdown("**User View (Translation):**")
        
        if clarity == "Standard Legalese":
            st.warning("⚠️ *Select a better level on the slider above to see the translation.*")
        elif clarity == "Simplified Language":
            st.success(
                "**Translation:** 'You are giving us permission to study your samples/data to understand diseases. "
                "You will not be paid, but your contribution helps science.'"
            )
        elif clarity == "Empowered Dialogue":
            st.success(
                "**Translation:** 'We want to partner with you. We will use your samples to study X. "
                "Here are the risks and benefits. You can ask questions now, and you can withdraw at any time. What do you think?'"
            )
            st.caption("✅ Narrator: 'Patients should feel empowered... understanding they have the right to withdraw.'")

# === SECTION 3: JUSTICE ===
elif section == "3. Justice: Sampling Demo":
    st.markdown('<h2 class="universal-header">Pillar 2: Justice & Health Equity</h2>', unsafe_allow_html=True)
    
    narrator(
        "Health equity involves actively addressing and reducing disparities... This means diversifying the recruitment "
        "for studies to include historically underrepresented and marginalized populations."
    )

    instruction("Use the slider to increase 'Community Engagement' and observe how the diversity of your dataset changes.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### Acquisition Strategy")
        
        effort = st.slider(
            "Community Outreach Effort (%)", 
            min_value=0, 
            max_value=100, 
            value=10, 
            step=10,
            help="Higher effort includes: Hiring translators, holding town halls, and partnering with community leaders."
        )
        
        st.write(f"**Current Investment:** {effort}%")
        
        # Logic: Effort drives diversity
        diversity_percent = 10 + (effort * 0.4) # Max 50%
        
    with col2:
        st.markdown("### Resulting Dataset Composition")
        
        # Data generation
        df = pd.DataFrame({
            "Population Group": ["Historically Well-Represented", "Underserved / Marginalized"],
            "Percentage": [100 - diversity_percent, diversity_percent]
        })
        
        fig = px.pie(
            df, values="Percentage", names="Population Group", 
            color="Population Group",
            color_discrete_map={"Historically Well-Represented": "#BDC3C7", "Underserved / Marginalized": "#27AE60"},
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)
        
    # Feedback
    if diversity_percent < 25:
        st.info("ℹ️ **Status:** Your dataset is currently homogenous. Scientific findings may not be applicable to the general population.")
    else:
        st.success("✅ **Status:** Your dataset reflects the real world. Your scientific conclusions will be robust and equitable.")

# === SECTION 4: PRIVACY ===
elif section == "4. Privacy: Security Demo":
    st.markdown('<h2 class="universal-header">Pillar 3: Privacy & Security</h2>', unsafe_allow_html=True)
    
    narrator(
        "Protecting privacy is... a moral imperative. Employ multi-layered security protocols, including "
        "state-of-the-art encryption... and stringent access controls."
    )
    
    instruction("Check the boxes to add security layers to your data protocol. Try to achieve 'Secure' status.")
    
    st.markdown("### Protocol Configuration")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        layer1 = st.checkbox(
            "End-to-End Encryption",
            help="Ensures data is unreadable to anyone without the decryption key, even if intercepted."
        )
    with c2:
        layer2 = st.checkbox(
            "Role-Based Access Control",
            help="Ensures only authorized personnel (e.g., PI, Data Manager) can access sensitive files."
        )
    with c3:
        layer3 = st.checkbox(
            "De-identification",
            help="Removes direct identifiers (names, SSN) from the dataset used for analysis."
        )
    with c4:
        layer4 = st.checkbox(
            "Regular Security Audits",
            help="Routine checks to find vulnerabilities before hackers do."
        )
        
    security_score = sum([layer1, layer2, layer3, layer4])
    
    st.write("---")
    st.markdown("### Protocol Status")
    
    if security_score == 4:
        st.success("🛡️ **SECURE:** You have implemented a multi-layered defense. You are compliant with regulations like HIPAA.")
    elif security_score >= 2:
        st.warning("⚠️ **VULNERABLE:** You have some protection, but sophisticated threats could still expose sensitive genomic or medical data.")
    else:
        st.error("🚨 **AT RISK:** Data is largely unprotected. A breach here would damage patient trust and violate ethical standards.")

# === SECTION 5: BENEFICENCE ===
elif section == "5. Beneficence: Impact Demo":
    st.markdown('<h2 class="universal-header">Pillar 4: Beneficence & Availability</h2>', unsafe_allow_html=True)
    
    narrator(
        "To maximize beneficence... researchers must cultivate an ethical framework that integrates continuous "
        "feedback. Patients [and communities] should feel as though they are partners in the research process."
    )

    instruction("Click the button below to 'Close the Loop' and see how data availability benefits the community.")

    st.subheader("The Ethical Data Cycle")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("⬇️ **1. Acquisition**\n\nParticipants donate data/samples with trust.")
    with col2:
        st.info("⚙️ **2. Research**\n\nScientists analyze data to find patterns.")
    with col3:
        loop = st.button(
            "🔄 Close the Loop (Share Results)",
            help="Click to simulate returning the value of research back to the participants."
        )
        
    st.write("---")
    
    if loop:
        st.success("⬆️ **3. Return of Value (Beneficence Achieved)**")
        st.markdown("""
        **Impact:**
        * **For Patients:** Access to improved treatments & personal health insights.
        * **For Communities:** Public health reports & shared intellectual property.
        * **For Science:** Trust is built, ensuring participation in future studies.
        """)
    else:
        st.markdown("""
        **3. The Void (Current State)** *Data is extracted, but nothing is returned. Participants feel used rather than included.*
        """)

# === SECTION 6: SUMMARY ===
elif section == "6. Summary":
    st.title("🎓 Demo Summary")
    
    narrator(
        "Ethically acquiring biomedical data is a nuanced process... By maintaining a steadfast commitment "
        "to these principles, healthcare organizations can achieve a delicate balance where scientific "
        "innovation does not compromise individual rights."
    )
    
    st.markdown("""
    ### Checklist for Ethical Acquisition
    Whether you are pipetting in a lab or treating patients in a ward, these rules apply:
    
    * **Autonomy:** Did the person truly understand what they agreed to?
    * **Justice:** Who is missing from my dataset?
    * **Privacy:** Is this data treated with the same security I would want for my own family?
    * **Beneficence:** How does this research give back to the people who made it possible?
    """)
    
    st.success("Thank you for exploring this demo. Together, we can turn the challenges of today into opportunities for a healthier and more just tomorrow.")
