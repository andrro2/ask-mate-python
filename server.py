from flask import Flask, render_template, redirect, request
import connection

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_route():
    questions = connection.get_user_story(url_for('question.csv'))
    return render_template('list.html', questions=questions)


if __name__ == '__name__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
        )
