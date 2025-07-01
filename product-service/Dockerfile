# Use a lighter base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only necessary files first to help cache pip layer
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining files
COPY . .

# Expose the port Cloud Run requires
EXPOSE 8080

# Run the application
CMD ["python", "product_service.py"]
