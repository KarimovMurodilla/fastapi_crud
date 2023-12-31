# О проекте
Простая API для CRUD запросов на [FastAPI](https://github.com/tiangolo/fastapi).
В этом проекте использован паттерн [Unit of work](https://en.wikipedia.org/wiki/Unit_of_work)

## Запуск приложения

### С помощью docker-compose 
```
docker-compose up --build
```
> Откройте в: [0.0.0.0:9999](http://0.0.0.0:9999)

### С помощью python
1. Установка модулей
```
pip install -r requirements.txt
```
2. Миграции
```
alembic revision --autogenerate --m="Initial check"
```
```
alembic upgrade head
```

3. Запуск (в корневом каталоге)
```
python src/main.py
```
> Откройте в: [localhost:8000](http://localhost:8000)


## Запуск тестов
Для тестов использовал [Pytest](https://pypi.org/project/pytest/)
1. Запуск тестов (в корневом каталоге)
```
pytest -v tests/
```

