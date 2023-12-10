# # Use the official Python base image
# FROM python:3.8

# # Set the working directory in the container
# WORKDIR /app

# # Copy the dependencies file to the working directory
# COPY requirements.txt .

# # Install any dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the content of the local src directory to the working directory
# COPY . .

# # Specify the command to run on container start
# CMD streamlit run app.py --server.port $PORT
# Use an official Python runtime as a parent image
FROM python:3.10.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]