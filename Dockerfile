From python:3.10.9
RUN pip3 install fastapi uvicorn SQLAlchemy PyMySQL pycodestyle
copy app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]