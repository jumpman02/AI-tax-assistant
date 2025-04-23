import openai
import os
from typing import List

class LLMHandler:
    def __init__(self):
        openai.api_key = os.getenv('OPENAI_API_KEY')
        self.conversation_history = []

    def generate_response(self, question: str, contexts: List[str]) -> str:
        # Combine contexts
        context_text = "\n".join(contexts)
        
        # Create the prompt
        prompt = f"""Answer the following question based only on the provided context.
        
Context:
{context_text}

Question: {question}

Please provide a clear and concise answer based solely on the information provided in the context."""

        # Add conversation history for follow-up questions
        messages = self.conversation_history + [
            {"role": "user", "content": prompt}
        ]

        # Generate response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=150
        )

        answer = response.choices[0].message['content']
        
        # Update conversation history
        self.conversation_history.extend([
            {"role": "user", "content": question},
            {"role": "assistant", "content": answer}
        ])
        
        return answer
