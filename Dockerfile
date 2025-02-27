FROM python:3.9-slim

WORKDIR /app

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"

COPY pyproject.toml .
RUN uv sync

COPY . .
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "-w", "5", "-b", "0.0.0.0:8000", "task_manager.wsgi:application"]
