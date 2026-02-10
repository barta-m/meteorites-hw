# Use python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of application code
COPY . .

# Default command to run when the container starts
CMD ["python", "script.py"]