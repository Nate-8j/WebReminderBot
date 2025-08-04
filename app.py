from flask import Flask, render_template, request

from config import repository

app = Flask(__name__)


@app.route('/')
def index():
    user_id = 5022508915
    reminders = repository.get_reminders(user_id=user_id)
    print(reminders)

    return render_template("reminders.html", reminders=reminders)



if __name__ == '__main__':
    app.run(debug=True)