from datetime import datetime
from pyfiles import db


def update_user_login(user):
    user.last_login = datetime.utcnow()
    db.session.commit()
