# Use Python base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy all files into the image
COPY . .

# Install Flask
RUN pip install flask

# Expose the port used by the app
EXPOSE 5002

# Run the application
CMD ["python", "product_service.py"]
