from flask import Flask, render_template, redirect, request, url_for
import data_manager
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def latest_questions():
    questions = data_manager.get_latest_five_questions()
    return render_template('main.html', questions=questions)


@app.route('/list')
def list_route():
    questions = sorted(data_manager.get_question_data(), key=lambda key: key['submission_time'], reverse=True)
    return render_template('list.html', questions=questions)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_selected_question(question_id: int):
    question = data_manager.get_question_data(question_id)
    answers = data_manager.get_answer_data(question_id)
    question_comments = data_manager.get_question_comment(question_id)
    answer_ids = data_manager.get_answer_ids(question_id)
    answer_comments = {}
    for a_id in answer_ids:
        for i in a_id:
            answer_comments[a_id[i]] = (data_manager.get_answer_comment(a_id[i]))
    return render_template('question.html', question=question, question_id=question_id, answers=answers,
                           question_comments=question_comments, answer_comments=answer_comments)


@app.route('/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        message = request.form.get("message")
        title = request.form.get('title')
        image = request.form.get('image')
        view_number = 0
        vote_number = 0
        submission_time = datetime.now()
        question_id = data_manager.add_question(message, title, image, view_number, vote_number, submission_time)[0]['id']
        return redirect(f'/question/{question_id}')
    return render_template('add_question.html')


@app.route('/question/<question_id>/add_answer', methods=['GET', 'POST'])
def add_answer(question_id: int):
    if request.method == 'POST':
        message = request.form.get('message')
        image = request.form.get('picture')
        submission_time = datetime.now()
        vote_number = 0
        data_manager.add_answer(submission_time, vote_number, question_id, message, image)
        return redirect(f'/question/{question_id}')

    return render_template('add_answer.html', question_id=question_id)


@app.route('/question/<question_id>/remove', methods=['GET', 'POST'])
def remove_question(question_id):
    data_manager.remove_question(question_id)
    return redirect('/list')


@app.route('/question/<question_id>/remove_answer_<answer_id>')
def remove_answer(answer_id, question_id):
    data_manager.remove_answers(answer_id)
    return redirect(f'/question/{question_id}')


@app.route('/question/<question_id>/add_comment', methods=['GET', 'POST'])
def add_question_comment(question_id: int):
    if request.method == 'POST':
        user_comment = request.form.get('comment')
        now_time = datetime.now()
        data_manager.add_comment_to_question(question_id, user_comment, now_time)
        return redirect(f'/question/{question_id}')
    return render_template('add_comment.html')


@app.route('/answer/<answer_id>/add_comment', methods=['GET', 'POST'])
def add_answer_comment(answer_id: int):
    if request.method == 'POST':
        user_comment = request.form.get('comment')
        now_time = datetime.now()
        data_manager.add_comment_to_answer(answer_id, user_comment, now_time)
        return redirect('/')
    return render_template('add_comment.html')


@app.route('/?<search>')
def search(search):
    questions, answers, comments = data_manager.search(search)
    return render_template('search.html', questions=questions, answers=answers, comments=comments, search=search)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
