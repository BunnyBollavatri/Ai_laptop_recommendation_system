# 💻 AI-Powered Laptop Recommendation System

An intelligent laptop recommendation platform that leverages **AI agents, PostgreSQL, and Streamlit** to deliver real-time, data-driven laptop suggestions based on user preferences such as budget, performance, RAM, value-for-money, and gaming capability.

Designed using scalable architecture principles to simulate a real-world recommendation engine.

---

## 🚀 Project Overview

Choosing the right laptop can be overwhelming due to the vast number of options available. This system simplifies the decision-making process by analyzing laptop specifications and recommending the best devices using optimized SQL queries and AI-driven logic.

The application provides:

✅ Smart budget recommendations  
✅ Performance-based filtering  
✅ AI-calculated value rankings  
✅ Gaming laptop detection  
✅ Interactive UI  
✅ Fast database retrieval  

---

## ⭐ Key Features

### 🔎 Smart Budget Search
- Automatically applies a **price buffer** to avoid missing high-value laptops near the budget range.

### ⚡ Performance Filtering
- Find laptops with higher RAM configurations instantly.

### 📊 AI Value Score
Laptops are ranked using a weighted scoring formula:
    Value Score =
        (RAM Weight + CPU Tier + Storage Factor) / Price


This ensures users receive **maximum performance per rupee**.

### 🎮 Gaming Laptop Detector
Gaming machines are identified using GPU indicators and premium series such as:

- NVIDIA RTX / GTX
- AMD RX
- ASUS ROG / TUF
- Lenovo Legion
- Acer Predator / Nitro

Minimum requirements include:

✅ 16GB RAM  
✅ Dedicated GPU indicators  

---

## 🧠 System Architecture

User → Streamlit UI → Python Backend → SQLAlchemy → PostgreSQL → AI Formatting → Recommendations.


### Architecture Breakdown

**Frontend**
- Streamlit (Interactive Web UI)

**Backend**
- Python
- Agent-based modular design

**Database**
- PostgreSQL
- Optimized SQL queries for fast retrieval

**AI Layer**
- Groq LLM integration
- Tool-based agent execution

---

## 🏗️ Architecture Diagram

        ┌─────────────────┐
        │   Streamlit UI  │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │  Python Backend │
        │   (Agents)      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   SQLAlchemy    │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   PostgreSQL    │
        └─────────────────┘



---

## 🛠️ Tech Stack

### 👨‍💻 Programming Language
- Python

### ⚙️ Frameworks & Libraries
- Streamlit  
- SQLAlchemy  
- LangChain  
- Groq API  
- Pandas  

### 🗄️ Database
- PostgreSQL

---

## 📂 Project Structure


---

## 🛠️ Tech Stack

### 👨‍💻 Programming Language
- Python

### ⚙️ Frameworks & Libraries
- Streamlit  
- SQLAlchemy  
- LangChain  
- Groq API  
- Pandas  

### 🗄️ Database
- PostgreSQL

---

## 📂 Project Structure

AI-Laptop-Recommendation-System/
│
├── agents/ → AI agent logic
├── tools/ → SQL query tools
├── db/ → Database connection
├── app.py → Streamlit UI
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Laptop-Recommendation-System.git
cd AI-Laptop-Recommendation-System

## 2) Create Virtual Environment
python -m venv venv

# Activate:

# Windows

venv\Scripts\activate

# 3) Install Dependencies
pip install -r requirements.txt

# 4)Configure PostgreSQL

#Create a database and update your connection string inside:

db/connection.py

#Example DATABASE_URL = "postgresql://username:password@localhost:5432/laptop_db"

# 5)Add API Key

# Create a .env file:

GROQ_API_KEY=your_api_key_here


# 6) Run the Application
streamlit run app.py

