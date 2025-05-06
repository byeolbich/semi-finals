import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Francis Rose Esterado, BSIT 3, ITE 322 - System Integration and Architecture 1, Semi Final Exam!'


if __name__ == '__main__':
    app.run()
