from app import app
from flask import render_template



@app.route('/')
def index():
    return render_template('MainPage.html')


if __name__ == '__main__':
    app.run()