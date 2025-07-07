# Use a slim Python base image

FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy only necessary files first (better for Docker cache)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of your app
COPY . .

# Expose the port Streamlit will run on
EXPOSE 8501

# Set environment variable to disable Streamlit's telemetry
ENV STREAMLIT_DISABLE_UPDATE_CHECK true

# Default command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.enableCORS=false"]
