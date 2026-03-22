# Experiment Report: Offline Customer Support Chatbot

## Introduction
The goal of this project was to evaluate the feasibility of using a local, offline Large Language Model (LLM) for automated customer support. We compared two prompting strategies—Zero-Shot and One-Shot—to determine which provides more accurate and helpful responses for a fictional e-commerce store, "Chic Boutique".

## Methodology
- **Model**: Meta Llama 3.2 (3B) running on Ollama.
- **Dataset**: 20 queries adapted from the Ubuntu Dialogue Corpus to fit e-commerce scenarios.
- **Prompting**:
    - **Zero-Shot**: Role assignment and query instructions only.
    - **One-Shot**: Included one example of a high-quality query-response pair.
- **Scoring**: Responses were manually scored from 1-5 on Relevance, Coherence, and Helpfulness.

## Results & Analysis

### Quantitative Summary
| Prompting Method | Avg Relevance | Avg Coherence | Avg Helpfulness |
|------------------|---------------|---------------|-----------------|
| Zero-Shot        | 4.6           | 5.0           | 4.5             |
| One-Shot         | 4.9           | 5.0           | 4.8             |

### Qualitative Observations
1. **Persona Alignment**: The One-Shot method consistently followed the "Chic Boutique" persona. 
   - *Example (Good)*: Query #1 One-Shot starts with "Thank you for choosing Chic Boutique!", establishing immediate rapport.
   - *Example (Neutral)*: Query #1 Zero-Shot is polite but starts directly with "To create an account...", which is less warm.
2. **Conciseness**: One-Shot responses mirrored the style of the provided example.
   - *Example (Good)*: Query #8 One-Shot concisely lists return steps.
   - *Example (Weak)*: Query #4 Zero-Shot includes a long meta-commentary about being "a bit old-school", which is unnecessary for a support agent.
3. **Accuracy & Hallucination**:
   - *Example (Bad)*: Query #10 Zero-Shot provides detailed but entirely fabricated steps for changing currency in the "Order Summary" section (which doesn't exist).
   - *Example (Good)*: Query #10 One-Shot correctly identifies it doesn't have the info and admits the limitation, following the "Do not make up information" instruction more effectively.

## Conclusion & Limitations
Llama 3.2 (3B) is surprisingly capable of handling common customer service queries on local hardware. The One-Shot prompting technique significantly improves the quality and consistency of the "Agent" persona.

**Limitations**:
- **Static Knowledge**: The model lacks access to real-time order data or inventory.
- **Hallucination Risk**: Without Retrieval-Augmented Generation (RAG), the model may "guess" store policies.
- **Hardware Constraints**: Response times can be slow depending on CPU/GPU capabilities.

**Next Steps**: 
- **RAG Integration**: Implement a Retrieval-Augmented Generation (RAG) system using a vector database (e.g., ChromaDB) to provide the model with a real policy knowledge base.
- **Fine-Tuning**: Explore LoRA fine-tuning on domain-specific e-commerce chat logs to further refine the persona.
- **Quantization Testing**: Compare performance across different quantization levels (q4_K_M vs q8_0) to optimize for speed vs. accuracy on lower-end hardware.

