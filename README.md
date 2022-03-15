## Учебный проект "CRUD для Yatube"

Реализовано API для всех моделей Yatube приложения posts.
API доступен только аутентифицированным пользователям. Использована аутентификация по токену TokenAuthentication.
Аутентифицированный пользователь авторизован на изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения. При попытке изменить чужие данные - возвращаться код ответа 403 Forbidden.

Проект реализован на Django REST Framework.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Marikalis/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Документация к API:

```
http://127.0.0.1:8000/redoc/
```

Регистрация нового пользователя:

```
http://127.0.0.1:8000/api/v1/users/
```
