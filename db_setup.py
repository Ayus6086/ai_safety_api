from app import app
from extensions import db
from models import Incident

sample_data = [
    Incident(title="AI Overconfidence", description="AI made high-stakes decisions without oversight", severity="High"),
    Incident(title="Data Leak", description="User data exposed by LLM", severity="Medium")
]

with app.app_context():
    db.create_all()
    db.session.add_all(sample_data)
    db.session.commit()
