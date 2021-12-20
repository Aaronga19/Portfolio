
FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN mkdir /Portfolio

WORKDIR /Portfolio

COPY requirements/prod.txt ./

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY . /Portfolio/


CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "Portfolio", "Portfolio.wsgi:application"]

