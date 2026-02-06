Ethical Biomedical Data Acquisition Demo ⚖️
An interactive educational dashboard designed to accompany the course module "Acquiring Ethically Sourced Biomedical Data."

This application serves as a companion tool to the video lecture, allowing participants to simulate the impact of ethical choices in both Clinical Science (patient data) and Foundational Science (biological samples/donors).

🎯 Learning Objectives
By using this app, participants will explore the "Four Pillars" of ethical data acquisition:

Autonomy: Experience how clear communication impacts a participant's ability to give informed consent.

Justice: Visualize how recruitment effort correlates with dataset diversity and representativeness.

Privacy: Build a security protocol and test it against simulated data breaches.

Beneficence: Demonstrate the importance of "closing the loop" by returning research value to the community.

🛠️ Prerequisites
Python 3.8 or higher

pip (Python package installer)

📦 Installation
Clone or download this repository to your local machine.

Navigate to the project folder in your terminal.

Install the required dependencies:

Bash

pip install -r requirements.txt
🚀 How to Run
Execute the following command in your terminal:

Bash

streamlit run app.py
Note: If your script is named something else (e.g., demo.py), replace app.py with your filename.

📂 File Structure
app.py: The main application script containing the interactive modules.

requirements.txt: List of Python libraries required (Streamlit, Pandas, Plotly).

README.md: This documentation file.

🧠 Application Modules
The app is divided into sections that mirror the video script:

Intro: Overview of the four pillars.

Autonomy Module: Compare "Legalese" vs. "Empowered" consent language using a slider.

Justice Module: Adjust community outreach efforts to see real-time updates on dataset demographics (Pie Chart).

Privacy Module: A checklist exercise to implement security layers (Encryption, RBAC, etc.) and a "Status Check" based on your configuration.

Beneficence Module: An interactive flow diagram demonstrating the return of value to participants.

📝 License & Usage
This tool is intended for educational purposes / course demonstration.

Concepts based on: REP-EQUITY Toolkit and standard bioethics frameworks (Belmont Report).
