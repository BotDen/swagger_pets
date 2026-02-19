from faker import Faker


class Fake:
    """Класс по генерации тестовых данных"""

    def __init__(self, faker: Faker):
        self.faker = faker

    def get_id(self) -> int:
        """
        Метод по генерации id
        :return: Возвращает id
        """
        return self.get_random_int()

    def get_user_name(self) -> str:
        """
        Метод по генерации user name
        :return: Возвращает user name
        """
        return self.faker.user_name()

    def get_first_name(self) -> str:
        """
        Метод по генерации first name
        :return: Возвращает first name
        """
        return self.faker.first_name()

    def get_last_name(self) -> str:
        """
        Метод по генерации last name
        :return: Возвращает last name
        """
        return self.faker.last_name()

    def get_email(self, domain: str | None = None) -> str:
        """
        Метод по генерации email
        :param domain: Если домен не передан, то будет подставлено домен по умолчанию. Пример домена "gmail.com"
        :return: Возвращает адрес электронной почты
        """
        return self.faker.email(domain=domain)

    def get_password(self) -> str:
        """
        Метод по генерации password
        :return: Возвращает password
        """
        return self.faker.password()

    def get_phone_number(self) -> str:
        """
        Метод по генерации phone number
        :return: Возвращает phone number
        """
        return self.faker.phone_number()

    def get_random_int(self) -> int:
        """
        Метод по генерации случайного числа int
        :return: Возвращает случайное число int
        """
        return self.faker.random_int()


fake = Fake(faker=Faker("ru-RU"))
