import os
from dotenv import load_dotenv
from retriever import Retriever
from llm_handler import LLMHandler

def main():
    load_dotenv()
    
    # Initialize components
    retriever = Retriever('data/tax_data.json')
    llm_handler = LLMHandler()
    
    print("AI Tax Assistant (type 'quit' to exit)")
    print("=====================================")
    
    while True:
        # Get user question
        question = input("\nYour question: ").strip()
        
        if question.lower() == 'quit':
            break
        
        # Retrieve relevant contexts
        contexts = retriever.retrieve(question)
        
        # Generate response
        response = llm_handler.generate_response(question, contexts)
        
        print("\nAnswer:", response)

if __name__ == "__main__":
    main()
