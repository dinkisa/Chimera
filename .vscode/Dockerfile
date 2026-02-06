#Use an official Python runtime as a parent image  
FROM python:3.11-slim-bookworm  

# Set the working directory in the container to /app  
WORKDIR /app  

# Copy the requirements.txt file to the container  
COPY requirements.txt ./  

# Install dependencies  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy the rest of your application's source code from your host to your image filesystem.  
COPY . .  

# Make port 80 available to the world outside this container  
EXPOSE 80  

# Run app.py when the container launches  
CMD ["python", "app.py"]  