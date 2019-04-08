
import time
import os
import connection




@connection.connection_handler
def get_question_data(cursor, question_id=None):
    if question_id:
        cursor.execute("""
                        select * from question where id = %(question_id)s 
                        """,{'question_id': question_id})
        user_questions = cursor.fetchall()
    else:
        cursor.execute("""
                        select * from question;
                        """)
        user_questions = cursor.fetchall()
    return user_questions

@connection.connection_handler
def add_question(cursor, message, title, image, view_number, vote_number, submission_time):
    cursor.execute("""
                    insert into question (submission_time, view_number, vote_number, title, message, image)
                    values (%s, %s, %s, %s, %s, %s);
                    """, (submission_time, view_number,vote_number, title, message, image))



@connection.connection_handler
def get_answer_data(cursor, question_id=None):
    cursor.execute("""
                    select * from answer where question_id = %(question_id)s
                    """, {'question_id' : question_id})
    question_answers = cursor.fetchall()
    return question_answers


def get_whole_answer_data():
    answers = []
    with open(ANSWER_FILEPATH, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            answer = dict(row)
            answers.append(answer)
    return answers


def update_answer_data(message, image, question_id):
    existing_data = get_whole_answer_data()
    id = generate_new_id(existing_data)
    submission_time = time.time()
    vote_number = 0
    dict = {'id': id, 'submission_time': submission_time, 'vote_number': vote_number, 'question_id': question_id, 'message': message, 'image': image}
    existing_data.append(dict)
    return existing_data


def write_data(filepath, fieldnames, data):
    with open(filepath, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def remove_question(question_data_path, question_id):
    remove_answers(question_id=question_id)
    data = get_question_data()
    for index, item in enumerate(data):
        if question_id == item['id']:
            data.pop(index)
    write_data(question_data_path, QUESTION_DATA_HEADER, data)


def remove_answers(answer_id=None, question_id=None):
    indexes = []
    data = get_whole_answer_data()
    if question_id is not None:
        for index in range(-(len(data)),0):
            if question_id == data[index]['question_id']:
                data.pop(index)
        write_data(ANSWER_FILEPATH, ANSWWER_DATA_HEADER, data)
    else:
        for index, item in enumerate(data):
            if answer_id == item['id']:
                data.pop(index)
        write_data(ANSWER_FILEPATH, ANSWWER_DATA_HEADER, data)

