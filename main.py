from src import create_app
#init schedule manager !
import src.utils.schedule_manager
app = create_app()


if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug=True, host="0.0.0.0", port=5000)
