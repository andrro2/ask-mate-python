UPDATE public.answer SET submission_time = '2017-04-28 16:49:00.000000', vote_number = 4, question_id = 1, message = 'You need to use brackets: my_list = []', image = null, user_id = null WHERE id = 1;
UPDATE public.answer SET submission_time = '2017-04-25 14:42:00.000000', vote_number = 35, question_id = 1, message = 'Look it up in the Python docs', image = 'images/image2.jpg', user_id = null WHERE id = 2;
UPDATE public.answer SET submission_time = '2019-04-12 08:44:56.571766', vote_number = 0, question_id = 3, message = 'Au is astronomical unit
1 Au is the average distance of Sun and Earth', image = null, user_id = null WHERE id = 4;
UPDATE public.answer SET submission_time = '2019-04-12 08:52:31.639136', vote_number = 0, question_id = 4, message = 'Binary star system is where there is 2 star which orbiting each other or where one star orbiting the other
', image = null, user_id = null WHERE id = 5;
UPDATE public.answer SET submission_time = '2019-04-12 08:54:39.511676', vote_number = 0, question_id = 5, message = 'It is a constellation which looks like a giraffe', image = null, user_id = null WHERE id = 6;
UPDATE public.answer SET submission_time = '2019-04-12 08:44:08.362649', vote_number = 0, question_id = 3, message = 'Au means Astronomical unit...', image = null, user_id = null WHERE id = 3;
UPDATE public.comment SET question_id = 0, answer_id = null, message = 'Please clarify the question as it is too vague!', submission_time = '2017-05-01 05:49:00.000000', edited_count = null, user_id = null WHERE id = 1;
UPDATE public.comment SET question_id = null, answer_id = 1, message = 'I think you could use my_list = list() as well.', submission_time = '2017-05-02 16:55:00.000000', edited_count = null, user_id = null WHERE id = 2;
UPDATE public.comment SET question_id = null, answer_id = 4, message = 'Thx for the info', submission_time = '2019-04-12 08:45:15.621360', edited_count = null, user_id = null WHERE id = 3;
UPDATE public.comment SET question_id = 3, answer_id = null, message = 'Nem tudom.', submission_time = '2019-04-12 10:28:56.386170', edited_count = null, user_id = null WHERE id = 4;
UPDATE public.comment SET question_id = null, answer_id = 3, message = 'Helyes', submission_time = '2019-04-12 10:29:09.688568', edited_count = null, user_id = null WHERE id = 5;
UPDATE public.question SET submission_time = '2017-04-28 08:29:00.000000', view_number = 29, vote_number = 7, title = 'How to make lists in Python?', message = 'I am totally new to this, any hints?', image = null, user_id = null WHERE id = 0;
UPDATE public.question SET submission_time = '2017-04-29 09:19:00.000000', view_number = 15, vote_number = 9, title = 'Wordpress loading multiple jQuery Versions', message = 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', image = 'images/image1.png', user_id = null WHERE id = 1;
UPDATE public.question SET submission_time = '2017-05-01 10:41:00.000000', view_number = 1364, vote_number = 57, title = 'Drawing canvas with an image picked with Cordova Camera Plugin', message = 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', image = null, user_id = null WHERE id = 2;
UPDATE public.question SET submission_time = '2019-04-12 08:43:22.728214', view_number = 0, vote_number = 0, title = 'What is AU', message = 'What AU means?', image = '', user_id = null WHERE id = 3;
UPDATE public.question SET submission_time = '2019-04-12 08:50:47.314861', view_number = 0, vote_number = 0, title = 'Binary star system?', message = 'What is a binary star system', image = '', user_id = null WHERE id = 4;
UPDATE public.question SET submission_time = '2019-04-12 08:53:54.798455', view_number = 0, vote_number = 0, title = 'Camelopardalis?', message = 'What is this Camelopardalis', image = '', user_id = null WHERE id = 5;
UPDATE public.question_tag SET  WHERE question_id = 0 AND tag_id = 1;
UPDATE public.question_tag SET  WHERE question_id = 1 AND tag_id = 3;
UPDATE public.question_tag SET  WHERE question_id = 2 AND tag_id = 3;
UPDATE public.tag SET name = 'python' WHERE id = 1;
UPDATE public.tag SET name = 'sql' WHERE id = 2;
UPDATE public.tag SET name = 'css' WHERE id = 3;
