FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . /app/

# Собираем статические файлы
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:8000", "task_manager.wsgi:application"]
