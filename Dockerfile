FROM python:3.13-alpine

WORKDIR /site

COPY . .

EXPOSE 8001

CMD ["python", "-m", "http.server", "8001", "--bind", "0.0.0.0"]