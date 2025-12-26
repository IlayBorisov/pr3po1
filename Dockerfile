FROM python:3.9-slim

WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код
COPY mortgage_calculator.py .

# Создаем пользователя без привилегий
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Запускаем приложение
CMD ["python", "mortgage_calculator.py"]