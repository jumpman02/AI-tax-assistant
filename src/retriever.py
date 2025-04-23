from sentence_transformers import SentenceTransformer
import numpy as np
import json
from typing import List, Dict, Tuple

class Retriever:
    def __init__(self, data_path: str):
        # Initialize the sentence transformer model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.data = self._load_data(data_path)
        self.embeddings = self._create_embeddings()

    def _load_data(self, data_path: str) -> List[Dict]:
        with open(data_path, 'r') as f:
            return json.load(f)

    def _create_embeddings(self) -> np.ndarray:
        texts = [item['content'] for item in self.data]
        return self.model.encode(texts)

    def retrieve(self, query: str, top_k: int = 2) -> List[str]:
        # Encode the query
        query_embedding = self.model.encode(query)
        
        # Calculate similarities
        similarities = np.dot(self.embeddings, query_embedding)
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        # Return the most relevant contexts
        return [self.data[idx]['content'] for idx in top_indices]
