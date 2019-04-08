from flask import Flask, render_template, redirect, request, url_for
import data_manager
from datetime import datetime



app = Flask(__name__)


@app.route('/')
@app.route('/list')
def list_route():
    questions = sorted(data_manager.get_question_data(), key=lambda key: key['submission_time'], reverse=True)
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_selected_question(question_id: int):
    question = data_manager.get_question_data(question_id)
    answers = data_manager.get_answer_data(question_id)
    print(question)
    print(answers)
    return render_template('question.html', question=question, answers=answers, question_id=question_id)


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        message = request.form.get("message")
        title = request.form.get('title')
        image = request.form.get('image')
        view_number = 0
        vote_number = 0
        submission_time = datetime.now()
        data_manager.add_question(message, title, image, view_number, vote_number, submission_time)
        return redirect(f'/question/{question_id}')
    return render_template('add_question.html')


@app.route('/question/<question_id>/add_answer', methods=['GET', 'POST'])
def add_answer(question_id: int):
    if request.method == 'POST':
        message = request.form.get('message')
        picture = request.form.get('picture')
        data = data_manager.update_answer_data(message, picture, question_id)
        filepath = ANSWER_FILEPATH
        data_manager.write_data(filepath, ANSWWER_DATA_HEADER, data)
        return redirect(f'/question/{question_id}')

    return render_template('add_answer.html', question_id=question_id)


@app.route('/question/<question_id>/remove', methods=['GET', 'POST'])
def remove_question(question_id):
    data_manager.remove_question(QUESTION_FILEPATH, question_id)
    return redirect('/list')


@app.route('/question/<question_id>/remove_answer_<answer_id>')
def remove_answer(answer_id, question_id):
    data_manager.remove_answers(answer_id)
    return redirect(f'/question/{question_id}')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
