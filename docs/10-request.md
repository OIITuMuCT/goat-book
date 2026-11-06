# Объект `request` in Django 
## 1. Данные от пользователя (GET and POST)
> !!! note
> 
> Это то, как мы забираем данные, которые ввел или отправил пользователь

- `request.GET` - словарь со всеми параметрами из URL-строки (после знака ?).
    * Пример URL: `/search/?q=python&page=2`
    * К коде: query = request.GET.get('q') (получим `'python'`)
- `request.POST` - словарь с данными, отправленными через HTML-форму (методом `POST`)
    * В коде: `username = request.POST.get('username')`
- `request.body` - сырые (raw) данные запроса в виде байта. Используется, если вам прислали JSON (например, в API)
    * В коде: `data = json.loads(request.body)`

## 2. Кто делает запрос? (Пользователь и Сессия)
> Django автоматически распознает пользователя благодаря встроенным Middleware.

- `request.user` - объект текущего пользователя.
    * Если пользователь вошел на сайт: это объект модели `User`. Можно проверить: `request.user.email` или `request.user.is_staff`
    * Если гость (не авторизован): это объект `AnonymousUser`. Чтобы проверить, залогинен ли человек, используют `if request.user.is_authenticated:`
- `request.session` - словарь сессии. Позволяет хранить данные о пользователе между запросами (например `id` товаров в корзине неавторизованного юзера).
    * В коде: `request.session['catr_count'] = 5`

## 3. Метаданные (Метод, IP, Заголовки)
> Информация о том, как и откуда пришел запрос.
- `request.method` - строка, указывающая на HTTP-метод. Всегда пишется капсом ('GET', 'POST', 'PUT', 'DELETE').
    * В коде: `if request.method == 'POST':` (используется для разделения логики показа формы и ее сохранения).
- `request.META` - огромный словарь со всеми заголовками и системными переменными сервера. Отсюда берут IP-адрес и тип браузера:
    * IP-адрес: `ip = request.META.get('REMOTE_ADDR')`
    * Браузер (User-Agent): `browser = request.META.get('HTTP_USER_AGENT')`
- `request.headers` - более удобный и современный способ читать HTTP-заголовки (появился в Django 3.x).
    * В коде: `auth_token = request.headers.get('Authentication')`

## 4. Файлы и Куки.

- `request.FILES` - словарь со всеми загруженными файлами (картинки, документы), которые пользователь прикрепил к форме (`<input type="file">`). 
    * В коде: `avatar = request.FILES.get('avatar')`
- `request.COOKIES` - словарь со всеми куками браузера.
    * В коде: `theme = request.COOKIES.get('theme_color')`

## 🛠️ Живой пример: всё в одном месте
> Вот как выглядит типичная View-функция, 
> которая использует возможности request по максимуму:

```python
# views.py
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def FeedbackView(request):
    # 1. Передаем метод запроса
    if request.method == "POST":
        # 2. Проверяем, авторизован ли пользователь
        if not request.user.is_authenticated:
            return HttpResponse("Только для зарегистрированных пользователей", status=403)
        
        # 3. Вытаскиваем данные из формы и файл
        user_text = request.POST.get('message')
        uploaded_file = request.FILES.get('screenshot')

        # 4. Логируем IP-адрес того, кто отправил
        user_ip = request.META.get('REMOTE_ADDR')
        print(f"Пользователь {request.user.username} (IP: {user_ip}) отправил сообщение.")

        # Какая-то логика сохранения...
        return HttpResponse("Спасибо за отзыв!")
    
    # Если это обычный GET-запрос, просто показываем страницу с формой
    return render(request, 'feedback.html')
```