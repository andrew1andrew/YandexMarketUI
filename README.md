<a name="Установка и запуск"><h2>Установка и запуск:</h2></a>\
Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/andrew1andrew/YandexMarketUI.git

cd <укажите путь к проекту>
```

\
Шаг 2: Создание виртуального окружения и установка зависимостей
```
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

\
Шаг 3: Запуск теста
```
python -m pytest -v test_market.py
```


