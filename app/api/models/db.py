import psycopg2


class Database:

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

    def create_tables(self):
        pass
