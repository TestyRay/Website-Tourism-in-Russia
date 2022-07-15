## Вебсайт: Туризм в России

### Установка и запуск Backend:

**Установка нужных библиотек и компонентов:**

```
pip install -r req.txt
```

**Проведение миграций модели БД:**

```
python manage.py makemigrations
```

```
python manage.py migrate
```

**Создание суперпользователя (для разработчиков/владельцев):**

```
python manage.py createsuperuser
```

**Запуск сервера:**

```
python manage.py runserver
```

**Команды тестирования БД и API:**

```
python .\manage.py test tourism_backend.tests.test_model
```

```
python .\manage.py test tourism_backend.tests.test_views
```

### Установка и запуск Frontend (при наличии node js на устройстве):

**Установка нужных библиотек и компонентов:**

```
npm install
```

**Запуск сервера:**

```
npm run dev
```
