from app import db, bcrypt      # bcrypt is a instance of flask_bcrypt
from datetime import datetime

from flask_login import UserMixin
from app import login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    user_email = db.Column(db.String(60), unique=True, index=True)
    user_password = db.Column(db.String(80))
    registration_date = db.Column(db.DateTime, default=datetime.utcnow())

    #   for check password in login page
    def check_password(self, password):
        return bcrypt.check_password_hash(self.user_password, password)

    # class methods belongs to this class only not associate with any class instance -> static method
    @classmethod
    def create_user(cls, user, email, password):

        user = cls(
            user_name=user,
            user_email=email,
            user_password=bcrypt.generate_password_hash(password).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        return user

#   for stay login call back function and instance on login_manager
#   this function receive id in unicode format so we return it into int
#   if not found return none
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))