from datetime import datetime
from app import db

class Task(db.Model):
    """
    Task model: represents a to-do item.
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    done = db.Column(db.Boolean, default=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Serialize Task to a dict for JSON responses."""
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done,
            'timestamp': self.timestamp.isoformat()
        }

    def from_dict(self, data):
        """Update Task fields from a dict."""
        for field in ['title', 'done']:
            if field in data:
                setattr(self, field, data[field])
