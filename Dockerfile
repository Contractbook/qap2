FROM python:3.10-alpine3.17
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /code
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--workers", "1"]