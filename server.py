from flask import Flask, redirect, render_template, url_for, request

import data_manager

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_route():
    return render_template('list.html')


if __name__ == '__name__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
        )
