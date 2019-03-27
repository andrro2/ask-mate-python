import csv
import time
import os

QUESTION_DATA_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']
ANSWWER_DATA_HEADER = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']

script_dir = os.path.dirname(__file__)
question_rel_path = "sample_data/question.csv"
QUESTION_FILEPATH = os.path.join(script_dir, question_rel_path)
answer_rel_path = "sample_data/answer.csv"
ANSWER_FILEPATH = os.path.join(script_dir, answer_rel_path)


def get_question_data(question_id=None):
    user_questions = []

    with open(QUESTION_FILEPATH, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            question = dict(row)

            if question_id is not None and question_id == question['id']:
                return question

            user_questions.append(question)
    return user_questions


def get_answer_data(question_id=None):
    question_answers = []

    with open(ANSWER_FILEPATH, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            answer = dict(row)

            if question_id is not None and question_id == answer['question_id']:
                question_answers.append(answer)

    return question_answers


def get_whole_answer_data():
    answers = []
    with open(ANSWER_FILEPATH, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            answer = dict(row)
            answers.append(answer)
    return answers


def generate_new_id(existing_data):
    new_id = 0
    for item in existing_data:
        if int(item['id']) >= new_id:
            new_id = int(item['id']) + 1
    return new_id


def update_question_data(title, message, image):
    existing_data = get_question_data()
    id = generate_new_id(existing_data)
    submission_time = time.time()
    wiew_number = 0
    vote_number = 0
    dict = {'id':id, 'submission_time': submission_time, 'view_number': wiew_number, 'vote_number':vote_number, 'title':title, 'message':message, 'image':image}
    existing_data.append(dict)
    return existing_data


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
    remove_answers(question_id)
    data = get_question_data()
    print(data)
    for index, item in enumerate(data):
        if question_id == item['id']:
            data.pop(index)
    write_data(question_data_path, QUESTION_DATA_HEADER, data)


def remove_answers(answer_id=None, question_id=None):
    print(answer_id, question_id)
    data = get_whole_answer_data()
    if question_id is not None:
        for index, item in enumerate(data):
            if question_id == item['question_id']:
                data.pop(index)
        write_data(ANSWER_FILEPATH, ANSWWER_DATA_HEADER, data)
    else:
        for index, item in enumerate(data):
            if answer_id == item['id']:
                data.pop(index)
        write_data(ANSWER_FILEPATH, ANSWWER_DATA_HEADER, data)