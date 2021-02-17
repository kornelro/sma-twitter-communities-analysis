FROM python:3.6

COPY requirements.txt .
COPY polarity.py .

RUN pip3 install -U git+https://github.com/aboSamoor/polyglot.git@master
RUN pip3 install -r requirements.txt
RUN polyglot download sentiment2.pl
RUN polyglot download sentiment2.en

RUN mkdir home/work
RUN mkdir home/data
