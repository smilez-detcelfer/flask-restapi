from datetime import datetime, timedelta
import os
from src.models import db, User


def delete_old_users():
    print('scheduled job "delete old users" in use')
    current_time = datetime.utcnow()
    # set user deletion delta here:
    two_month_ago = current_time - timedelta(days=3)
    user_for_delete = User.query.filter(User.last_login < two_month_ago).all()
    #making log info
    user_log_list = list(map(lambda user:
                             f'{user.id},{user.username},{user.last_login}, {current_time}',
                             user_for_delete))
    print(f'{len(user_log_list)} users will be deleted')
    User.query.filter(User.last_login < two_month_ago).delete()
    db.session.commit()
    #change log file path here:
    logfile_path = os.path.join(os.getcwd(), "logs", "delete_old_users.log")
    with open(logfile_path, 'a', encoding='UTF-8') as file:
        file.writelines(line + '\n' for line in user_log_list)


# from src.utils.scheduler import delete_old_users
# # scheduled jobs:
# scheduler = BackgroundScheduler(daemon=True)
# scheduler.add_job(delete_old_users, 'interval', seconds=20)
# scheduler.start()