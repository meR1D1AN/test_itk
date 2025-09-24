# Тестовое задание для бэкенд разработчика на Python в ITK academy. 
- Реализовать API используя FastAPI и Pydantic - с этим знаком очень слабо, `Лиана` сказала, что можно сделать на DRF, что я и сделал.

## Используемый стек:
- uv
- Python - 3.13
- DRF - 3.16.1
- Psycopg2-binary - 2.9.10
- Gunicorn - 23.0
- DRF-spectacular - 0.28
- Django-filter - 25.1
- Faker - 37.6 
- tqdm - 4.67.1
- pre-commit (линтер ruff)
- docker
---
## Запуск проекта с помощью Docker
1. Склонируйте репозиторий:
```bash
git clone https://github.com/meR1D1AN/test_itk.git
cd test_itk
```
2. Скопируйте файл `.env.sample` и внесите изменения в файл `.env`:
```bash
cp .env.sample .env
```
3. Проверьте, что программа Docker Desktop установлена и запущена, и введите команду:
```bash
docker compose up -d --build
```
4. При запуске контейнера в базе будет создан админ, можно будет перейти в админку Django, используя ADMIN_USERNAME и ADMIN_PASSWORD внесённые в файле `.env` и 10000 рандомных задач.
  
**Команда без передачи аргумента создаёт 10000 задач**
```bash
docker compose exec app uv run python3 manage.py create_test_data
```
**Команда с передачей аргумента создаст к примеру 12345 задач**
```bash
docker compose exec app uv run python3 manage.py create_test_data --count 12345        
```
5. Ссылка на [Админку](http://localhost/admin).
6. Сслыка на [Swagger](http://localhost/api/v1/docs) документацию.

---
### Ендпоинты
- Ручка GET на получение всех задач с фильтрацией по полям, и пагинацией ![img.png](image_for_readme/img.png)
* пример успешного получения списка всех задач ![img_1.png](image_for_readme/img_1.png)

- Ручка POST на создание задачи ![img_4.png](image_for_readme/img_4.png)
* пример успешного создания задачи, с возможными ошибками ![img_3.png](image_for_readme/img_3.png)

- Ручка GET id на получение детальной информации о задаче, необходимо передать ID задачи ![img_5.png](image_for_readme/img_5.png)
* пример успешного получение детальной информации о задаче, с возможными ошибками ![img_6.png](image_for_readme/img_6.png)

- Ручка PUT id полное обновление задачи, необходимо передать ID задачи ![img_7.png](image_for_readme/img_7.png)
* пример успешного полного обновления задачи, с возможными ошибками ![img_8.png](image_for_readme/img_8.png)

- Ручка PATCH id частичное обновление задачи, необходимо передать ID задачи ![img_9.png](image_for_readme/img_9.png)
* пример успешного частичного обновления задачи, с возможными ошибками ![img_10.png](image_for_readme/img_10.png)

- Ручка DELETE id удаление задачи, необходимо передать ID задачи ![img_11.png](image_for_readme/img_11.png)
* пример успешного удаления задачи, с возможными ошибками ![img_12.png](image_for_readme/img_12.png)
