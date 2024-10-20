# Dockerfile for app2.py (Web Request API)
FROM python:3.10-slim
WORKDIR /app
COPY api2.py /app
RUN pip install Flask requests
CMD ["python", "app2.py"]
