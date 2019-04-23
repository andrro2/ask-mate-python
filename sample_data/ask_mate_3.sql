--
-- PostgreSQL database dump
--

-- Dumped from database version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.6 (Ubuntu 10.6-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: rozner
--



--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.question VALUES (0, '2017-04-28 08:29:00', 29, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', NULL, NULL);
INSERT INTO public.question VALUES (1, '2017-04-29 09:19:00', 15, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png', NULL);
INSERT INTO public.question VALUES (2, '2017-05-01 10:41:00', 1364, 57, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', NULL, NULL);
INSERT INTO public.question VALUES (3, '2019-04-12 08:43:22.728214', 0, 0, 'What is AU', 'What AU means?', '', NULL);
INSERT INTO public.question VALUES (4, '2019-04-12 08:50:47.314861', 0, 0, 'Binary star system?', 'What is a binary star system', '', NULL);
INSERT INTO public.question VALUES (5, '2019-04-12 08:53:54.798455', 0, 0, 'Camelopardalis?', 'What is this Camelopardalis', '', NULL);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.answer VALUES (1, '2017-04-28 16:49:00', 4, 1, 'You need to use brackets: my_list = []', NULL, NULL);
INSERT INTO public.answer VALUES (2, '2017-04-25 14:42:00', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg', NULL);
INSERT INTO public.answer VALUES (4, '2019-04-12 08:44:56.571766', 0, 3, 'Au is astronomical unit
1 Au is the average distance of Sun and Earth', NULL, NULL);
INSERT INTO public.answer VALUES (5, '2019-04-12 08:52:31.639136', 0, 4, 'Binary star system is where there is 2 star which orbiting each other or where one star orbiting the other
', NULL, NULL);
INSERT INTO public.answer VALUES (6, '2019-04-12 08:54:39.511676', 0, 5, 'It is a constellation which looks like a giraffe', NULL, NULL);
INSERT INTO public.answer VALUES (3, '2019-04-12 08:44:08.362649', 0, 3, 'Au means Astronomical unit...', NULL, NULL);


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.comment VALUES (1, 0, NULL, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00', NULL, NULL);
INSERT INTO public.comment VALUES (2, NULL, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00', NULL, NULL);
INSERT INTO public.comment VALUES (3, NULL, 4, 'Thx for the info', '2019-04-12 08:45:15.62136', NULL, NULL);
INSERT INTO public.comment VALUES (4, 3, NULL, 'Nem tudom.', '2019-04-12 10:28:56.38617', NULL, NULL);
INSERT INTO public.comment VALUES (5, NULL, 3, 'Helyes', '2019-04-12 10:29:09.688568', NULL, NULL);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.tag VALUES (1, 'python');
INSERT INTO public.tag VALUES (2, 'sql');
INSERT INTO public.tag VALUES (3, 'css');


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.question_tag VALUES (0, 1);
INSERT INTO public.question_tag VALUES (1, 3);
INSERT INTO public.question_tag VALUES (2, 3);


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.answer_id_seq', 6, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.comment_id_seq', 5, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.question_id_seq', 5, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- PostgreSQL database dump complete
--

