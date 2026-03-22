# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Environment variable to help the client find the host-run Ollama server
# Use host.docker.internal for Windows/Mac
ENV OLLAMA_HOST=http://host.docker.internal:11434

# Use an environment variable in chatbot.py if we wanted to make it dynamic
# For now, we'll keep the script as is or adjust it to check ENV

# Run the chatbot script
CMD ["python", "chatbot.py"]
