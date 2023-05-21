From python:3.10.9

copy ./ /app/src
copy  ./requeriments.txt /app
WORKDIR /app

RUN pip3 install -r requeriments.txt

EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]