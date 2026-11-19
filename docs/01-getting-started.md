# Работа с `Doker`

> Создание и запуск Docker-контейнера.
```bash
docker build -t superlists2 . && docker run  -p 8888:8888  --mount type=bind,source="$PWD/src/db.sqlite3",target=/src/db.sqlite3  -it superlists2
```

> Команда для запуска тестового сервера

```bash
TEST_SERVER=localhost:8888 ./src/manage.py test src/functional_tests --failfast
```

## Команды для работы внутри Docker-контейнера

```bash
docker exec -it container-id-or-name bash
# для установки curl
root@5ed84681fdf8:/src# apt-get update && apt-get install -y curl

root@5ed84681fdf8:/src# curl -iv http://localhost:8888
```