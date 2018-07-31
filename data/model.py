""" Create Database """
from flask_sqlalchemy import SQLAlchemy
import time

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """User of Newsflash"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256))

    events = db.relationship("Event",
                            secondary = "user_events",
                            backref="users")

    def __repr__(self):
        """Representation of User instance"""

        return "<User: user_id={}, email={}>".format(self.user_id, self.email)


class Search(db.Model):
    """Event saved by User on website."""

    __tablename__ = "events"

    event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    event_term = db.Column(db.String(64), unique=True)

    def __repr__(self):
        """Representation of Search instance"""

        return "<Search: event_id={}, event_term={}>".format(self.event_id, self.event_term)

class User_Event(db.Model):
    """ Tracks Events saved by User"""

    __tablename__ = "user_events"

    user_event_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'),
                         nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                         nullable=False)
 
    def __repr__(self):
        """Representation of User instance"""

        return "<Outlet: user_event_id={}, search_id={}, user_id={}>".format(self.user_event_id, self.event_id, self.user_id)


##############################################################################
# Model definitions

def connect_to_db(app, db_url='postgresql:///ctdb'):
    """ Connect database to Flask app"""
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."
