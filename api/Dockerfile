FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /churnprediction

COPY requirements.txt /churnprediction

WORKDIR /churnprediction

RUN pip install -r requirements.txt

COPY . /churnprediction

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
