from django.test import TestCase

from tourism_backend.models import Application
from datetime import datetime, timezone


# python .\manage.py test tourism_backend.tests.test_model
class ModelTestCase(TestCase):

    def test_creating_db_data(self):
        # Входные данные
        data = [
            "TestName", "88005553535",
            "TestEmail@mail.ru", "Test",
            datetime.now(timezone.utc).replace(
                microsecond=0,
            ),  # Допустимы погрешности в microsecond, поэтому не будем их учитывать, заменим на 0
        ]

        # Создаём объект БД
        application = Application.objects.create(
            name=data[0], mobile_phone=data[1],
            email=data[2], comment=data[3],
        )

        # Проверка входных и выходных данных БД
        self.assertEqual(
            data, [
                application.name, application.mobile_phone,
                application.email, application.comment,
                application.date.replace(
                    microsecond=0,
                ),
            ],
        )