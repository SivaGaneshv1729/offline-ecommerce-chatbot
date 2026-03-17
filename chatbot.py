import requests
import json
import os

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2:3b"

# 20 adapted e-commerce queries
QUERIES = [
    "My discount code is not working at checkout.",
    "How do I track the shipping status of my recent order?",
    "Do you offer international shipping to Europe?",
    "Can I change my shipping address after placing an order?",
    "What is your return policy for sale items?",
    "I received a damaged item, how do I get a replacement?",
    "How can I cancel my order?",
    "Are your products ethically sourced?",
    "Do you have a size guide for your clothing?",
    "How do I reset my account password?",
    "What payment methods do you accept?",
    "Can I combine two separate orders to save on shipping?",
    "Is there a physical store where I can try on clothes?",
    "How long does standard shipping usually take?",
    "Do you offer gift wrapping services?",
    "Why was my payment declined?",
    "Are the colors on the website accurate to the real product?",
    "Can I pre-order items that are coming soon?",
    "How do I sign up for your newsletter for discounts?",
    "Is my personal information secure with you?"
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
