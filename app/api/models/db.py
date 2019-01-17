import os
import psycopg2
from instance.config import app_config


tables = [
            'users',
            'meetups',
            'questions',
            'comments',
            'sessions',
            'rsvp',


        ]

table_queries = [

            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY NOT NULL,
                firstname VARCHAR(255) NOT NULL,
                lastname VARCHAR(255) NOT NULL,
                othername VARCHAR(255) NULL,
                username VARCHAR(255) UNIQUE NOT NULL,
                phonenumber VARCHAR(255) NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                registered TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                admin BOOLEAN NOT NULL DEFAULT FALSE
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS meetups (
                id SERIAL PRIMARY KEY NOT NULL,
                topic VARCHAR(255) NOT NULL,
                description VARCHAR(255) NOT NULL,
                location VARCHAR(255) NOT NULL,
                venue VARCHAR(255) NOT NULL,
                time TIMESTAMP WITHOUT TIME ZONE,
                user_id INTEGER NOT NULL,
                happening_on TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (user_id) REFERENCES users(id)

            )
            """,

            """
            CREATE TABLE IF NOT EXISTS questions (
                id SERIAL PRIMARY KEY NOT NULL,
                topic VARCHAR(255) NULL,
                body VARCHAR(255) NOT NULL,
                upvotes INTEGER NOT NULL DEFAULT 0,
                downvotes INTEGER NOT NULL DEFAULT 0,
                meetup_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (meetup_id) REFERENCES meetups(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY NOT NULL,
                body VARCHAR(255) NULL,
                question_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (question_id) REFERENCES questions(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS sessions (
                id SERIAL PRIMARY KEY NOT NULL,
                token VARCHAR(255) NOT NULL,
                created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS rsvp (
                id SERIAL PRIMARY KEY NOT NULL,
                meetup_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                response VARCHAR(255) NULL,
                created_on TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (meetup_id) REFERENCES meetups(id)

            )
            """
        ]


class Database:

    def __init__(self, env):
        self.config_name = env
        self.config = app_config[self.config_name]
        self.db_user = self.config.DB_USER
        self.db_password = self.config.DB_PASSWORD
        self.db_host = self.config.DB_HOST
        self.db_port = self.config.DB_PORT
        self.db_name = self.config.DB_NAME

        self.connection = self.connect(self.db_user, self.db_password, self.db_host, self.db_port, self.db_name)

    def connect(self, user, password, host, port, db):
        try:
            connection = psycopg2.connect(user=user,
                                          password=password,
                                          host=host,
                                          port=port,
                                          database=db)

            return connection
        except (Exception, psycopg2.Error) as error:
            return "Error while connecting to PostgreSQL", error

    def delete_data(self):

        cursor = self.connection.cursor()
        cursor.execute('TRUNCATE TABLE ' + ','.join(tables) + ' CASCADE')
        self.connection.commit()

    def delete_table_data(self, table_name):

        cursor = self.connection.cursor()
        cursor.execute('TRUNCATE TABLE ' + table_name + ' CASCADE')
        self.connection.commit()


    def drop_tables(self):

        cursor = self.connection.cursor()
        for table in tables:
            cursor.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table))

        self.connection.commit()

    def drop_table(self, table_name):

        cursor = self.connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table_name))

        self.connection.commit()


    def create_tables(self):

        cursor = self.connection.cursor()
        for query in table_queries:
            cursor.execute(query)

        self.connection.commit()
