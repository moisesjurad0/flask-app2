FROM python:3.10

EXPOSE 5000
# EXPOSE 80
# EXPOSE 443

WORKDIR /myapp

COPY . .

RUN pip install -r requirements.txt

# CMD ["python", "app.py"]
# CMD flask run --debug
CMD flask run --host=0.0.0.0