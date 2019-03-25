import csv

DATA_HEADER = ['id','submission_time','view_number','vote_number','title','message','image']

def get_user_story(story_id=None):
    return get_csv_data(story_id)

def get_csv_data(filename, one_user_story_id=None):
    """
    :param one_user_story_id:
        If given, it will act as a filter and return the dictionary of one specific User Story
        If not given, it will return a list of dictionaries with all the details
    :return:
    """
    #  create a temporary list to read each line
    user_questions = []

    #  open csv file to read
    with open(filename, encoding='utf-8') as csvfile:
        #  use DictReader to directly create dictionaries from each lines in the csv file
        reader = csv.DictReader(csvfile)

        #  read all lines in csv file
        for row in reader:
            #  make a copy of the read row, since we can't modify it
            user_story = dict(row)

            # if filtered, then just return this _found_ user story
            if one_user_story_id is not None and one_user_story_id == user_story['id']:
                return user_story

            #  store modified data in temporary list
            user_questions.append(user_story)
    print(user_questions)
    # return the temporary list
    return user_questions

get_csv_data('/home/zsana/Codecool/WEB/ask-mate-python/sample_data/question.csv')