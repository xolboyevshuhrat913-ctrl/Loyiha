FROM python:3.13-alpine

WORKDIR /site

COPY . .   
EXPOSE 8001

# CD shu orqali konteyner tayyor bo'lganini biladi
HEALTHCHECK --interval=5s --timeout=3s --start-period=5s --retries=3 \
  CMD wget -qO- http://127.0.0.1:8001/ >/dev/null || exit 1

CMD ["python", "-m", "http.server", "8001", "--bind", "0.0.0.0"]