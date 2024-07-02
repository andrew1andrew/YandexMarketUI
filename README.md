<a name="Установка и запуск"><h2>Установка и запуск:</h2></a>

<a name="Шаг 1: Клонирование репозитория"><h2>Шаг 1: Клонирование репозитория</h2></a>
```bash
git clone https://github.com/andrew1andrew/YandexMarketUI.git

cd <укажите путь к проекту>
```

\
<a name="Шаг 2: Создание виртуального окружения и установка зависимостей"><h2>Шаг 2: Создание виртуального окружения и установка зависимостей</h2></a>
```
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

\
<a name="Шаг 3: Запуск теста"><h2>Шаг 3: Запуск теста</h2></a>
```
python -m pytest -v test_market.py
```


