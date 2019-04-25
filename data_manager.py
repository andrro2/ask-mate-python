import connection


@connection.connection_handler
def get_user_login_data(cursor, user_name):
    cursor.execute("""
                            select user_name, password from users
                            where user_name like %(user_name)s;
                """, {'user_name': user_name})
    return cursor.fetchall()


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
def add_answer(cursor, submission_time, vote_number, question_id, message, image, userid):
    cursor.execute("""
                    insert into answer (submission_time, vote_number, question_id, message, image, user_id)
                    values (%s, %s, %s, %s, %s, %s);""",
                   (submission_time, vote_number, question_id, message, image, userid))


@connection.connection_handler
def remove_question(cursor, question_id):
    cursor.execute("""
                    select id from answer where question_id = %(question_id)s

                    """, {'question_id': question_id})
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
                    """, {'question_id': question_id})


@connection.connection_handler
def remove_answers(cursor, answer_id):
    cursor.execute("""
                    delete from comment where answer_id = %(answer_id)s;
                    delete from answer where id = %(answer_id)s;
                    """, {'answer_id': answer_id})


@connection.connection_handler
def add_question(cursor, message, title, image, view_number, vote_number, submission_time, user_id):
    cursor.execute("""
                    insert into question (submission_time, view_number, vote_number, title, message, image, user_id)
                     values (%s, %s, %s, %s, %s, %s, %s);""",
                   (submission_time, view_number, vote_number, title, message, image, user_id))
    cursor.execute("""
                    select id from question
                    where submission_time = %(submission_time)s;""", {'submission_time': submission_time})
    question_id = cursor.fetchall()
    return question_id


@connection.connection_handler
def add_comment_to_question(cursor, question_id, comment, time, userid):
    cursor.execute("""
                        insert into comment (question_id, message, submission_time, user_id)
                        values (%s, %s, %s, %s);""", (question_id, comment, time, userid))


@connection.connection_handler
def get_question_comment(cursor, question_id):
    cursor.execute("""
                    select message, submission_time from comment
                    where question_id = %(question_id)s;""", {'question_id': question_id})
    datas = cursor.fetchall()
    return datas


@connection.connection_handler
def add_comment_to_answer(cursor, answer_id, comment, time, userid):
    cursor.execute("""
                        insert into comment (answer_id, message, submission_time, user_id)
                        values (%s, %s, %s, %s);""", (answer_id, comment, time, userid))


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
def edit_answer(cursor, answer_id, message):
    cursor.execute("""
                    update answer
                    set message = %(message)s
                    where id = %(answer_id)s;""", {'message': message, 'answer_id': answer_id})


@connection.connection_handler
def search(cursor, search):
    cursor.execute("""
                    select DISTINCT question.* from answer
                    full join question on question.id = answer.question_id
                    where answer.message ilike %(search)s or question.title ilike %(search)s or question.message ilike %(search)s;

                    """, {'search': search})
    questions = cursor.fetchall()

    return questions


@connection.connection_handler
def list_all_users(cursor):
    cursor.execute("""
                    SELECT user_name, registration_time FROM users;
    """)
    all_users = cursor.fetchall()
    return all_users


@connection.connection_handler
def add_new_user(cursor, user_data):
    cursor.execute("""
                    INSERT INTO users(user_name, password, registration_time)
                    VALUES (%s, %s, %s)
                    """, (user_data.get('user_name'), user_data.get('password'), user_data.get('registration_time')))


@connection.connection_handler
def get_user_id(cursor, username):
    cursor.execute("""
                    select id from users
                    where user_name = %(username)s;""", {'username': username})
    u_id = cursor.fetchone()
    for u in u_id:
        return u_id[u]
    return 'There is no such username'


@connection.connection_handler
def check_registration_name(cursor, regi_name):
    cursor.execute("""
                    select user_name from users 
                    where user_name = %(regi_name)s;""", {'regi_name': regi_name})
    result = cursor.fetchone()
    return result
