#Dockerfile, Image, Container
FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# run docker with docker run -it -p 8000:8000 --name=xxxx ur images