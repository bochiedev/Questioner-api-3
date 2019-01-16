import psycopg2

tables = [
            'users',
            'meetups',
            'questions',
            'comments'
        ]

table_queries = [
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY NOT NULL,
                firstname VARCHAR(250) NOT NULL,
                lastname VARCHAR(250) NOT NULL,
                othername VARCHAR(250) NULL,
                username VARCHAR(250) NOT NULL,
                phonenumber VARCHAR(250) NULL,
                email VARCHAR(250) NOT NULL,
                password VARCHAR(250) NOT NULL,
                registered TIMESTAMP WITHOUT TIME ZONE \
                DEFAULT (NOW() AT TIME ZONE 'utc'),
                admin BOOLEAN NOT NULL DEFAULT FALSE
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS meetups (
                id SERIAL PRIMARY KEY NOT NULL,
                topic VARCHAR(250) NOT NULL,
                description VARCHAR(250) NOT NULL,
                location VARCHAR(250) NOT NULL,
                venue VARCHAR(250) NOT NULL,
                time TIMESTAMP WITHOUT TIME ZONE,
                user_id INTEGER NOT NULL,
                happening_on TIMESTAMP WITHOUT TIME ZONE \
                DEFAULT (NOW() AT TIME ZONE 'utc'),
                created_at TIMESTAMP WITHOUT TIME ZONE \
                DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (user_id) REFERENCES users(id)

            )
            """,

            """
            CREATE TABLE IF NOT EXISTS questions (
                id SERIAL PRIMARY KEY NOT NULL,
                topic VARCHAR(250) NULL,
                body VARCHAR(250) NOT NULL,
                upvotes INTEGER NOT NULL DEFAULT 0,
                downvotes INTEGER NOT NULL DEFAULT 0,
                meetup_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE \
                DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (meetup_id) REFERENCES meetups(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """,

            """
            CREATE TABLE IF NOT EXISTS comments (
                id SERIAL PRIMARY KEY NOT NULL,
                body VARCHAR(250) NULL,
                question_id INTEGER NOT NULL,
                user_id INTEGER NOT NULL,
                created_at TIMESTAMP WITHOUT TIME ZONE \
                DEFAULT (NOW() AT TIME ZONE 'utc'),
                FOREIGN KEY (question_id) REFERENCES questions(id),
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
            """
        ]


class Database:
    def __init__(self):
        pass

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
        connection = self.connect("bochie","jamohsize","127.0.0.1","5432","questioner")

        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE ' + ','.join(tables) + ' CASCADE')
        connection.commit()

    def delete_table_data(self, table_name):
        connection = self.connect("bochie","jamohsize","127.0.0.1","5432","questioner")

        cursor = connection.cursor()
        cursor.execute('TRUNCATE TABLE ' + table_name + ' CASCADE')
        connection.commit()


    def drop_tables(self):
        connection = self.connect("bochie","jamohsize","127.0.0.1","5432","questioner")

        cursor = connection.cursor()
        for table in tables:
            cursor.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table))

        connection.commit()

    def drop_table(self, table_name):
        connection = self.connect("bochie","jamohsize","127.0.0.1","5432","questioner")

        cursor = connection.cursor()

        cursor.execute('DROP TABLE IF EXISTS {} CASCADE'.format(table_name))

        connection.commit()


    def create_tables(self):
        connection = self.connect("bochie","jamohsize","127.0.0.1","5432","questioner")

        cursor = connection.cursor()
        for query in table_queries:
            cursor.execute(query)

        connection.commit()
