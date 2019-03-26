import csv
import os


DATA_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']

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
    user_answers = []

    with open(ANSWER_FILEPATH, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            answer = dict(row)

            if question_id is not None and question_id == answer['question_id']:
                user_answers.append(answer)

    return user_answers

