FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /api

COPY requirements.txt /api

WORKDIR /api

RUN pip install -r requirements.txt

COPY . /api

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
