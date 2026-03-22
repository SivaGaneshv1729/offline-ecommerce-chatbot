from datasets import random
from datasets import load_dataset

def main():
    """
    Loads the Ubuntu Dialogue dataset and samples 20 technical queries for adaptation.
    NOTE: Using 'sedthh/ubuntu_dialogue_qa' as 'rguo12/ubuntu_dialogue_corpus' is currently unavailable.
    """
    print("Loading dataset 'sedthh/ubuntu_dialogue_qa'...")
    try:
        # Load the alternate dataset split
        dataset = load_dataset("sedthh/ubuntu_dialogue_qa", split="train")
        
        # We are interested in the 'train' split which contains the dialogues
        train_data = dataset
        
        # Sample 20 technical queries
        indices = random.sample(range(len(train_data)), 20)
        samples = [train_data[i] for i in indices]

        print("\n--- Technical Queries for Adaptation ---")
        with open("samples.txt", "w", encoding="utf-8") as f:
            for i, sample in enumerate(samples, 1):
                # Column name might vary; 'question' covers most cases in this subset
                query = sample.get('question', sample.get('text', 'N/A'))
                print(f"{i}. {query}")
                f.write(f"{i}. {query}\n")
        
        print("\nSamples saved to 'samples.txt'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
