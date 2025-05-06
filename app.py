import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')
    return 'Francis Rose Esterado, BSIT 3, ITE 322 - System Integration and Architecture 1, Semi Final Exam!'


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)