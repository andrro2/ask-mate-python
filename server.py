from flask import Flask, render_template, redirect, request, url_for
import connection
import os


app = Flask(__name__)

@app.route('/')
@app.route('/list')
def list_route():
    questions = connection.get_question_data()
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_selected_question(question_id: int):
    question = connection.get_question_data(question_id)
    answers = connection.get_answer_data(question_id)
    return render_template('question.html', question=question, answers=answers)

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
        )
