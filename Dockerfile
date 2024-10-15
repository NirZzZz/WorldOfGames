FROM python:3.9-slim
WORKDIR /WoG
COPY . /WoG
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 3000
CMD python ./MainGame.py
