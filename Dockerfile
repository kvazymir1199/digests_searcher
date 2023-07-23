FROM python:3.10.9-slim
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r /app/requirements.txt
COPY . .

CMD ["gunicorn", "digest_project.wsgi:application", "--bind", "0:8000" ]