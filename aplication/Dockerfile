FROM python:3.9.0

WORKDIR /usr/local/bin

RUN apt-get update && \
    apt-get upgrade -y

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8050

CMD [ "python","database_population.py" ]