FROM python:3-alpine3.14
WORKDIR /WoG
COPY . /WoG
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 3000
CMD python ./MainGame.py
