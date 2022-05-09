FROM python:3.9.0

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# arguments are sender address, receive address, password
CMD ["python3", "app.py", "", "", ""]
