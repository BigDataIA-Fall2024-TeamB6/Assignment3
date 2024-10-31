# Use the base image from Apache Airflow
FROM apache/airflow:2.10.2

# Switch to root user to install additional software
USER root

# Install system dependencies, Chrome, and Chromedriver
RUN apt-get update && \
    apt-get install -y wget unzip && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb && \
    wget -q https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Set environment variable for PATH to ensure only necessary directories are included
ENV PATH="/home/airflow/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# Switch back to the airflow user to maintain container security
USER airflow

# Install additional Python libraries
RUN pip install selenium==4.25.0
