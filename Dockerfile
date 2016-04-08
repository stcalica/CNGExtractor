FROM python:2.7-onbuild

COPY . /src

RUN pip install -r requirements.txt


RUN chmod 755 /src

VOLUME /data : /src/data

CMD ["python", "extractor.py"]
