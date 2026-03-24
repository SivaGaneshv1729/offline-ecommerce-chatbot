import random
from datasets import load_dataset

def main():
    """
    Loads the Ubuntu Dialogue dataset and samples 20 technical queries for adaptation.
    Uses 'ntcuong777/ubuntu_dialogue_corpus_train' as a stable alternative.
    """
    print("Loading dataset 'ntcuong777/ubuntu_dialogue_corpus_train'...")
    try:
        # Load the stable dataset split
        dataset = load_dataset("ntcuong777/ubuntu_dialogue_corpus_train", split="train")
        
        # We sample 20 technical queries
        indices = random.sample(range(len(dataset)), 20)
        samples = [dataset[i] for i in indices]

        print("\n--- Technical Queries for Adaptation ---")
        with open("samples.txt", "w", encoding="utf-8") as f:
            for i, sample in enumerate(samples, 1):
                # Using 'Context' as it contains the technical query/prompt
                query = sample.get('Context', sample.get('Utterance', 'N/A'))
                # Clean up multiple '__EOS__' tags if present for better readability
                query = query.replace('__EOS__', ' | ').strip()
                print(f"{i}. {query[:100]}...") # Print a preview
                f.write(f"{i}. {query}\n")
        
        print("\nSamples saved to 'samples.txt'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
