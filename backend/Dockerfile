# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend code
COPY app.py /app

# Install Flask
RUN pip install Flask

# Expose port 5000
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
