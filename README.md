# AI Safety API

This project is a **Flask-based REST API** for managing AI safety-related incident reports.

---

## 📦 How to Build / Install / Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ayus6086/ai_safety_api.git
   cd ai_safety_api

2. **Set up a Virtual Environment (recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies:
   ```bash
   pip install -r requirements.txt

5. Set up the Database:
   ```bash
   python db_setup.py

5. Run the Application:
   ```bash
   python app.py

**The app will be available at:**
➔ http://127.0.0.1:5000

### 🛠 Language & Framework:
- **Language**: Python 3
- **Framework**: Flask
- **ORM**: Flask-SQLAlchemy
- **Database**: SQLite (for local development)


**🛢️ Database Setup & Configuration:**
The database used is SQLite.

The database file (incidents.db) is automatically created when you run:
   ```bash
   python db_setup.py

