from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable = False, index=True, unique=True)
    email = db.Column(db.String(120), nullable = False, index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable = False)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
        
    class phonebook(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(64), index=True, unique=True)
        last_name = db.Column(db.String(64), index=True, unique=True)
        mobile_number= db.Column(db.String(120),index=True, unique=True)
        office_number = db.Column(db.String(128), index=True, unique = True)
        date_created = db.Column(db.DateTime, default = datetime.utcnow)

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            db.session.add(self)
            db.session.commit()
    
        def __repr__(self):
            return f'<User {self.id} | {self.first_name}>'   
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = generate_password_hash(kwargs['password'])
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'<User {self.id} | {self.username}>'