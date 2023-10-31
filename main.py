from src.hh_api import HeadHunterAPI
from src.db_manager import DBManager
from src.utils import load_companies, config
from src.vacancy import Vacancy


def main():

    database_name = 'base'  # изменить название при повторном запуске
    file_companies_ids = 'data/companies.json'

    # подгрузка компаний из файла
    companies = load_companies(file_companies_ids)

    # загрузка параметров из database.ini
    params = config()

    # создание БД
    db_manager = DBManager(database_name, params)
    print(f'База SQL {db_manager.name} создана')
    print(f"Подождите! Идет загрузка в базу данных SQL...")

    # API менеджер
    hh_api = HeadHunterAPI()

    for company in companies:
        # инфо о компании по айди
        vacancies_info = hh_api.get_all_vacancies(company['id'])

        # отпарвление инфо о компании в БД
        db_manager.insert_data_company(vacancies_info[0])

        # Список вакансий
        vacancies = []
        for vacancy_info in vacancies_info:
            vacancy = Vacancy.create_vacancy_from_hh(vacancy_info)
            vacancies.append(vacancy)

        # пушим вакансии в БД
        db_manager.insert_data_vacancy(vacancies)

    print('Данные по вакансиям выбранных работодателей добавлены в базу данных SQL')

    while True:

        print('''
Добрый день!
Выберите один из пунктов
1 - получить список всех компаний и количество вакансий у каждой компании
2 - получить список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
3 - получить среднюю зарплату по вакансиям
4 - получить список всех вакансий, у которых зарплата выше средней по всем вакансиям
5 - получить список всех вакансий, в названии которых содержится слово python
0 - выход''')

        user_input = input()
        if user_input == "1":
            db_manager.get_companies_and_vacancies_count()
        elif user_input == "2":
            db_manager.get_all_vacancies()
        elif user_input == "3":
            db_manager.get_avg_salary()
        elif user_input == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif user_input == "5":
            db_manager.get_vacancies_with_keyword('python')
        elif user_input == "0":
            break
        else:
            print('Неверная команда')


if __name__ == "__main__":
    main()
