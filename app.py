from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///incidents.db'
db = SQLAlchemy(app)

# Model
class Incident(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    severity = db.Column(db.String(10), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "severity": self.severity,
            "reported_at": self.reported_at.isoformat()
        }

# Routes
@app.route('/')
def home():
    return "AI Safety API is running!"

@app.route('/incidents', methods=['GET'])
def get_incidents():
    incidents = Incident.query.all()
    return jsonify([incident.to_dict() for incident in incidents])

@app.route('/incidents', methods=['POST'])
def create_incident():
    data = request.get_json()
    new_incident = Incident(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )
    db.session.add(new_incident)
    db.session.commit()
    return jsonify(new_incident.to_dict()), 201

@app.route('/incidents/<int:id>', methods=['PUT'])
def update_incident(id):
    incident = Incident.query.get_or_404(id)
    data = request.get_json()

    incident.title = data.get('title', incident.title)
    incident.description = data.get('description', incident.description)
    incident.severity = data.get('severity', incident.severity)

    db.session.commit()
    return jsonify({'message': 'Incident updated successfully'})

@app.route('/incidents/<int:id>', methods=['DELETE'])
def delete_incident(id):
    incident = Incident.query.get_or_404(id)
    db.session.delete(incident)
    db.session.commit()
    return jsonify({'message': 'Incident deleted successfully'})

# Run server
if __name__ == '__main__':
    app.run(debug=True)