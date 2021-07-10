FROM python:3.8-slim-buster

RUN python3 -m venv /opt/venv

COPY . .
RUN /opt/venv/bin/pip install -r requirements.txt

CMD ["/opt/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

