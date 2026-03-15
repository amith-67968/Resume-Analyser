🚀 Career Compass AI – Resume Analysis & Career Guidance

Career Compass AI is a Streamlit-based web application that analyzes resumes and offers personalized career guidance. It suggests suitable job roles, highlights skill gaps, and provides learning resources to help users upskill and grow in their career.

📌 Features

✔ Upload resume (PDF / text)

✔ Extracts skills from resume

✔ Matches skills to multiple job roles

✔ Shows skill match score (0–100)

✔ Identifies missing / recommended skills

✔ Displays learning resources & career roadmap

✔ Minimal UI powered by Streamlit

✔ No database or ML model required (static data)


🧠 Tech & Tools Used
Component	Technology
Frontend UI	Streamlit
Resume Parsing	PyPDF2
Skill Matching	Static Keyword Match
Data Handling	Python Dictionaries / Pandas
Language	Python 3.x
🔧 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/amith-67968/Resume-Analyser.git
cd career-compass-ai


2️⃣ Install required dependencies
pip install -r requirements.txt


3️⃣ Run the Streamlit app
streamlit run app.py


📄 Supported Resume Format

✔ PDF files
✔ Text input (copy-paste resume text)


🔐 All resume data stays local — no cloud upload, no database.


📊 How It Works
Step	Action
1	User uploads a resume
2	System extracts skills using keyword detection
3	Skills are matched with static job role data
4	App calculates a match score
5	Missing skills & learning roadmap are displayed

The app uses simple rule-based matching to deliver fast insights without a heavy ML model.

🌱 Future Enhancements

🔮 NLP-based skill extraction
📌 Real-time job market stats
📊 Trend-based scoring
🎯 Personalized learning path
🔐 Save & secure user profiles with login

🤝 Contributing

Contributions are welcome! Feel free to fork, open an issue, or submit a pull request.

📜 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it.

⭐ If you like this project, give it a star on GitHub!

💬 For ideas or issues, feel free to connect
