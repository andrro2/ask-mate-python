from flask import Flask, render_template, redirect, request, url_for
import connection

app = Flask(__name__)
filename = '/home/rozner/codecool/web/1st_tw/ask-mate-python/sample_data/question.csv'

@app.route('/')
@app.route('/list')
def list_route():
    questions = connection.get_user_story(filename)
    return render_template('list.html', questions=questions)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
        )
