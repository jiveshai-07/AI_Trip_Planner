# ✈️ AI Trip Planner

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?logo=streamlit)
![OpenRouter](https://img.shields.io/badge/OpenRouter-LLM-orange)
![Meta Llama](https://img.shields.io/badge/Meta-Llama_3.3_70B-purple)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 🌍 Overview

AI Trip Planner is a professional **Multi-Agent AI Travel Planning System** that generates complete travel itineraries using multiple AI agents working together.

Unlike traditional AI travel assistants that rely on a single prompt, this application breaks the planning process into specialized agents, making the generated plans more structured, realistic, and personalized.

The system also integrates Deep Learning for travel style detection using inspiration images and provides weather information, interactive destination maps, currency conversion, downloadable PDF itineraries, trip history, and an AI-powered travel assistant.

---

## ✨ Features

### 🤖 Multi-Agent AI Workflow

- 🔍 Research Agent
- 💰 Budget Planner Agent
- 📅 Itinerary Writer Agent
- 🧐 Reviewer Agent
- 🔁 Self-Correcting Itinerary Generation

---

### 🧠 Artificial Intelligence

- OpenRouter API
- Meta Llama 3.3 70B
- Prompt Engineering
- Multi-Agent Architecture

---

### 📸 Deep Learning

- CLIP Image Classification
- Travel Style Detection
- Personalized Recommendations

---

### 🌍 Travel Features

- Interactive Destination Map
- Live Weather Information
- Currency Conversion
- Google Flights Search
- Trip History
- PDF Export
- AI Travel Chat Assistant

---
## 🏗️ Project Architecture

```
User
   │
   ▼
Plan Trip Page
   │
   ▼
────────────────────────────────────────
Research Agent
        │
        ▼
Budget Planner Agent
        │
        ▼
Itinerary Writer Agent
        │
        ▼
Reviewer Agent
        │
        ▼
Final Trip Plan
────────────────────────────────────────
        │
        ▼
PDF • Chat • Trip History • Maps
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Language | Python |
| Frontend | Streamlit |
| AI Model | Meta Llama 3.3 70B |
| LLM Provider | OpenRouter |
| Deep Learning | OpenAI CLIP |
| Frameworks | Transformers, PyTorch |
| Mapping | Folium |
| Geolocation | Geopy |
| Weather | OpenWeather API |
| Currency | ExchangeRate API |
| PDF | ReportLab |
| Authentication | Streamlit OAuth + Custom Login |

---

## 📁 Project Structure

```text
AI_Trip_Planner/
│
├── agents/
│   ├── researcher.py
│   ├── budget_planner.py
│   ├── itinerary_writer.py
│   └── reviewer.py
│
├── components/
│   ├── auth.py
│   ├── navbar.py
│   └── ui.py
│
├── pages/
│   ├── Plan_Trip.py
│   ├── Trip_History.py
│   ├── Travel_Chat.py
│   ├── About.py
│   └── Settings.py
│
├── utils/
│
├── icons/
├── assets/
├── data/
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📸 Application Screenshots

Replace these images after deployment.

### Dashboard

```
assets/dashboard.png
```

### Plan Trip

```
assets/plan_trip.png
```

### Trip History

```
assets/trip_history.png
```

### Travel Chat

```
assets/travel_chat.png
```

### About Page

```
assets/about.png
```

---
## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/jiveshai-07/AI_Trip_Planner.git
```

### 2️⃣ Navigate into the Project

```bash
cd AI_Trip_Planner
```

### 3️⃣ Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Configure Streamlit Secrets

Create a `.streamlit/secrets.toml` file and add your API keys.

```toml
OPENROUTER_API_KEY = "YOUR_OPENROUTER_API_KEY"

OPENWEATHER_API_KEY = "YOUR_OPENWEATHER_API_KEY"

EXCHANGE_RATE_API_KEY = "YOUR_EXCHANGE_RATE_API_KEY"
```

---

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 🌟 Key Highlights

- 🤖 Multi-Agent AI Architecture
- 🧠 Deep Learning using CLIP
- ✈️ Personalized Trip Planning
- 📍 Interactive Destination Maps
- 🌤️ Live Weather Information
- 💱 Currency Conversion
- 📄 PDF Itinerary Generation
- 💬 AI Travel Assistant
- 🕓 Trip History Management
- 🔐 Secure Authentication
- 📱 Responsive Streamlit Interface

---

# 🎯 Future Improvements

- Flight Price API Integration
- Hotel Booking Integration
- Restaurant Recommendation Agent
- Voice-based Travel Assistant
- Expense Tracking During Trips
- Collaborative Group Trip Planning
- Calendar Synchronization
- Mobile Application

---

# 📊 Project Status

✅ Authentication

✅ Multi-Agent Workflow

✅ Deep Learning Integration

✅ Travel Chat

✅ PDF Export

✅ Trip History

✅ Interactive Maps

✅ Weather Integration

✅ Currency Conversion

✅ Ready for Deployment

---
# 👨‍💻 Author

## Jivesh Mishra

AI & Data Science Enthusiast passionate about building intelligent applications using Artificial Intelligence, Machine Learning, Deep Learning, Large Language Models, Computer Vision, and Python.

### 🌐 Connect with Me

- **LinkedIn:** https://www.linkedin.com/in/jivesh-mishra
- **GitHub:** https://github.com/jiveshai-07

---

# 🙏 Acknowledgements

This project was built using several amazing open-source technologies and APIs.

Special thanks to:

- OpenRouter
- Meta AI (Llama 3.3 70B)
- Streamlit
- Hugging Face Transformers
- OpenAI CLIP
- PyTorch
- Folium
- ReportLab
- Geopy

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

💡 Open an issue for suggestions

🤝 Contributions are always welcome!

---

# 📜 License

This project is licensed under the **MIT License**.

See the **LICENSE** file for more information.

---

<p align="center">

### ✈️ Built with ❤️ using Multi-Agent AI, OpenRouter, Meta Llama 3.3 70B, Streamlit & CLIP

</p>