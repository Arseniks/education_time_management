# education_time_management


## Копирование проекта
- Клонируйте проект с GitHub с помощью команды:
```
git clone https://github.com/Arseniks/education_time_management
```
- Перейдите в папку с проектом:
```
cd education_time_management
```
## Запуск приложения

Для запуска всего приложение нужно запустить файл /education_time_management/app/__main__.py, 
при этом добавив в командную строку при необходимости:

    education_time_management [-h] [--db_connection_uri DB_CONNECTION_URI] [--port PORT] [--reload RELOAD]
 
    опицональные аргументы:
      -h, --help            вывести вспомогательное сообщение и выйти
      --db_connection_uri   DB_CONNECTION_URI полный URI для 
                            бд PostgreSQL [по умолчанию: postgresql://user:password@host:port/database_name]
      --port PORT           привязать сокет к этому порту [по умолчанию: 5001]
      --reload RELOAD       включение авто-перезапуска


