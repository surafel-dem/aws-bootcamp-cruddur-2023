CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
DROP TABLE IF EXISTS public.users;
DROP TABLE IF EXISTS public.activities;


CREATE TABLE public.users (
  uuid UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
  display_name text,
  handle text,
  email text,
  cognito_user_id text,
  created_at TIMESTAMP default current_timestamp
);

CREATE TABLE public.activities (
  uuid UUID default uuid_generate_v4() primary key,
  user_uuid UUID REFERENCES public.users(uuid),
  message text,
  replies_count integer default 0,
  reposts_count integer default 0,
  likes_count integer default 0,
  reply_to_activity_uuid integer,
  expires_at timestamp,
  created_at timestamp default current_timestamp 
);
