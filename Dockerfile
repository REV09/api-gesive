From python:3.10.9

WORKDIR /app
copy  ./requeriments.txt .

RUN pip3 install -r requeriments.txt

COPY . .

EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]