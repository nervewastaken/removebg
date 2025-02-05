# Use a specific version of Python
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies if a requirements file exists
RUN pip install --no-cache-dir -r requirements.txt || true

EXPOSE 5000

# Run the Python model script first, then the application script
CMD ["python", "app.py"]