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
