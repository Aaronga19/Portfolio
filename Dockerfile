FROM python:3.7.9

WORKDIR /code

#ENV

#ENV

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt 

RUN pip install -r requirements.txt

COPY . . 

CMD ["python", "manage.py", "runserver"]