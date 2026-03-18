# Setup Guide: Offline Customer Support Chatbot

This project uses Ollama to serve a local Llama 3.2 model for customer support.

## Prerequisites
1. **Ollama**: Install from [ollama.com](https://ollama.com).
2. **Model**: Pull the Llama 3.2 3B model:
   ```bash
   ollama pull llama3.2:3b
   ```

## Installation
1. Navigate to the project folder:
   ```bash
   cd offline-chatbot
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install requests datasets
   ```

## Running the Chatbot
To process the 20 queries and generate results:
```bash
python chatbot.py
```
Results will be saved in `eval/results.md`.
