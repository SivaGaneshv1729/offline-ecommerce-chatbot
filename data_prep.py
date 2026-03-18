from datasets import load_dataset
import random

def main():
    print("Loading Ubuntu Dialogue Corpus...")
    # Using a small subset or specific split if available, otherwise just loading train
    try:
        dataset = load_dataset("sedthh/ubuntu_dialogue_qa", split='train', trust_remote_code=True)
        print(f"Dataset loaded. Total rows: {len(dataset)}")
        
        # Sample 20 technical queries
        samples = random.sample(list(dataset), 20) 
        
        print("\n--- SAMPLE TECHNICAL QUERIES ---")
        for i, s in enumerate(samples, 1):
            # Checking for 'question' or similar keys
            query = s.get('question', s.get('utterance', s.get('Context', 'N/A')))
            print(f"{i}. Technical: {query[:150]}")
            print("-" * 20)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
