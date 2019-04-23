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

ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_tag_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_answer_id;
ALTER TABLE IF EXISTS ONLY public.tag DROP CONSTRAINT IF EXISTS pk_tag_id;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS pk_question_tag_id;
ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS pk_comment_id;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS pk_answer_id;
ALTER TABLE IF EXISTS public.tag ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.question ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.comment ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.answer ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.tag_id_seq;
DROP TABLE IF EXISTS public.tag;
DROP TABLE IF EXISTS public.question_tag;
DROP SEQUENCE IF EXISTS public.question_id_seq;
DROP TABLE IF EXISTS public.question;
DROP SEQUENCE IF EXISTS public.comment_id_seq;
DROP TABLE IF EXISTS public.comment;
DROP SEQUENCE IF EXISTS public.answer_id_seq;
DROP TABLE IF EXISTS public.answer;
DROP EXTENSION IF EXISTS plpgsql;
DROP SCHEMA IF EXISTS public;
--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: rozner
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text
);


ALTER TABLE public.answer OWNER TO rozner;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: rozner
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO rozner;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rozner
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: rozner
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer
);


ALTER TABLE public.comment OWNER TO rozner;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: rozner
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO rozner;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rozner
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: rozner
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text
);


ALTER TABLE public.question OWNER TO rozner;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: rozner
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO rozner;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rozner
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: rozner
--

CREATE TABLE public.question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.question_tag OWNER TO rozner;

--
-- Name: tag; Type: TABLE; Schema: public; Owner: rozner
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO rozner;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: rozner
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO rozner;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: rozner
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (1, '2017-04-28 16:49:00', 4, 1, 'You need to use brackets: my_list = []', NULL);
INSERT INTO public.answer (id, submission_time, vote_number, question_id, message, image) VALUES (2, '2017-04-25 14:42:00', 35, 1, 'Look it up in the Python docs', 'images/image2.jpg');


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (1, 0, NULL, 'Please clarify the question as it is too vague!', '2017-05-01 05:49:00', NULL);
INSERT INTO public.comment (id, question_id, answer_id, message, submission_time, edited_count) VALUES (2, NULL, 1, 'I think you could use my_list = list() as well.', '2017-05-02 16:55:00', NULL);


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (0, '2017-04-28 08:29:00', 29, 7, 'How to make lists in Python?', 'I am totally new to this, any hints?', NULL);
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (1, '2017-04-29 09:19:00', 15, 9, 'Wordpress loading multiple jQuery Versions', 'I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();

I could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.

BUT in my theme i also using jquery via webpack so the loading order is now following:

jquery
booklet
app.js (bundled file with webpack, including jquery)', 'images/image1.png');
INSERT INTO public.question (id, submission_time, view_number, vote_number, title, message, image) VALUES (2, '2017-05-01 10:41:00', 1364, 57, 'Drawing canvas with an image picked with Cordova Camera Plugin', 'I''m getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I''m on IOS, it throws errors such as cross origin issue, or that I''m trying to use an unknown format.
', NULL);


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.question_tag (question_id, tag_id) VALUES (0, 1);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (1, 3);
INSERT INTO public.question_tag (question_id, tag_id) VALUES (2, 3);


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: rozner
--

INSERT INTO public.tag (id, name) VALUES (1, 'python');
INSERT INTO public.tag (id, name) VALUES (2, 'sql');
INSERT INTO public.tag (id, name) VALUES (3, 'css');


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.answer_id_seq', 2, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.comment_id_seq', 2, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.question_id_seq', 2, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: rozner
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- Name: answer pk_answer_id; Type: CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);


--
-- Name: comment pk_comment_id; Type: CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);


--
-- Name: question pk_question_id; Type: CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);


--
-- Name: question_tag pk_question_tag_id; Type: CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);


--
-- Name: tag pk_tag_id; Type: CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);


--
-- Name: comment fk_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: answer fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: comment fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: rozner
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

