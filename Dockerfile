FROM python:3.10.4-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
ENV PORT=8000
EXPOSE 8000
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD python ./manage.py runserver 0.0.0.0:$PORT