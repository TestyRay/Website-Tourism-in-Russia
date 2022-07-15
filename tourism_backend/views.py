import re

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Application
from .serializers import ApplicationSerializers


class APIApplication(APIView):
    @staticmethod
    def get(request):
        application = Application.objects.all()
        application_serializer = ApplicationSerializers(application, many=True).data

        if application:
            apl_id = request.GET.get("id")
            if apl_id:
                application = Application.objects.filter(id=apl_id)
                application_serializer = ApplicationSerializers(application, many=True).data
                if application:
                    return Response(application_serializer, status=201)
                return Response([{"В базе данных нет такого id"}], status=201)
            return Response(application_serializer, status=201)
        return Response([{"В базе данных ещё нет заявок"}], status=201)

    @staticmethod
    def post(request):

        name = request.data.get("name")
        phone = request.data.get("phone")
        email = request.data.get("email")
        comment = request.data.get("comment")

        valid_name = re.compile(r'^[a-zA-Zа-яёА-ЯЁ]+$')
        valid_phone = re.compile(r'(\+7|7|8)\D*\d{3}\D*\d{3}\D*\d{2}\D*\d{2}')
        valid_email = re.compile(r'([A-Za-z\d]+[.-_])*[A-Za-z\d]+@[A-Za-z\d-]+(\.[A-Z|a-z]{2,})+')

        if name:
            if re.fullmatch(valid_name, name):
                if phone:
                    if re.fullmatch(valid_phone, phone):
                        if email:
                            if re.fullmatch(valid_email, email):
                                if comment:
                                    application = Application.objects.create(name=name, mobile_phone=phone, email=email, comment=comment)
                                    application.save()
                                    return Response({"data": "Заявка успешно отправлена"}, status=201)
                                return Response({"error": 'Введите данные в поле \'Комментарий\''}, status=400)
                            return Response({"error": 'Введите корректный email'}, status=400)
                        return Response({"error": 'Введите данные в поле \'Email\''}, status=400)
                    return Response({"error": 'Введите корректный телефон'}, status=400)
                return Response({"error": 'Введите данные в поле \'Телефон\''}, status=400)
            return Response({"error": 'Введите корректное имя'}, status=400)
        return Response({"error": "Введите данные в поле \'Имя\'"}, status=400)
