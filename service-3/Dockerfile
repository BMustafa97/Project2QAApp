FROM python:latest
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5002
ENTRYPOINT ["python3", "app.py"]