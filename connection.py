import csv

filename = '/home/rozner/codecool/web/1st_tw/ask-mate-python/sample_data/question.csv'
DATA_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']

def get_user_story(story_id=None):
    return get_csv_data(story_id)

def get_csv_data(filename, one_user_story_id=None):
    user_questions = []

    with open(filename, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            user_story = dict(row)

            if one_user_story_id is not None and one_user_story_id == user_story['id']:
                return user_story

            user_questions.append(user_story)
    return user_questions

