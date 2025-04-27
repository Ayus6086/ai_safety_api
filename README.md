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

6. Run the Application:
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


***📡 API Endpoints (with Examples)***
Method | Endpoint | Description | Example
GET | / | Home page | Open browser or curl http://127.0.0.1:5000/
GET | /incidents | Get all incidents | curl http://127.0.0.1:5000/incidents
POST | /incidents | Create new incident | curl -X POST http://127.0.0.1:5000/incidents -H "Content-Type: application/json" -d "{\"title\": \"Test\", \"description\": \"Test description\", \"severity\": \"High\"}"
PUT | /incidents/<id> | Update an incident | curl -X PUT http://127.0.0.1:5000/incidents/1 -H "Content-Type: application/json" -d "{\"title\": \"Updated Title\"}"
DELETE | /incidents/<id> | Delete an incident | curl -X DELETE http://127.0.0.1:5000/incidents/1
```

### ✍️ Design Decisions / Challenges
- **Simple Design** : Flask with SQLite for quick setup, avoiding complex configuration.

- **Modular Code**: Separate models.py for database models.

- **Error Handling**: Basic error handling for wrong requests.

- **Challenge**: Managing database sessions outside app context was tricky initially.