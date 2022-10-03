from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    address = db.Column(db.Text(), nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def get_all_users():
        return User.query.all()
  
    def get_user(self,id, email=None):
        user = User.query.get(id=id)
        if not id and email is not None:
            user = User.query.filter(email=email).first()
        return user
  
    def __repr__(self):
        return f'<Name: {self.first_name} {self.last_name}>'
