from src import create_app
from flask_apscheduler import APScheduler
app = create_app()

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from src.utils.scheduled_tasks import delete_old_users
@scheduler.task('interval', id='do_job_1', seconds=15)
def job1():
    with scheduler.app.app_context():
        print('Job 1 executed')
        delete_old_users()

if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug=True, host="0.0.0.0", port=5000)
