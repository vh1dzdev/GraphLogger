FROM python:3.13-slim
WORKDIR /usr/GraphLogger/
EXPOSE 8000
COPY ./ ./
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]