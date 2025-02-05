# Use a specific version of Python
FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install –no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .


EXPOSE 5000

# Run the Python model script first, then the application script
CMD ["python", "app.py"]