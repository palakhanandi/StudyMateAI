# 📚 StudyMate AI

> A Multi-Agent Learning Assistant for Personalized Education

StudyMate AI is an AI-powered learning assistant built using a **Multi-Agent Architecture**. Instead of relying on a single AI model, the application uses specialized agents that work together to provide personalized learning experiences including study planning, tutoring, quiz generation, and progress tracking.

This project was developed as part of the **Kaggle AI Agents Capstone**.

---

## 🚀 Features

### 📅 Planner Agent
- Creates personalized study schedules
- Plans based on subjects, available study hours, and exam dates
- Generates structured day-by-day learning plans

### 📖 Tutor Agent
- Explains difficult concepts in simple language
- Provides interactive learning support
- Adapts explanations based on user queries

### 📝 Quiz Agent
- Generates topic-based quizzes
- Tests understanding with AI-generated questions
- Helps reinforce learning through practice

### 📊 Progress Agent
- Tracks learning progress
- Stores quiz performance
- Displays improvement over time
- Highlights weak areas for revision

---

## 📂 Project Structure

```
StudyMateAI/
│
├── agents/
│   ├── planner_agent.py
│   ├── tutor_agent.py
│   ├── quiz_agent.py
│   ├── progress_agent.py
│   └── __init__.py
│
├── tools/
│   ├── quiz_tool.py
│   ├── scheduler.py
│   ├── tracker.py
│   └── __init__.py
│
├── data/
│   └── progress.json
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## 💻 Technologies Used

- Python
- Streamlit
- Google Gemini API
- Multi-Agent Architecture
- JSON
- Git & GitHub

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/palakhanandi/StudyMateAI.git
```

```bash
cd StudyMateAI
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Or replace the placeholder in your configuration with your own API key.

---
---

## 🎯 How It Works

1. User opens the Streamlit interface.
2. Selects one of the AI agents.
3. Enters study details or asks a question.
4. The selected agent communicates with Google Gemini.
5. AI-generated response is displayed.
6. Progress is saved for future tracking.

---

## 🌟 Future Improvements

- 🎤 Voice Tutor
- 📄 PDF Study Material Analysis
- 📷 OCR Support for Notes
- 🌍 Multilingual Learning
- 📅 Google Calendar Integration
- 📈 Advanced Analytics Dashboard

---

## 📸 Demo

### Study Planner
Generate personalized study schedules.

### Tutor
Interactive AI-powered learning assistant.

### Quiz Generator
Generate topic-based quizzes instantly.

### Progress Dashboard
Track learning performance over time.

---

## 📌 Key Highlights

- Multi-Agent AI Architecture
- Personalized Learning
- Interactive Tutoring
- Automatic Quiz Generation
- Progress Tracking
- Clean Streamlit Interface
- Google Gemini Integration

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push

```bash
git push origin feature-name
```

5. Create a Pull Request

---

