from .app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    dob = db.Column(db.DateTime(), nullable=False) 
    date_created  = db.Column(db.DateTime, server_default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Name: {self.first_name} {self.last_name}>'
