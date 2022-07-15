from collections import OrderedDict

from django.test import TestCase
from rest_framework import status

from tourism_backend.models import Application


# python .\manage.py test tourism_backend.tests.test_views
class ViewsTestCase(TestCase):
    # Тест по корректным входным данным
    def test_post_valid_data(self):

        # URL-пост запроса
        url = "http://127.0.0.1:8000/api/v1/application/"

        # Входные данные
        data = [
            "TestName", "88005553535",
            "TestEmail@mail.ru", "Test",
        ]

        # Отправка запроса
        response = self.client.post(
            url,
            {"name": data[0], "phone": data[1],
             "email": data[2], "comment": data[3]},
        )

        # Получения результата из БД
        application = Application.objects.filter(
            name=data[0], mobile_phone=data[1],
            email=data[2], comment=data[3],
        )[0]

        # Проверка статуса пост-запроса
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # Проверка входных и выходных данных БД через пост запрос
        self.assertEqual(
            data, [
                application.name, application.mobile_phone,
                application.email, application.comment,
            ],
        )

    # Тест по некорректным входным данным (некорректное имя)
    def test_post_not_valid_name(self):

        # URL-пост запроса
        url = "http://127.0.0.1:8000/api/v1/application/"

        # Входные данные
        data = [
            [
                "Test46Name", "TestName#",
                "Тес%тНейм", "#$%^&23",
            ],
            "88005553535", "TestEmail@mail.ru", "Test",
        ]

        # Отправка запроса
        for i in range(len(data[0])):
            response = self.client.post(
                url,
                {"name": data[0][i], "phone": data[1],
                 "email": data[2], "comment": data[3]},
            )

            # Cравнение статуса ответа
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            # Cравнение json ответа
            self.assertEqual(

                {
                    'error': 'Введите корректное имя'
                },
                response.data
            )

    # Тест по некорректным входным данным (некорректный телефон)
    def test_post_not_valid_mobile(self):

        # URL-пост запроса
        url = "http://127.0.0.1:8000/api/v1/application/"

        # Входные данные
        data = [
            "TestName",
            [
                "880055535354", "8df8d00555353dfg5",
                "8005553535", "8800555.3.535",
            ],
            "TestEmail@mail.ru", "Test",
        ]

        # Отправка запроса
        for i in range(len(data[1])):
            response = self.client.post(
                url,
                {"name": data[0], "phone": data[1][i],
                 "email": data[2], "comment": data[3]},
            )

            # Cравнение статуса ответа
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            # Cравнение json ответа
            self.assertEqual(
                {
                    'error': 'Введите корректный телефон'
                },
                response.data
            )

    # Тест по некорректным входным данным (некорректный email)
    def test_post_not_valid_email(self):

        # URL-пост запроса
        url = "http://127.0.0.1:8000/api/v1/application/"

        # Входные данные
        data = [
            "TestName", "88005553535",
            [
                "Test#Email@mail.ru", "TestEmail@mail..ru",
                "TestEmailmail.ru", "@mail.ruTestEmail",
            ],
            "Test",
        ]

        # Отправка запроса
        for i in range(len(data[2])):
            response = self.client.post(
                url,
                {"name": data[0], "phone": data[1],
                 "email": data[2][i], "comment": data[3]},
            )

            # Cравнение статуса ответа
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            # Cравнение json ответа
            self.assertEqual(
                {
                    'error': 'Введите корректный email'
                },
                response.data
            )

    # Тест гет запроса без параметров
    def test_get_without_parameters(self):

        # URL-пост запроса
        url = "http://127.0.0.1:8000/api/v1/application/"

        # Поместим данные в БД
        Application.objects.create(
            name="TestNameQ", mobile_phone="88005553535",
            email="TestEmail1@mail.ru", comment="Test1",
        )
        Application.objects.create(
            name="TestNameW", mobile_phone="88004553535",
            email="TestEmail2@mail.ru", comment="Test2",
        )
        Application.objects.create(
            name="TestNameE", mobile_phone="88004453535",
            email="TestEmail3@mail.ru", comment="Test3",
        )
        Application.objects.create(
            name="TestNameR", mobile_phone="88004443535",
            email="TestEmail4@mail.ru", comment="Test4",
        )
        # Отправка запроса
        response = self.client.get(url)

        # Проверка статуса гет-запроса
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # Дату учитывать не будем
        result = response.data
        for i in range(len(result)):
            result[i].pop("date")

        # Проверка данных гет запроса
        self.assertEqual(
            [
                OrderedDict(
                    [('id', 1), ('name', 'TestNameQ'), ('mobile_phone', '88005553535'), ('email', 'TestEmail1@mail.ru'),
                     ('comment', 'Test1')]),
                OrderedDict(
                    [('id', 2), ('name', 'TestNameW'), ('mobile_phone', '88004553535'), ('email', 'TestEmail2@mail.ru'),
                     ('comment', 'Test2')]),
                OrderedDict(
                    [('id', 3), ('name', 'TestNameE'), ('mobile_phone', '88004453535'), ('email', 'TestEmail3@mail.ru'),
                     ('comment', 'Test3')]),
                OrderedDict(
                    [('id', 4), ('name', 'TestNameR'), ('mobile_phone', '88004443535'), ('email', 'TestEmail4@mail.ru'),
                     ('comment', 'Test4')]),
            ], result
        )

    # Тест гет запроса с параметром
    def test_get_with_parameters(self):
        param = 4
        # URL-пост запроса
        url = f"http://127.0.0.1:8000/api/v1/application/?id={param}"

        # Поместим данные в БД
        Application.objects.create(
            name="TestNameQ", mobile_phone="88005553535",
            email="TestEmail1@mail.ru", comment="Test1",
        )
        Application.objects.create(
            name="TestNameW", mobile_phone="88004553535",
            email="TestEmail2@mail.ru", comment="Test2",
        )
        Application.objects.create(
            name="TestNameE", mobile_phone="88004453535",
            email="TestEmail3@mail.ru", comment="Test3",
        )
        Application.objects.create(
            name="TestNameR", mobile_phone="88004443535",
            email="TestEmail4@mail.ru", comment="Test4",
        )
        # Отправка запроса
        response = self.client.get(url)

        # Проверка статуса гет-запроса
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

        # Дату учитывать не будем
        result = response.data
        for i in range(len(result)):
            result[i].pop("date")

        # Проверка данных гет запроса
        self.assertEqual(
            [
                OrderedDict(
                    [('id', 4), ('name', 'TestNameR'), ('mobile_phone', '88004443535'), ('email', 'TestEmail4@mail.ru'),
                     ('comment', 'Test4')]),
            ], result
        )
