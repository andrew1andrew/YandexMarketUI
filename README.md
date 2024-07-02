## Установка и запуск

### Шаг 1: Клонирование репозитория
```bash
git clone https://github.com/andrew1andrew/YandexMarketUI.git
cd <укажите путь к проекту>

### Шаг 2: Создание виртуального окружения и установка зависимостей
python -m venv venv
venv\Scripts\activate  # для Windows
pip install -r requirements.txt

###Шаг 3: Запуск теста
python -m pytest -v test_market.py
