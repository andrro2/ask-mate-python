import connection

@connection.connection_handler
def get_question_data(cursor, question_id=None):
    if question_id:
        cursor.execute("""
                                select * from question
                                where id = %(question_id)s;""", {'question_id': question_id})
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
                    select id from answer where question_id = %(question_id)s
                    
                    """, {'question_id':question_id})
    answer_ids = cursor.fetchall()
    for item in answer_ids:
        answer_id = item['id']
        cursor.execute("""
                        delete from comment where answer_id = %(answer_id)s;
                        """, {'answer_id': answer_id})

    cursor.execute("""
                    delete from comment where question_id = %(question_id)s;
                    delete from question_tag where question_id = %(question_id)s;
                    delete from answer where question_id = %(question_id)s;
                    delete from question where id = %(question_id)s;
                    """,{'question_id': question_id})


@connection.connection_handler
def remove_answers(cursor, answer_id):
    cursor.execute("""
                    delete from comment where answer_id = %(answer_id)s;
                    delete from answer where id = %(answer_id)s;0
                    """,{'answer_id': answer_id})

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

@connection.connection_handler
def add_comment_to_question(cursor, question_id, comment, time):
        cursor.execute("""
                        insert into comment (question_id, message, submission_time)
                        values (%s, %s, %s);""", (question_id, comment, time))


@connection.connection_handler
def get_question_comment(cursor, question_id):
    cursor.execute("""
                    select message, submission_time from comment
                    where question_id = %(question_id)s;""", {'question_id': question_id})
    datas = cursor.fetchall()
    return datas


@connection.connection_handler
def add_comment_to_answer(cursor, answer_id, comment, time):
        cursor.execute("""
                        insert into comment (answer_id, message, submission_time)
                        values (%s, %s, %s);""", (answer_id, comment, time))


@connection.connection_handler
def get_question_comment(cursor, question_id):
    cursor.execute("""
                    select message, submission_time from comment
                    where question_id = %(question_id)s;""", {'question_id': question_id})
    datas = cursor.fetchall()
    return datas


@connection.connection_handler
def get_answer_comment(cursor, answer_id):
    cursor.execute("""
                    select message, submission_time from comment
                    where answer_id = %(answer_id)s;""", {'answer_id': answer_id})
    datas = cursor.fetchall()
    return datas

@connection.connection_handler
def get_answer_ids(cursor, question_id):
    cursor.execute("""
                    select id from answer
                    where question_id = %(question_id)s;""", {'question_id': question_id})
    ids = cursor.fetchall()
    return ids


@connection.connection_handler
def get_latest_five_questions(cursor):
    cursor.execute("""
                    select * from question
                    order by submission_time desc limit 5;""")
    latest_questions = cursor.fetchall()
    return latest_questions


@connection.connection_handler
def get_answer_ids(cursor, question_id):
    cursor.execute("""
                    select id from answer
                    where question_id = %(question_id)s;""", {'question_id': question_id})
    ids = cursor.fetchall()
    return ids

@connection.connection_handler
def search(cursor, search):
    cursor.execute("""
                    select title, message from question
                    where message like %(search)s or title like %(search)s
                    """, {'search': search})
    questions = cursor.fetchall()

    cursor.execute("""
                        select message from answer
                        where message like %(search)s
                        """, {'search': search})
    answers = cursor.fetchall()

    cursor.execute("""
                        select message from comment
                        where message like %(search)s
                        """, {'search': search})
    comments = cursor.fetchall()
    return questions, answers, comments



