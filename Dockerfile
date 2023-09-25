FROM python:3
COPY . /app
WORKDIR /app
RUN apt update && apt install -y git libcairo2 && pip install --upgrade -r requirements.txt
EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]