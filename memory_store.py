from sentence_transformers import SentenceTransformer
import faiss

class MemoryStore:
    def __init__(self):
        self.memories = []  # Store text chunks
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.index = faiss.IndexFlatL2(384)  # 384 = vector size for this model

    def add_memory(self, text):
        """Break text into chunks and store embeddings."""
        chunks = self._split_into_chunks(text, chunk_size=100)
        for chunk in chunks:
            self.memories.append(chunk)
            vector = self.model.encode([chunk])
            self.index.add(vector)

    def search(self, query, top_k=3):
        """Return top K most relevant memories to a query."""
        query_vector = self.model.encode([query])
        distances, indices = self.index.search(query_vector, top_k)
        return [self.memories[i] for i in indices[0]]

    def _split_into_chunks(self, text, chunk_size=100):
        """Simple chunking: breaks long memory into small groups of sentences."""
        words = text.split()
        return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]
