FROM python:3.9-slim
COPY pruebadocker.py .
CMD [ "python", "pruebadocker.py" ]