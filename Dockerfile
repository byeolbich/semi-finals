FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy your application
COPY . .

# Expose the port (Railway will pass PORT via env)
EXPOSE 5000

# Set environment path if needed
ENV PATH="/root/.local/bin:$PATH"

# Command to run the app
CMD ["python", "app.py"]
