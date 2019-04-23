create table answer
(
  id              serial not null
    constraint pk_answer_id
      primary key,
  submission_time timestamp,
  vote_number     integer,
  question_id     integer
    constraint fk_question_id
      references question,
  message         text,
  image           text,
  user_id         integer
    constraint fk_user_id
      references users
);

alter table answer
  owner to rozner;

create unique index answer_user_id_uindex
  on answer (user_id);

INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (1, '2017-04-28 16:49:00.000000', 4, 1, 'You need to use brackets: my_list = []', null, null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (2, '2017-04-25 14:42:00.000000', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg', null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (4, '2019-04-12 08:44:56.571766', 0, 3, 'Au is astronomical unit
1 Au is the average distance of Sun and Earth', null, null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (5, '2019-04-12 08:52:31.639136', 0, 4, 'Binary star system is where there is 2 star which orbiting each other or where one star orbiting the other
', null, null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (6, '2019-04-12 08:54:39.511676', 0, 5, 'It is a constellation which looks like a giraffe', null, null);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image, user_id) VALUES (3, '2019-04-12 08:44:08.362649', 0, 3, 'Au means Astronomical unit...', null, null);
create table comment
(
  id              serial not null
    constraint pk_comment_id
      primary key,
  question_id     integer
    constraint fk_question_id
      references question,
  answer_id       integer
    constraint fk_answer_id
      references answer,
  message         text,
  submission_time timestamp,
  edited_count    integer,
  user_id         integer
    constraint fk_user_id
      references users
);

alter table comment
  owner to rozner;

create unique index comment_user_id_uindex
  on comment (user_id);

INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (1, 0, null, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00.000000', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (2, null, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00.000000', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (3, null, 4, 'Thx for the info', '2019-04-12 08:45:15.621360', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (4, 3, null, 'Nem tudom.', '2019-04-12 10:28:56.386170', null, null);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count, user_id) VALUES (5, null, 3, 'Helyes', '2019-04-12 10:29:09.688568', null, null);
create table question
(
  id              serial not null
    constraint pk_question_id
      primary key,
  submission_time timestamp,
  view_number     integer,
  vote_number     integer,
  title           text,
  message         text,
  image           text,
  user_id         integer
    constraint fk_user_id
      references users
);

alter table question
  owner to rozner;

create unique index question_user_id_uindex
  on question (user_id);

INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (0, '2017-04-28 08:29:00.000000', 29, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', null, null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (1, '2017-04-29 09:19:00.000000', 15, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (2, '2017-05-01 10:41:00.000000', 1364, 57, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', null, null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (3, '2019-04-12 08:43:22.728214', 0, 0, 'What is AU', 'What AU means?', '', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (4, '2019-04-12 08:50:47.314861', 0, 0, 'Binary star system?', 'What is a binary star system', '', null);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image, user_id) VALUES (5, '2019-04-12 08:53:54.798455', 0, 0, 'Camelopardalis?', 'What is this Camelopardalis', '', null);
create table question_tag
(
  question_id integer not null
    constraint fk_question_id
      references question,
  tag_id      integer not null
    constraint fk_tag_id
      references tag,
  constraint pk_question_tag_id
    primary key (question_id, tag_id)
);

alter table question_tag
  owner to rozner;

INSERT INTO public.question_tag (question_id, tag_id) VALUES (0, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 3);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 3);
create table tag
(
  id   serial not null
    constraint pk_tag_id
      primary key,
  name text
);

alter table tag
  owner to rozner;

INSERT INTO public.tag (id, name) VALUES (1, 'python');
INSERT INTO public.tag (id, name) VALUES (2, 'sql');
INSERT INTO public.tag (id, name) VALUES (3, 'css');
create table users
(
  id                serial not null
    constraint users_pk
      primary key,
  user_name         text,
  password          text,
  registration_time timestamp
);

alter table users
  owner to rozner;

create unique index users_id_uindex
  on users (id);

