from flask import Flask, render_template, redirect, request, make_response, session, escape, url_for
import data_manager
from datetime import datetime
import bcrypt
import util

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def latest_questions():
    questions = data_manager.get_latest_five_questions()
    return render_template('main.html', questions=questions)


@app.route('/list')
def list_route():
    questions = sorted(data_manager.get_question_data(), key=lambda key: key['submission_time'], reverse=True)
    return render_template('all_questions.html', questions=questions)


@app.route('/question/<question_id>', methods=['GET', 'POST'])
def route_selected_question(question_id: int):
    question = data_manager.get_question_data(question_id)
    answers = data_manager.get_answer_data(question_id)
    question_comments = data_manager.get_question_comment(question_id)
    answer_ids = data_manager.get_answer_ids(question_id)
    answer_comments = {}
    for a_id in answer_ids:
        for i in a_id:
            answer_comments[a_id[i]] = data_manager.get_answer_comment(a_id[i])
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
        user_id = data_manager.get_user_id(session['username'])
        question_id = data_manager.add_question(message, title, image, view_number, vote_number, submission_time,user_id)[0][
            'id']
        return redirect(f'/question/{question_id}')
    return render_template('add_question.html')


@app.route('/question/<question_id>/add_answer', methods=['GET', 'POST'])
def add_answer(question_id: int):
    if request.method == 'POST':
        message = request.form.get('message')
        image = request.form.get('picture')
        submission_time = datetime.now()
        vote_number = 0
        try:
            userid = data_manager.get_user_id(session['username'])
        except KeyError:
            userid = None
        data_manager.add_answer(submission_time, vote_number, question_id, message, image, userid)
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
        try:
            userid = data_manager.get_user_id(session['username'])
        except KeyError:
            userid = None
        data_manager.add_comment_to_question(question_id, user_comment, now_time, userid)
        return redirect(f'/question/{question_id}')
    return render_template('add_comment_question.html', question_id=question_id)


@app.route('/answer/<question_id>&<answer_id>/add_comment', methods=['GET', 'POST'])
def add_answer_comment(answer_id: int, question_id: int):
    if request.method == 'POST':
        user_comment = request.form.get('comment')
        now_time = datetime.now()
        try:
            userid = data_manager.get_user_id(session['username'])
        except KeyError:
            userid = None
        data_manager.add_comment_to_answer(answer_id, user_comment, now_time, userid)
        return redirect(f'/question/{question_id}')
    return render_template('add_comment_answer.html', answer_id=answer_id, question_id=question_id)


@app.route('/search')
def search():
    search = '%' + request.args.get('search') + '%'
    questions = data_manager.search(search)
    return render_template('main.html', questions=questions, search=search)


@app.route('/answer/<answer_id>&<question_id>/edit', methods=['GET', 'POST'])
def edit_answer(answer_id: int, question_id: int):
    text = request.args.get('text')
    if request.method == 'POST':
        edited_answer = request.form.get('edit')
        data_manager.edit_answer(answer_id, edited_answer)
        return redirect(f'/question/{question_id}')
    return render_template('edit_answer.html', answer_id=answer_id, text=text, question_id=question_id)


@app.route('/list-users')
def list_users():
    all_users = data_manager.list_all_users()
    return render_template('list_users.html', users=all_users)


def create_user_data():
    passwd = util.hash_password(request.form.get('password'))
    user_data = {
        'user_name': request.form.get('user_name'),
        'password': passwd,
        'registration_time': datetime.now()
    }
    return user_data


@app.route('/registration', methods=['GET', 'POST'])
def save_new_user():
    if request.method == 'POST':
        data_manager.add_new_user(create_user_data())
        return redirect('/')
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login(verified=None):
    if request.method == 'POST':
        user_name = request.form.get('user_name')
        password = request.form.get('password')
        user_login_data = data_manager.get_user_login_data(user_name)
        if len(user_login_data) == 1:
            verified = util.verify_password(password, user_login_data[0]['password'])
            if verified:
                session['username'] = user_name
                return redirect('/')

        else:
            verified = False
    return render_template('login.html', verified=verified)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
