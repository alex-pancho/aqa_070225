FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY lesson_30/HW_30.py .

CMD ["pytest", "-v", "HW_30.py"]