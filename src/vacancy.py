import datetime


class Vacancy:
    """
    Добавление класса вакансии
    """

    def __init__(self, vacancy_information: dict):
        self.id = vacancy_information["id"]
        self.type = vacancy_information["type"]
        self.name = vacancy_information["name"]
        self.data_published = vacancy_information["data_published"]
        self.salary_from = vacancy_information["salary_from"]
        self.salary_to = vacancy_information["salary_to"]
        self.currency = vacancy_information["currency"]
        self.area = vacancy_information["area"]
        self.url = vacancy_information["url"]
        self.employer = vacancy_information["employer"]
        self.employer_id = vacancy_information["employer_id"]
        self.employer_url = vacancy_information["employer_url"]
        self.requirement = vacancy_information["requirement"]
        self.experience = vacancy_information["experience"]
        self.employment = vacancy_information["employment"]
        self.salary_average = self.salary_average()

    def __str__(self):
        if self.requirement is None:
            requirement = None
        else:
            requirement = self.requirement[:200]
        return f'''Vacancy - {self.name}
                   Type - {self.type}
                   Data published - {datetime.datetime.fromtimestamp(self.data_published).strftime('%Y-%m-%d %H:%M:%S')}
                   Employer - {self.employer}
                   Salary - {self.salary_from} - {self.salary_to}
                   Requirement - {requirement}...
                   Experience - {self.experience}
                   Employment - {self.employment}
                   Area - {self.area}
                   Url - {self.url}
                '''

    def salary_average(self):
        """
        Получает среднюю зарплату
        :return: average salary
        """
        if self.salary_from:
            if self.salary_to:
                result = int((self.salary_to + self.salary_from) / 2)
            else:
                result = self.salary_from
        else:
            if self.salary_to:
                result = self.salary_to
            else:
                result = 0

        return result

    @classmethod
    def create_vacancy_from_hh(cls, vacancy_info_hh: dict):
        """
        Классметод конвертирует информацию о вакансии из hh и создает обьект Вакансии
        :param vacancy_info_hh: dict with information about vacancy
        :return: object Vacancy
        """
        result = {
            "id": cls.check_for_availability(vacancy_info_hh, "id"),
            "website": 'HeadHunter',
            "type": cls.check_for_availability(vacancy_info_hh, "type", "name"),
            "name": cls.check_for_availability(vacancy_info_hh, "name"),
            "data_published": cls.check_for_availability(vacancy_info_hh, "published_at"),
            "salary_from": cls.check_for_availability(vacancy_info_hh, "salary", "from"),
            "salary_to": cls.check_for_availability(vacancy_info_hh, "salary", "to"),
            "currency": cls.check_for_availability(vacancy_info_hh, "salary", "currency"),
            "area": cls.check_for_availability(vacancy_info_hh, "area", "name"),
            "url": cls.check_for_availability(vacancy_info_hh, "alternate_url"),
            "employer": cls.check_for_availability(vacancy_info_hh, "employer", "name"),
            "employer_id": cls.check_for_availability(vacancy_info_hh, "employer", "id"),
            "employer_url": cls.check_for_availability(vacancy_info_hh, "employer", "alternate_url"),
            "requirement": cls.check_for_availability(vacancy_info_hh, "snippet", "requirement"),
            "experience": cls.check_for_availability(vacancy_info_hh, "experience", "name"),
            "employment": cls.check_for_availability(vacancy_info_hh, "employment", "name")
        }
        return Vacancy(result)
