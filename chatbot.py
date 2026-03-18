import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# 20 adapted e-commerce queries from technical support scenarios
QUERIES = [
    "How do I create an account on your store?", # Adapt: How to install Ubuntu?
    "My discount code is not working at checkout.", # Adapt: My wifi is not connecting.
    "How do I reset my account password?", # Adapt: How to reset root password?
    "Where can I find my order invoice?", # Adapt: Where are the log files?
    "Is your mobile app available on iOS?", # Adapt: Can I run this on Mac?
    "How do I update my shipping address?", # Adapt: How to update the kernel?
    "I'm getting an 'out of stock' error for items in my cart.", # Adapt: Unmet dependencies error.
    "How do I return a purchased item?", # Adapt: How to uninstall package?
    "My payment was declined during checkout.", # Adapt: Permission denied error.
    "How do I change the currency on the website?", # Adapt: How to change timezone?
    "Is there a physical store where I can visit?", # Adapt: Is there a GUI for this?
    "The product images are not loading correctly.", # Adapt: Screen resolution is wrong.
    "How do I save items to my wishlist?", # Adapt: How to backup my files?
    "When will the new summer collection be released?", # Adapt: What is the latest version?
    "How do I reach customer support?", # Adapt: How to contact the dev team?
    "Can I share my referral link with friends?", # Adapt: Can I share my desktop?
    "How do I enable SMS notifications for my order?", # Adapt: How to enable ssh?
    "Why is my shipping taking longer than expected?", # Adapt: Performance is slow.
    "How do I delete my account and data?", # Adapt: How to format a drive?
    "Are your products ethically sourced?" # Adapt: Is this open source?
]

def query_ollama(prompt):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_ENDPOINT, json=payload)
        response.raise_for_status()
        return json.loads(response.text).get("response", "").strip()
    except requests.exceptions.RequestException as e:
        print(f"Error querying Ollama: {e}")
        return "Error: Could not get a response from the model."

def load_template(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if not os.path.exists('eval'):
        os.makedirs('eval')

    zero_shot_tpl = load_template('prompts/zero_shot_template.txt')
    one_shot_tpl = load_template('prompts/one_shot_template.txt')

    results_file = 'eval/results.md'
    
    with open(results_file, 'w', encoding='utf-8') as f:
        f.write("# Evaluation Results\n\n")
        f.write("| Query # | Customer Query | Prompting Method | Response | Relevance (1-5) | Coherence (1-5) | Helpfulness (1-5) |\n")
        f.write("|---------|----------------|------------------|----------|-----------------|-----------------|--------------------|\n")

        for i, query in enumerate(QUERIES, 1):
            print(f"Processing query {i}/20...")
            
            # Zero-Shot
            zs_prompt = zero_shot_tpl.format(query=query)
            zs_response = query_ollama(zs_prompt).replace('\n', ' ')
            f.write(f"| {i} | \"{query}\" | Zero-Shot | {zs_response} | | | |\n")
            
            # One-Shot
            os_prompt = one_shot_tpl.format(query=query)
            os_response = query_ollama(os_prompt).replace('\n', ' ')
            f.write(f"| {i} | \"{query}\" | One-Shot | {os_response} | | | |\n")

    print(f"Evaluation complete. Results saved to {results_file}")

if __name__ == "__main__":
    main()
