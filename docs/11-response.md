from django.http import HttpResponse

# 1. Самые частые типы ответов в Django

---
## 📄 HTML-страница (Обычный сайт)
> Когда нужно отрендерить красивую веб-страницу, используется функция-помощник `render()`.
> Она берет HTML-шаблон, подставляет туда переменные и **автоматически оборачивает результат в `HttpResponse`** со статус-кодом `200 OK`

```python
# views.py
from django.shortcuts import render

def home_page(request):
    context = {"username": request.user.username}
    # render() сам собирает и возвращает полноценный HttpResponse
    return render(request, "index.html", context)
```

## ⚙️ JSON-данные (Для API, фронтенда на React/Vue или AJAX)
> Если сайт общается с фронтендом без перезагрузки страниц, то нужно возвращать структурированные данные.
> Для этого есть **`JsonResponse`**. Он автоматически превращает Python-словарь в JSON-строку и выставляет правильный заголовок `Content-Type: application/json`.

```python
# views.py
from django.http import JsonResponse

def api_status(request):
    data = {
        "status": "success",
        "items_count": 25
    }
    return JsonResponse(data) # Вернет браузеру JSON со статус-кодом 200
```

## ↪️ Перенаправление (Редирект)
> Часто после того, как пользователь заполнил форму или нажал "выйти", его нужно отправить на другую страницу.
> Для этого используется **`HttpResponseRedirect`** (или сокращенно `redirect()`). Он возвращает статус-код **`302`**, заставляя браузер сменить `URL`.

```python
# views.py
from django.shortcuts import redirect

def logout_view(request):
    # Логика выхода из системы...
    return redirect("/login/") # Перенаправляем на страницу входа
```

# 2. Управление статус-кодами и ошибками
> Иногда нужно явно сказать браузеру, что что-то пошло не так. 
> Для этого можно передать параметр `status` в любой ответ:

```python
# views.py
from django.http import HttpResponse

def delete_article(request, id):
    if not request.user.is_staff:
        # возвращаем пустой ответ со статус-кодом 403 (Доступ запрещен)
        return HttpResponse("У вас нет прав", status=403)
    # логика удаления
    return HttpResponse("Успешно удалено", status=200)
```
> В Django также есть встроенные готовые сокращения для популярных ошибок:
> * `HttpResponseNotFound("Текст")` - вернет со статус **404** (Не найдено).
> * `HttpResponseBadRequest()` - вернет статус **400** (Плохой запрос).
> * `HttpResponseForbidden()` - вернет статус **403** (Запрещено).

# 3. Как управлять заголовками ответов (Headers) и Куками
> Объект ответа можно наполнять кастомными заголовками и куками до того, как совершить `return`.
> Сам объект `response` ведет себя внутри функции как словарь Python.

> **Добавление кастомного HTTP-заголовка:**

```python
# views.py
def my_secret_view(request):
    response = HttpResponse("Секретные данные")
    # Добавляем кастомный заголовок, который увидит браузер в Network DevTools
    response["X-Developer-Name"] = "Neko"
    return response
```

> **Установка Cookies (Кук) в браузере пользователя:**

```python
# views.py
def set_theme_view(request):
    response = HttpResponse("Тема переключена")
    # Записываем в куки браузера пользователя ключ 'theme' со значением 'dark'
    # max_age=3600 означает, что кука удалится ровно через 1 час (3600 секунд)
    response.set_cookie("theme", "dark", max_age=3600)
    return response
```