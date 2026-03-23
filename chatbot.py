import requests
import json
import os
import sys

# Configuration
OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"
RESULTS_DIR = 'eval'
RESULTS_FILE = os.path.join(RESULTS_DIR, 'results.md')

# 20 adapted e-commerce queries from technical support scenarios
QUERIES = [
    "How do I create an account on your store?",
    "My discount code is not working at checkout.",
    "How do I reset my account password?",
    "Where can I find my order invoice?",
    "Is your mobile app available on iOS?",
    "How do I update my shipping address?",
    "I'm getting an 'out of stock' error for items in my cart.",
    "How do I return a purchased item?",
    "My payment was declined during checkout.",
    "How do I change the currency on the website?",
    "Is there a physical store where I can visit?",
    "The product images are not loading correctly.",
    "How do I save items to my wishlist?",
    "When will the new summer collection be released?",
    "How do I reach customer support?",
    "Can I share my referral link with friends?",
    "How do I enable SMS notifications for my order?",
    "Why is my shipping taking longer than expected?",
    "How do I delete my account and data?",
    "Are your products ethically sourced?"
]

def query_ollama(prompt):
    """Sends a prompt to the local Ollama instance and returns the response."""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        # Increased timeout to 90s to handle potentially slow local CPU inference
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=90)
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return f"Error: {e}"

def load_template(filepath):
    """Loads a prompt template from a file."""
    if not os.path.exists(filepath):
        print(f"Template not found: {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    # Ensure findings directory exists
    if not os.path.exists(RESULTS_DIR):
        os.makedirs(RESULTS_DIR)

    # Safety Check: Do not overwrite scored results
    if os.path.exists(RESULTS_FILE):
        print(f"WARNING: {RESULTS_FILE} already exists.")
        choice = input("Overwrite existing results and lose manual scores? (y/N): ").lower()
        if choice != 'y':
            print("Operation cancelled to protect your scores.")
            return

    # Load templates
    zero_shot_tpl = load_template('prompts/zero_shot_template.txt')
    one_shot_tpl = load_template('prompts/one_shot_template.txt')
    
    with open(RESULTS_FILE, 'w', encoding='utf-8') as f:
        # Write Header
        f.write("# Evaluation Results\n\n")
        f.write("## Scoring Rubric\n")
        f.write("- **Relevance (1-5)**: Addresses the query correctly.\n")
        f.write("- **Coherence (1-5)**: Grammatically correct and clear.\n")
        f.write("- **Helpfulness (1-5)**: Provides useful instructions.\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|--------------------|\n")

        # Run Inference
        for i, query in enumerate(QUERIES, 1):
            print(f"Processing query {i}/{len(QUERIES)}...")
            
            # Zero-Shot Pass
            zs_prompt = zero_shot_tpl.format(query=query)
            zs_response = query_ollama(zs_prompt).replace('\n', ' ')
            f.write(f"| {i} | \"{query}\" | Zero-Shot | {zs_response} | | | |\n")
            
            # One-Shot Pass
            os_prompt = one_shot_tpl.format(query=query)
            os_response = query_ollama(os_prompt).replace('\n', ' ')
            f.write(f"| {i} | \"{query}\" | One-Shot | {os_response} | | | |\n")

    print(f"\nSuccess! Results saved to {RESULTS_FILE}")
    print("Please proceed with manual scoring in the markdown file.")

if __name__ == "__main__":
    main()
