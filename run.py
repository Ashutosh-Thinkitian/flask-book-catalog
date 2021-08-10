from app import create_app, db

from app.auth.models import User

flask_app = create_app('prod')

# flask gives us to ability to run multiple application with each set of config
# tell to flask use current application context
with flask_app.app_context():
    db.create_all()

    if not User.query.filter_by(user_name='ashu').first():
        User.create_user(user='ashu', email='ashutosh.patil@thinkitive.com', password='11121997')
        flask_app.run()
