import connection

@connection.connection_handler
def get_question_data(cursor, question_id=None):
    if question_id:
        cursor.execute("""
                                select * from question
                                where id = (%s);""", question_id)
        user_questions = cursor.fetchall()
        return user_questions
    else:
        cursor.execute("""
                        select * from question;""")
        user_questions = cursor.fetchall()
        return user_questions

@connection.connection_handler
def get_answer_data(cursor, question_id=None):
    cursor.execute("""
                    select * from answer
                    where question_id = %(question_id)s""", {'question_id': question_id})
    question_answers = cursor.fetchall()
    return question_answers

@connection.connection_handler
def add_answer(cursor, submission_time, vote_number, question_id, message, image):
    cursor.execute("""
                    insert into answer (submission_time, vote_number, question_id, message, image)
                    values (%s, %s, %s, %s, %s);""", (submission_time, vote_number, question_id, message, image))

@connection.connection_handler
def remove_question(cursor, question_id):
    cursor.execute("""
                    DELETE from answer where question_id = %(question_id)s;
                    DELETE from question where id = %(question_id)s;""", {'question_id': question_id})


@connection.connection_handler
def remove_answers(cursor, answer_id):
    cursor.execute("""
                    DELETE from answer
                    where id = %(answer_id)s;""", {'answer_id': answer_id})

@connection.connection_handler
def add_question(cursor, message, title, image, view_number, vote_number, submission_time):
    cursor.execute("""
                    insert into question (submission_time, view_number, vote_number, title, message, image)
                     values (%s, %s, %s, %s, %s, %s);""", (submission_time, view_number,vote_number, title, message, image))
    cursor.execute("""
                    select id from question
                    where submission_time = %(submission_time)s;""", {'submission_time': submission_time})
    question_id = cursor.fetchall()
    return question_id

