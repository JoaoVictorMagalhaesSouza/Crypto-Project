FROM python:3.9.0

WORKDIR /usr/local/bin

RUN apt-get update && \
    apt-get upgrade -y

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]