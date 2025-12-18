# Langchain

A collection of LangChain examples demonstrating different types of models and their usage.

## Project Structure

```
Models/
├── 1_LLMs/                    # Basic Language Model examples
│   └── 1_llm_demo.py         # Simple LLM demonstration
│
├── 2_ChatModels/              # Chat Model implementations
│   ├── 1_openai.py          # OpenAI Chat Model example
│   ├── 2_claude.py           # Anthropic Claude Chat Model
│   ├── 3_google.py           # Google Gemini Chat Model
│   └── 4_huggingface.py      # Hugging Face Chat Model
│
├── 3_EmbeddingModels/         # Embedding Model examples
│   ├── 1_openai_query.py    # OpenAI embedding query example
│   ├── 2_openai_docs.py     # OpenAI document embeddings
│   └── 3_document_similarity.py  # Document similarity using embeddings
│
├── 2_openai_docs.py          # Additional OpenAI documentation example
├── requirements.txt          # Python dependencies
└── test.py                   # Test file
```

## Setup

1. Install dependencies:

```bash
cd Models
pip install -r requirements.txt
```

2. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your API keys:
     ```
     OPENAI_API_KEY=your_openai_key
     ANTHROPIC_API_KEY=your_anthropic_key
     GOOGLE_API_KEY=your_google_key
     HUGGINGFACE_API_KEY=your_huggingface_key
     ```

## Usage

### LLMs (Language Models)

Basic language model examples for simple text generation:

```bash
python Models/1_LLMs/1_llm_demo.py
```

### Chat Models

Interactive chat model examples supporting multiple providers:

- OpenAI: `python Models/2_ChatModels/1_openai.py`
- Claude: `python Models/2_ChatModels/2_claude.py`
- Google: `python Models/2_ChatModels/3_google.py`
- Hugging Face: `python Models/2_ChatModels/4_huggingface.py`

### Embedding Models

Examples for generating embeddings and computing similarity:

- Query embeddings: `python Models/3_EmbeddingModels/1_openai_query.py`
- Document embeddings: `python Models/3_EmbeddingModels/2_openai_docs.py`
- Document similarity: `python Models/3_EmbeddingModels/3_document_similarity.py`

## Dependencies

See `Models/requirements.txt` for the complete list of dependencies, including:

- LangChain Core
- Provider-specific integrations (OpenAI, Anthropic, Google, Hugging Face)
- Machine learning utilities (NumPy, scikit-learn)
