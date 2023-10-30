import psycopg2


class DBManager:
    """
    Класс для работы с базой данных
    """

    def __init__(self, database_name: str, params: dict):
        self.name = database_name
        self.params = params
        self.create_database()

    def create_database(self):
        """
        метод для создания базы данных
        :return: None
        """
        conn = psycopg2.connect(**self.params)
        conn.autocommit = True
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE IF EXISTS {self.name}")
        cur.execute(f'CREATE DATABASE {self.name}')

        conn.close()

        self.params.update({'dbname': self.name})