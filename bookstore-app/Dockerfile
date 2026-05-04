# Dockerfile
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install curl and ping
RUN apt-get update && apt-get install -y curl iputils-ping

# Copy application files
COPY . .

# Expose port
EXPOSE 5000

# Run the app using Gunicorn
CMD ["gunicorn", "-c", "gunicorn.conf.py", "--factory", "app:create_app"]