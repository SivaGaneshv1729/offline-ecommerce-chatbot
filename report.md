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
1. **Persona Alignment**: The One-Shot method consistently followed the "Chic Boutique" persona, starting responses with friendly greetings as shown in the example. Zero-Shot responses were helpful but occasionally felt more generic or included long disclaimers.
2. **Conciseness**: One-Shot responses were typically more concise and direct, mirroring the style of the provided example.
3. **Hallucination**: Both methods exhibited minor hallucinations regarding specific store features (e.g., app availability, currency support). However, One-Shot was slightly better at admitting limitations when the example showed a clear policy boundary.

## Conclusion & Limitations
Llama 3.2 (3B) is surprisingly capable of handling common customer service queries on local hardware. The One-Shot prompting technique significantly improves the quality and consistency of the "Agent" persona.

**Limitations**:
- **Static Knowledge**: The model lacks access to real-time order data or inventory.
- **Hallucination Risk**: Without Retrieval-Augmented Generation (RAG), the model may "guess" store policies.
- **Hardware Constraints**: Response times can be slow depending on CPU/GPU capabilities.

**Next Steps**: Implement a RAG system to provide the model with a real policy knowledge base.
