# Миграции
Для накатывания миграций, если нет файла alembic.ini, запусти в терминале команду:
```commandline
alembic init migrations
```

После этого будет создана папка с миграциями и конфигурационный файл для alembic.

- В alembic.ini нужно задать адрес базы данных, в которую будут добавлены миграции.
- Дальше идем в папку с миграциями и открываем env.py, там вносим измениния в блок, где написано
```commandline
from myapp import mymodel
```
- Вводим ```alembic revision --autogenerate -m "comment"```
- Создается миграция
- Вводим ```alembic upgrade heads```