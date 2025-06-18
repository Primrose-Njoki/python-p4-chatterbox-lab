from app import app
from models import db, Message

with app.app_context():
    db.drop_all()
    db.create_all()

    m1 = Message(body="Hello world!", username="Ian")
    m2 = Message(body="This is Flask!", username="Primrose")

    db.session.add_all([m1, m2])
    db.session.commit()
