FROM python:3.6

COPY requirements.txt .
COPY scraper.py .

RUN apt install git
# RUN git clone --depth=1 https://github.com/twintproject/twint.git
RUN git clone --depth=1 https://github.com/himanshudabas/twint.git
RUN pip3 install ./twint/ -r ./twint/requirements.txt

RUN pip3 install -r requirements.txt

RUN mkdir home/work
RUN mkdir home/scrapped_data
