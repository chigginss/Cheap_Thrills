"""seed database"""

from sqlalchemy import func
from model import User, Event, User_Event, connect_to_db, db
from server import app
from datetime import datetime

# =============================================================================

def example_data():
    """Sample test data for database."""

    user_1 = User(email="hellohellohello@gmail.com", password="1234")
    event_1 = Event(search_term="testestest")
    user_event_1 = User_Event(user_id=1, search_id=1)

    db.session.add_all([user_1, event_1)
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    db.create_all()

    example_data()
    print "Connected to DB."
