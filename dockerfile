FROM python:3.9-slim

WORKDIR /Activida1Scraping

COPY setup.py .

RUN pip install -e .

CMD [ "python", "setup.py" ]