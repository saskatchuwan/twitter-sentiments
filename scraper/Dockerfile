FROM python:3

WORKDIR /twitter-sentiments/scraper

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "server.py"]