from django.db import models

class Application(models.Model):
    name = models.TextField("Имя")
    mobile_phone = models.TextField("Телефон")
    email = models.TextField("email")
    comment = models.TextField("Комментарий")
    date = models.DateTimeField("Дата", auto_now=True)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"


