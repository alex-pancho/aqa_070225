FROM python:3.11-slim

# Встановлюємо робочий каталог
WORKDIR /app

# Копіюємо requirements.txt у контейнер
COPY requirements.txt .

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту файлів (код, тести, модулі)
COPY . .

# Встановлюємо команду за замовчуванням (запуск тестів)
CMD ["pytest", "-v", "lesson_29_homework/tests/"]