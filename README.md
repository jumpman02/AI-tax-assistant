# AI Tax Assistant

A simple prototype that answers questions about tax policies using context-aware AI responses.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:
   ```bash
   pip install -r requirements.txt
```

Create a .env file with your OpenAI API key:
```bash
OPENAI_API_KEY=your_api_key_here
```
Run the application:
```bash
python src/main.py
```
## Approach
- Uses sentence-transformers for semantic similarity search

- Implements vector-based retrieval for finding relevant context

- Integrates with OpenAI's GPT-3.5-turbo for generating responses

- Maintains conversation history for follow-up questions

- Uses environment variables for secure API key management
