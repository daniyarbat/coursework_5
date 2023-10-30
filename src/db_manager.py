import psycopg2


class DBManager:
    """
    Класс для работы с базой данных
    """

    def __init__(self, database_name: str, params: dict):
        self.name = database_name
        self.params = params
        self.create_database()
        self.create_table_companies()

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

    def create_table_companies(self):
        """
        метод, добавляющий таблицу компаний
        :return:
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE companies (
            company_id_hh integer PRIMARY KEY,
            company_name varchar(150),
            employer_url varchar(150)
        )''')
        conn.commit()

        cur.close()
        conn.close()

    def create_table_vacancies(self):
        """
        метод, добавляющий таблицу вакансий
        :return:
        """
        conn = psycopg2.connect(**self.params)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE vacancies (
            vacancy_id_hh integer PRIMARY KEY,
            company_id_hh integer,
            vacancy_name varchar(150),
            data_published date,
            salary_average integer,
            area varchar(150),
            url varchar(150),
            requirement varchar(500),
            experience varchar(150),
            employment varchar(150),

            CONSTRAINT fk_hh_vacancies_vacancies FOREIGN KEY(company_id_hh) REFERENCES companies(company_id_hh)
        )''')
        conn.commit()

        cur.close()
        conn.close()
