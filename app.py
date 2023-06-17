from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)


class Session_():
    def __ini__(user: str, logged: bool, log_start: datetime=None):
        self.user = user
        self.logged = logged
        self.log_start = datetime.now()

    def create_session(context):
        user, log_status = None, None
        user, log_satus = check_loggin(context)
        if log_status:
            return Session(user, log_statusa)
        else:
            return False

    def check_loggin(context: dict):
        pass


@app.route("/index", methods = ["GET", "POST"])
def index():
    pass

@app.route("/loggin", methods = ["GET", "POST"])
def loggin():
    if request.method == "GET":
        return render_template('/auth/loggin.html')
    elif request.method == "POST":
        pass

@app.route("/", methods = ["GET"])
def main(session):
    if session:
        index()
    else:
        loggin()

@app.route("/index", methods = ["GET", "POST"])
def index():
    pass

if __name__ == "__main__":
    app.run('localhost', 8000, debug=True)
