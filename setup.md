# Setup Guide: Offline Customer Support Chatbot

This project uses Ollama to serve a local Llama 3.2 model for customer support.

## Prerequisites
1. **Ollama**: Install from [ollama.com](https://ollama.com).
2. **Model**: Pull the Llama 3.2 3B model:
   ```bash
   ollama pull llama3.2:3b
   ```

## Method 1: Local Virtual Environment (Recommended)
1. Navigate to the project folder:
   ```bash
   cd offline-chatbot
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate # macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the chatbot:
   ```bash
   python chatbot.py
   ```

## Method 2: Docker (Alternative)
1. Ensure **Ollama** is running on your host machine.
2. Build the Docker image:
   ```bash
   docker build -t chatbot-client .
   ```
3. Run the container (using `host.docker.internal` to connect to Ollama on the host):
   ```bash
   docker run -it --rm -e OLLAMA_HOST=http://host.docker.internal:11434 chatbot-client
   ```

## Results
Results will be saved in `eval/results.md`.
