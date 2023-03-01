from datetime import datetime
from pyfiles import db
# datetime object containing current date and time

def update_user_login(user):
    user.last_login = datetime.now()
    db.session.add(user)
    db.session.commit()