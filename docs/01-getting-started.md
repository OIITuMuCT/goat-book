# Работа с `Doker`

> Создание и запуск Docker-контейнера.
```bash
docker build -t superlists2 . && docker run  -p 8888:8888  --mount type=bind,source="$PWD/src/db.sqlite3",target=/src/db.sqlite3  -it superlists2
```

> Команда для запуска тестового сервера
> 
```bash
TEST_SERVER=localhost:8888 ./src/manage.py test src/functional_tests --failfast
```