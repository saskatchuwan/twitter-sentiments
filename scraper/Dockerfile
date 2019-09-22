FROM python:3

WORKDIR /twitter-sentiments/scraper

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "bash", "./run.sh"]