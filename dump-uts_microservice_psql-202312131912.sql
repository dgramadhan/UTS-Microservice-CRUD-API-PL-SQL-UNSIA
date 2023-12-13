--
-- PostgreSQL database dump
--

-- Dumped from database version 15.3
-- Dumped by pg_dump version 15.3

-- Started on 2023-12-13 19:12:44

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3403 (class 1262 OID 155764)
-- Name: uts_microservice_psql; Type: DATABASE; Schema: -; Owner: admin_galih
--

CREATE DATABASE uts_microservice_psql WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Indonesia.1252';


ALTER DATABASE uts_microservice_psql OWNER TO admin_galih;

\connect uts_microservice_psql

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 215 (class 1259 OID 155766)
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin_galih
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin_galih;

--
-- TOC entry 223 (class 1259 OID 155838)
-- Name: log_access; Type: TABLE; Schema: public; Owner: admin_galih
--

CREATE TABLE public.log_access (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    status character varying(255) NOT NULL,
    login_date timestamp without time zone NOT NULL
);


ALTER TABLE public.log_access OWNER TO admin_galih;

--
-- TOC entry 222 (class 1259 OID 155837)
-- Name: log_access_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_galih
--

CREATE SEQUENCE public.log_access_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.log_access_id_seq OWNER TO admin_galih;

--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 222
-- Name: log_access_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_galih
--

ALTER SEQUENCE public.log_access_id_seq OWNED BY public.log_access.id;


--
-- TOC entry 219 (class 1259 OID 155794)
-- Name: permissions; Type: TABLE; Schema: public; Owner: admin_galih
--

CREATE TABLE public.permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    role_id integer NOT NULL
);


ALTER TABLE public.permissions OWNER TO admin_galih;

--
-- TOC entry 218 (class 1259 OID 155793)
-- Name: permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_galih
--

CREATE SEQUENCE public.permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.permissions_id_seq OWNER TO admin_galih;

--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 218
-- Name: permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_galih
--

ALTER SEQUENCE public.permissions_id_seq OWNED BY public.permissions.id;


--
-- TOC entry 221 (class 1259 OID 155829)
-- Name: roles; Type: TABLE; Schema: public; Owner: admin_galih
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    role_name character varying(255) NOT NULL,
    description character varying(255) NOT NULL
);


ALTER TABLE public.roles OWNER TO admin_galih;

--
-- TOC entry 220 (class 1259 OID 155828)
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_galih
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_seq OWNER TO admin_galih;

--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 220
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_galih
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


--
-- TOC entry 217 (class 1259 OID 155783)
-- Name: users; Type: TABLE; Schema: public; Owner: admin_galih
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    address character varying(255) NOT NULL,
    phone_number character varying(255) NOT NULL
);


ALTER TABLE public.users OWNER TO admin_galih;

--
-- TOC entry 216 (class 1259 OID 155782)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: admin_galih
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO admin_galih;

--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 216
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin_galih
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3232 (class 2604 OID 155841)
-- Name: log_access id; Type: DEFAULT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.log_access ALTER COLUMN id SET DEFAULT nextval('public.log_access_id_seq'::regclass);


--
-- TOC entry 3230 (class 2604 OID 155797)
-- Name: permissions id; Type: DEFAULT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.permissions ALTER COLUMN id SET DEFAULT nextval('public.permissions_id_seq'::regclass);


--
-- TOC entry 3231 (class 2604 OID 155832)
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- TOC entry 3229 (class 2604 OID 155786)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3389 (class 0 OID 155766)
-- Dependencies: 215
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin_galih
--

COPY public.alembic_version (version_num) FROM stdin;
b2d3b30a0361
\.


--
-- TOC entry 3397 (class 0 OID 155838)
-- Dependencies: 223
-- Data for Name: log_access; Type: TABLE DATA; Schema: public; Owner: admin_galih
--

COPY public.log_access (id, username, status, login_date) FROM stdin;
1	cobsa	Gagal Login	2023-12-08 17:32:27.869458
2	coba	Gagal Login	2023-12-08 17:32:27.869458
3	coba	Gagal Login	2023-12-08 17:32:27.869458
4	coba	Gagal Login	2023-12-08 17:32:27.869458
5	coba	Gagal Login	2023-12-08 17:39:15.96014
6	coba	Gagal Login	2023-12-08 17:39:15.96014
7	coba	Berhasil Login	2023-12-08 17:39:39.860838
8	coba	Berhasil Login	2023-12-08 22:50:47.443342
9	coba	Gagal Login	2023-12-08 22:50:47.443342
10	coba2	Gagal Login	2023-12-08 22:50:47.443342
11	coba2	Gagal Login	2023-12-08 22:50:47.443342
12	coba2	Gagal Login	2023-12-08 22:50:47.443342
13	coba	Berhasil Login	2023-12-08 22:50:47.443342
14	coba	Berhasil Login	2023-12-08 22:56:15.546938
15	coba	Berhasil Login	2023-12-08 22:57:04.160581
16	coba	Berhasil Login	2023-12-08 23:00:32.635951
17	admin	Gagal Login	2023-12-08 23:00:32.635951
18	admin	Gagal Login	2023-12-08 23:01:52.010095
19	admin	Berhasil Login	2023-12-08 23:01:52.010095
20	admin	Berhasil Login	2023-12-08 23:05:50.425657
21	admin	Berhasil Login	2023-12-11 16:16:22.142919
22	admin	Berhasil Login	2023-12-11 16:18:25.689502
23	admin	Berhasil Login	2023-12-11 16:18:25.689502
24	admin	Berhasil Login	2023-12-11 16:18:25.689502
25	user1	Gagal Login	2023-12-11 16:18:25.689502
26	user1	Gagal Login	2023-12-11 16:20:30.785003
27	user1	Berhasil Login	2023-12-11 16:20:30.785003
28	budi	Gagal Login	2023-12-11 16:21:53.540469
29	budi	Berhasil Login	2023-12-11 16:54:52.752124
30	ujang	Berhasil Login	2023-12-11 16:54:52.752124
\.


--
-- TOC entry 3393 (class 0 OID 155794)
-- Dependencies: 219
-- Data for Name: permissions; Type: TABLE DATA; Schema: public; Owner: admin_galih
--

COPY public.permissions (id, user_id, role_id) FROM stdin;
11	56	6
10	57	6
\.


--
-- TOC entry 3395 (class 0 OID 155829)
-- Dependencies: 221
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: admin_galih
--

COPY public.roles (id, role_name, description) FROM stdin;
7	\\xc30d04070302d8516e0fa023d3bb6dd2360126217acf99a9bfad708c3a3853f1103e1fed9ed00531b863fd48deb31202dd1195b196b8edaf879d36f8553165534276eb80150961	\\xc30d040703024f2b36f7cad0966a7ed23a0149cfa2eac87295319f2546d98f4d3d64f8d1c7c3dfd1cf06124903f393ce0883ed0cf43f394a9a69354ef23c694f4efc02876938ba6671bf05
6	\\xc30d0407030270eecceaaf9c3d1973d23e01aae17aa26b98d65e47ecd9931560bcc51f24414e80f798441306097ba96a7c112db27a033cc3b0448b7d53d1e0112d4b2c6664e7b67b3650e880b763ec	\\xc30d04070302937ef10dd8e5b32678d24201c6f29190b43aab7a1150f57d4b3847b132154ec1f19ae8f5de3835f9448dfca0057e79b57124d06b6f7c6e6f008bb644e637324fbf3fe402c86584f8699b46e17c
\.


--
-- TOC entry 3391 (class 0 OID 155783)
-- Dependencies: 217
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: admin_galih
--

COPY public.users (id, username, email, password, address, phone_number) FROM stdin;
57	\\xc30d040703021ce199fc00de6f4b6fd23601a214967425e7db4e1513a48ba4ccc7484e5d45b53c0f733bb8b7c93c2ca47627d680bd9943d4efed8d8bb9f126f47bea35cd5f26f3	\\xc30d040703021e3663b3604a72ae74d24001c4d1417a5bb3ca805c6586730d35e0b4e8c64a12d8fa7944ae1342831a099e16af498b593e62e539931e61ad846bf814a2ca7af7c11aafcd822b9cb734ac29	\\xc30d04070302a5a92d68dffb720b7dd23601bec9f0fb677ed8b803cd75a75908406c2867b7361cbf78b5aa8bca2ad3bbec616336c10a0288a4dd824b0174df2e2b7f077f0745aa	\\xc30d0407030205bb57b5d8b62cd371d25201ea9c32f75ec83e946dff124a6a7757bf62e3b36d4a0635525532247dbc73d36a0ef9516f87fdac5bf68c5e59e9a04bcfa41f6dbd9abcac930edf544257391f5637b2fe75dcc0af7d8eed11646d917a6523	\\xc30d0407030283d1947aa13a77af66d23b01005ba6b6354842da761eaef051e9d510164f67cf7302b4478c9b4d5e90248e21a5af87e5eaa5f8dd5a32439b79b1ff79fdca5336fb94e69f5bb6
56	\\xc30d040703026d955720e532bb6763d235017940c4a6f476156d9c63c12d2ec6b879381fb1ac4a17590bd2afdaa32695c0b96cdee7502358cf67383329062ffdf4389716abfe	\\xc30d04070302425a0fd62e3ad31c74d23f011a13c1e57d0b08500175202153adda32d5419be6954deae55b7217205ba3f620f186e1c7bfe71ad857a7832b049497b91c2c61bbd49a2832607cb6325990	\\xc30d04070302d2d558e7171969a164d23501364a9146d96fcd0e3eaadbc3603d6683eb128a68458674bee83843e9dc3e589e41f7271857aa4f60f62d7fb402e1c6ecc70287d9	\\xc30d040703025a2ec984aa79b04e68d25b018196ebaffb320319421804df8b247761e0aa41ed24fd3e19ca3e691da31f68e80e452dbce48c77ceabf90d3de260c37e7e640fd3085b2d35d6cec71aa8da2d80a6ec51798ff30cf5d4065f5ccd2a0411c72643e755995dac4cac	\\xc30d04070302d1c69be68fccbbba6dd23b01e84274c71c3a00355d9f3ea409e33f2182d4d331cbb8b173fac21a278bab8a89727e85d6984edc57a34f4713d348407e5485278f7ee9aed24aa0
\.


--
-- TOC entry 3409 (class 0 OID 0)
-- Dependencies: 222
-- Name: log_access_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_galih
--

SELECT pg_catalog.setval('public.log_access_id_seq', 30, true);


--
-- TOC entry 3410 (class 0 OID 0)
-- Dependencies: 218
-- Name: permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_galih
--

SELECT pg_catalog.setval('public.permissions_id_seq', 11, true);


--
-- TOC entry 3411 (class 0 OID 0)
-- Dependencies: 220
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_galih
--

SELECT pg_catalog.setval('public.roles_id_seq', 8, true);


--
-- TOC entry 3412 (class 0 OID 0)
-- Dependencies: 216
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin_galih
--

SELECT pg_catalog.setval('public.users_id_seq', 58, true);


--
-- TOC entry 3234 (class 2606 OID 155770)
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- TOC entry 3244 (class 2606 OID 155843)
-- Name: log_access log_access_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.log_access
    ADD CONSTRAINT log_access_pkey PRIMARY KEY (id);


--
-- TOC entry 3240 (class 2606 OID 155799)
-- Name: permissions permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT permissions_pkey PRIMARY KEY (id);


--
-- TOC entry 3242 (class 2606 OID 155836)
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- TOC entry 3236 (class 2606 OID 155792)
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- TOC entry 3238 (class 2606 OID 155790)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3245 (class 2606 OID 155869)
-- Name: permissions fk_permission_role_id; Type: FK CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT fk_permission_role_id FOREIGN KEY (role_id) REFERENCES public.roles(id);


--
-- TOC entry 3246 (class 2606 OID 155864)
-- Name: permissions fk_permission_user_id; Type: FK CONSTRAINT; Schema: public; Owner: admin_galih
--

ALTER TABLE ONLY public.permissions
    ADD CONSTRAINT fk_permission_user_id FOREIGN KEY (user_id) REFERENCES public.users(id);


-- Completed on 2023-12-13 19:12:44

--
-- PostgreSQL database dump complete
--

