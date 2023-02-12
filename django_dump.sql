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

ALTER SCHEMA public OWNER TO root;

COMMENT ON SCHEMA public IS 'standard public schema';
SET default_tablespace = '';
SET default_table_access_method = heap;

ALTER TABLE public.auth_group OWNER TO root;
ALTER TABLE public.auth_group_permissions OWNER TO root;
ALTER TABLE public.auth_permission OWNER TO root;
ALTER TABLE public.auth_user OWNER TO root;
ALTER TABLE public.auth_user_groups OWNER TO root;
ALTER TABLE public.auth_user_user_permissions OWNER TO root;
ALTER TABLE public.books_book OWNER TO root;
ALTER TABLE public.books_book_genres OWNER TO root;
ALTER TABLE public.books_genre OWNER TO root;
ALTER TABLE public.borrows_borrow OWNER TO root;
ALTER TABLE public.django_admin_log OWNER TO root;
ALTER TABLE public.django_content_type OWNER TO root;
ALTER TABLE public.django_migrations OWNER TO root;
ALTER TABLE public.django_session OWNER TO root;
ALTER TABLE public.forums_forum OWNER TO root;
ALTER TABLE public.forums_message OWNER TO root;
ALTER TABLE public.libraries_library OWNER TO root;
ALTER TABLE public.libraries_libraryhasbook OWNER TO root;
ALTER TABLE public.reading_groups_readinggroup OWNER TO root;
ALTER TABLE public.reading_groups_readinggrouphasuser OWNER TO root;
ALTER TABLE public.users_profile OWNER TO root;

INSERT INTO public.auth_user VALUES (1, 'pbkdf2_sha256$390000$tA7zu9XbN9OG297e3GbaCy$/PAi9PiVRhX3MBZw8NLE//VacORAep0l0NurxDrHtEo=', '2023-02-12 10:06:38.296848+01', true, 'admin', 'John', 'SuperUser', 'admin@esgi.fr', true, true, '2023-01-21 17:42:29.988495+01');
INSERT INTO public.auth_user VALUES (6, 'pbkdf2_sha256$390000$tA7zu9XbN9OG297e3GbaCy$/PAi9PiVRhX3MBZw8NLE//VacORAep0l0NurxDrHtEo=', '2023-02-12 10:07:18.905579+01', false, 'librarian', 'James', 'LibraryMan', 'librarian@esgi.fr', false, true, '2023-01-27 21:33:14+01');
INSERT INTO public.auth_user VALUES (3, 'pbkdf2_sha256$390000$tA7zu9XbN9OG297e3GbaCy$/PAi9PiVRhX3MBZw8NLE//VacORAep0l0NurxDrHtEo=', '2023-02-12 10:07:30.474256+01', false, 'reader', 'Tom', 'TheReader', 'reader@esgi.fr', false, true, '2023-01-24 15:48:05+01');

INSERT INTO public.books_book VALUES ('c912d765-5aa4-4ee3-9fc3-1899b623a83a', 'Les chemins de la liberté', 'John Glen', 'BookSkill Production', '-');
INSERT INTO public.books_book VALUES ('a7450510-5113-4f61-acca-ab923f5e86aa', 'Les rêves de la nuit', 'Tony M', 'BookSkill Production', 'LOTY 2019');
INSERT INTO public.books_book VALUES ('ce6adbb7-236d-459f-8aae-b567e4faf8d2', 'Les ailes du destin', 'Tony M', 'Livre de poche', 'LOTY 2019');
INSERT INTO public.books_book VALUES ('50e77c3b-c88b-4472-9c5b-c7d5b41a9196', 'Le temps qui passe', 'Jack Mathew', 'DPS', '-');
INSERT INTO public.books_book VALUES ('a51f6443-c52c-458f-9b89-28452dd4ea06', 'L''ombre de la forêt', 'Elena Scott', 'Maison 1556', '-');
INSERT INTO public.books_book VALUES ('d057e093-5d62-4a91-8014-f5cdc2befc63', 'L''écho des montagnes', 'Tony M', 'Livre de poche', 'LOTY 2019');
INSERT INTO public.books_book VALUES ('905ce793-175b-4d87-b43c-8208d2d52fae', 'Les étoiles cachées', 'Tony M', 'DPS', 'LOTY 2019');
INSERT INTO public.books_book VALUES ('d305f06b-e691-44cc-887d-79e58a18c691', 'Les mots perdus', 'John Glen', 'Livre de poche', 'Jeunesse ');
INSERT INTO public.books_book VALUES ('6d980be3-dd2c-41d0-b08f-791d8316a5d0', 'Les secrets de la mer', 'Jack Mathew', 'Maison 1556', 'Jeunesse ');
INSERT INTO public.books_genre VALUES ('84c640f8-d02f-443d-98ec-2faf79aa565c', 'Horror');
INSERT INTO public.books_genre VALUES ('84da36b0-6b37-4a53-a766-c002a3fb2db7', 'Manga');
INSERT INTO public.books_genre VALUES ('544b7b39-2ee3-4d6d-b2f8-ee506e318cdd', 'Thriller');
INSERT INTO public.books_genre VALUES ('335fce11-4c5c-4286-b3dc-784c6edcb287', 'Roman');

INSERT INTO public.forums_forum VALUES ('35f12f47-2554-431f-ab76-01b71d0b5c11', 'c912d765-5aa4-4ee3-9fc3-1899b623a83a');
INSERT INTO public.forums_forum VALUES ('ea2d5481-5840-4c34-9127-ed6614a9661e', 'a7450510-5113-4f61-acca-ab923f5e86aa');
INSERT INTO public.forums_forum VALUES ('6f00ec75-b41f-4c05-8088-2b6073ec3298', 'ce6adbb7-236d-459f-8aae-b567e4faf8d2');
INSERT INTO public.forums_forum VALUES ('3441a7c6-d365-48bd-80ff-f1f2e54d162a', '50e77c3b-c88b-4472-9c5b-c7d5b41a9196');
INSERT INTO public.forums_forum VALUES ('628898f5-893d-47bf-a098-8dd0dbcdeb9c', 'a51f6443-c52c-458f-9b89-28452dd4ea06');
INSERT INTO public.forums_forum VALUES ('e7064fba-683f-415c-95cb-584a65a76a0d', 'd057e093-5d62-4a91-8014-f5cdc2befc63');
INSERT INTO public.forums_forum VALUES ('d7980899-44f9-42f0-b016-ff87ba997e58', '905ce793-175b-4d87-b43c-8208d2d52fae');
INSERT INTO public.forums_forum VALUES ('cc982506-2dd4-4f0d-8fcc-b0451094eeff', 'd305f06b-e691-44cc-887d-79e58a18c691');
INSERT INTO public.forums_forum VALUES ('84ab4f82-1832-49c9-bd71-aae4666b73dd', '6d980be3-dd2c-41d0-b08f-791d8316a5d0');

INSERT INTO public.books_book_genres VALUES (1, '50e77c3b-c88b-4472-9c5b-c7d5b41a9196', '544b7b39-2ee3-4d6d-b2f8-ee506e318cdd');
INSERT INTO public.books_book_genres VALUES (2, '905ce793-175b-4d87-b43c-8208d2d52fae', '544b7b39-2ee3-4d6d-b2f8-ee506e318cdd');
INSERT INTO public.books_book_genres VALUES (3, 'a51f6443-c52c-458f-9b89-28452dd4ea06', '84c640f8-d02f-443d-98ec-2faf79aa565c');
INSERT INTO public.books_book_genres VALUES (4, 'd305f06b-e691-44cc-887d-79e58a18c691', '84c640f8-d02f-443d-98ec-2faf79aa565c');
INSERT INTO public.books_book_genres VALUES (5, '6d980be3-dd2c-41d0-b08f-791d8316a5d0', '84c640f8-d02f-443d-98ec-2faf79aa565c');
INSERT INTO public.books_book_genres VALUES (6, '6d980be3-dd2c-41d0-b08f-791d8316a5d0', '335fce11-4c5c-4286-b3dc-784c6edcb287');
INSERT INTO public.books_book_genres VALUES (7, '6d980be3-dd2c-41d0-b08f-791d8316a5d0', '84da36b0-6b37-4a53-a766-c002a3fb2db7');
INSERT INTO public.books_book_genres VALUES (8, 'c912d765-5aa4-4ee3-9fc3-1899b623a83a', '84c640f8-d02f-443d-98ec-2faf79aa565c');
INSERT INTO public.books_book_genres VALUES (9, 'c912d765-5aa4-4ee3-9fc3-1899b623a83a', '544b7b39-2ee3-4d6d-b2f8-ee506e318cdd');
INSERT INTO public.books_book_genres VALUES (10, 'ce6adbb7-236d-459f-8aae-b567e4faf8d2', '84c640f8-d02f-443d-98ec-2faf79aa565c');
INSERT INTO public.books_book_genres VALUES (11, 'a7450510-5113-4f61-acca-ab923f5e86aa', '335fce11-4c5c-4286-b3dc-784c6edcb287');
INSERT INTO public.books_book_genres VALUES (12, 'a7450510-5113-4f61-acca-ab923f5e86aa', '84da36b0-6b37-4a53-a766-c002a3fb2db7');
INSERT INTO public.books_book_genres VALUES (13, 'd057e093-5d62-4a91-8014-f5cdc2befc63', '544b7b39-2ee3-4d6d-b2f8-ee506e318cdd');

INSERT INTO public.django_admin_log VALUES (1, '2023-01-23 17:08:24.352521+01', '68269ae6-b8b9-4cfe-8f7e-d852bf8cf9c5', 'Genre object (68269ae6-b8b9-4cfe-8f7e-d852bf8cf9c5)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (2, '2023-01-23 17:08:50.232284+01', 'fbd83299-9d43-4d5a-9508-731d6aa7e5d0', 'Genre object (fbd83299-9d43-4d5a-9508-731d6aa7e5d0)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (3, '2023-01-23 17:09:00.545937+01', '7a86923a-74da-44c3-8482-39f6c4b1f60c', 'Genre object (7a86923a-74da-44c3-8482-39f6c4b1f60c)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (4, '2023-01-23 17:09:04.840813+01', '7a86923a-74da-44c3-8482-39f6c4b1f60c', 'Genre object (7a86923a-74da-44c3-8482-39f6c4b1f60c)', 2, '[]', 10, 1);
INSERT INTO public.django_admin_log VALUES (5, '2023-01-23 17:27:09.450122+01', '682962ee-1f73-46db-bb9f-e80906573fe0', 'Library object (682962ee-1f73-46db-bb9f-e80906573fe0)', 1, '[{"added": {}}]', 2, 1);
INSERT INTO public.django_admin_log VALUES (6, '2023-01-23 18:11:32.035954+01', '84c640f8-d02f-443d-98ec-2faf79aa565c', 'Genre object (84c640f8-d02f-443d-98ec-2faf79aa565c)', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (7, '2023-01-24 15:30:27.281795+01', 'f7ab7b45-a2d8-4cbf-adc2-789fc446ddc7', 'ReadingGroup object (f7ab7b45-a2d8-4cbf-adc2-789fc446ddc7)', 1, '[{"added": {}}]', 14, 1);
INSERT INTO public.django_admin_log VALUES (8, '2023-01-24 15:32:33.337709+01', '682962ee-1f73-46db-bb9f-e80906573fe0', 'une biblio', 2, '[{"changed": {"fields": ["Name"]}}]', 2, 1);
INSERT INTO public.django_admin_log VALUES (9, '2023-01-24 15:46:20.430227+01', '2', 'client', 1, '[{"added": {}}]', 7, 1);
INSERT INTO public.django_admin_log VALUES (10, '2023-01-24 15:47:37.096459+01', '2', 'client', 2, '[{"changed": {"fields": ["First name", "Last name", "Email address"]}}]', 7, 1);
INSERT INTO public.django_admin_log VALUES (11, '2023-01-24 17:10:44.049154+01', '1', 'theclient in 2023-01-24 14:30:19+00:00 -> 2023-01-26 14:30:24+00:00 : une biblio', 1, '[{"added": {}}]', 15, 1);
INSERT INTO public.django_admin_log VALUES (12, '2023-01-24 17:11:10.643998+01', '1', 'theclient in 2023-01-24 14:30:19+00:00 -> 2023-01-26 14:30:24+00:00 : une biblio', 3, '', 15, 1);
INSERT INTO public.django_admin_log VALUES (13, '2023-01-24 17:11:29.662767+01', '2', 'client', 3, '', 7, 1);
INSERT INTO public.django_admin_log VALUES (14, '2023-01-24 17:11:36.951317+01', '3', 'client', 2, '[{"changed": {"fields": ["Username"]}}]', 7, 1);
INSERT INTO public.django_admin_log VALUES (15, '2023-01-24 17:53:47.223219+01', '92feb825-5ec7-4635-9136-fc7ed1e09b93', '2023-01-24 16:27:00+01:00 -> 2023-01-24 18:27:00+01:00 : une biblio', 2, '[{"changed": {"fields": ["End at"]}}]', 14, 1);
INSERT INTO public.django_admin_log VALUES (16, '2023-01-25 19:35:49.215849+01', '544b7b39-2ee3-4d6d-b2f8-ee506e318cdd', 'thriller', 1, '[{"added": {}}]', 10, 1);
INSERT INTO public.django_admin_log VALUES (17, '2023-01-25 19:36:08.275791+01', '50e77c3b-c88b-4472-9c5b-c7d5b41a9196', 'boboboo', 1, '[{"added": {}}]', 1, 1);
INSERT INTO public.django_admin_log VALUES (18, '2023-01-27 21:30:35.646646+01', '4', 'adelsen', 3, '', 7, 1);
INSERT INTO public.django_admin_log VALUES (19, '2023-01-27 21:32:15.98385+01', '5', 'adelsen', 3, '', 7, 1);
INSERT INTO public.django_admin_log VALUES (20, '2023-02-11 21:52:53.038322+01', '6', 'lib', 2, '[{"changed": {"fields": ["Username", "First name", "Last name", "Email address"]}}]', 7, 1);
INSERT INTO public.django_admin_log VALUES (21, '2023-02-11 21:55:02.483202+01', '6', 'lib', 2, '[{"changed": {"fields": ["password"]}}]', 7, 1);

INSERT INTO public.libraries_library VALUES ('682962ee-1f73-46db-bb9f-e80906573fe0', 'Jojo Wango', 12, 14);

INSERT INTO public.reading_groups_readinggroup VALUES ('f7ab7b45-a2d8-4cbf-adc2-789fc446ddc7', '2023-01-24 15:30:19+01', '2023-01-26 15:30:24+01', '682962ee-1f73-46db-bb9f-e80906573fe0');
INSERT INTO public.reading_groups_readinggroup VALUES ('92feb825-5ec7-4635-9136-fc7ed1e09b93', '2023-01-24 16:27:00+01', '2023-01-24 18:27:00+01', '682962ee-1f73-46db-bb9f-e80906573fe0');
INSERT INTO public.reading_groups_readinggroup VALUES ('1669c4ac-e32b-45b7-a246-d235f3f0432c', '2023-02-13 23:32:00+01', '2023-02-23 23:32:00+01', '682962ee-1f73-46db-bb9f-e80906573fe0');
INSERT INTO public.reading_groups_readinggroup VALUES ('2a00e815-1fa4-496c-8f04-72a2d0ef3892', '2023-02-16 23:33:00+01', '2023-02-17 23:33:00+01', '682962ee-1f73-46db-bb9f-e80906573fe0');

INSERT INTO public.users_profile VALUES (6, 'LIBRARIAN', 6);
INSERT INTO public.users_profile VALUES (7, 'READER', 3);

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
SELECT pg_catalog.setval('public.auth_permission_id_seq', 68, true);
SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
SELECT pg_catalog.setval('public.auth_user_id_seq', 8, true);
SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
SELECT pg_catalog.setval('public.books_book_genres_id_seq', 13, true);
SELECT pg_catalog.setval('public.django_admin_log_id_seq', 21, true);
SELECT pg_catalog.setval('public.django_content_type_id_seq', 17, true);
SELECT pg_catalog.setval('public.django_migrations_id_seq', 28, true);
SELECT pg_catalog.setval('public.reading_groups_readinggrouphasuser_id_seq', 3, true);
SELECT pg_catalog.setval('public.users_profile_id_seq', 7, true);

REVOKE USAGE ON SCHEMA public FROM PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;
GRANT ALL ON SCHEMA public TO PUBLIC;

