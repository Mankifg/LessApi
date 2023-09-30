FROM python:3
COPY . /app
WORKDIR /app
RUN mkdir tmp
RUN apt update && apt install -y git libcairo2 && pip install --upgrade -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]