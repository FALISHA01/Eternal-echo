import ollama
from memory_store import MemoryStore
from memory_loader import load_memories_from_folder

# 1. Load and embed memory
text = load_memories_from_folder("assets")
store = MemoryStore()
store.add_memory(text)

# 2. Short-term memory for live chat context
chat_history = []  # this stores last few messages during runtime

# 3. Chat function with memory
def chat_with_person(user_input,store):
    # Search top memory chunks (long-term)



    context_chunks = store.search(user_input, top_k=3)
    context = "\n".join(context_chunks)

    # Build recent chat history (short-term)
    history_snippet = ""
    for u, a in chat_history[-5:]:
        history_snippet += f"\nYou: {u}\nSambhavi: {a}"

    # Construct the full prompt
    full_prompt = f"""
You are replying *exactly* like Sambhavi. You often switch to Hindi naturally, use Gen Z lingo, and keep things light and caring, like a best friend would.

You are currently chatting with Falisha. Your past WhatsApp messages are shown below as memories. Use them to stay in character and respond how Sambhavi would.

## Memories:
{context}

## Recent Chat:
{history_snippet}

Now, respond to this new message from Falisha:
{user_input}
"""

    # Ask LLaMA 3 via Ollama
    response = ollama.chat(model="llama3", messages=[
        {"role": "user", "content": full_prompt}
    ])
    bot_reply = response['message']['content']

    # Save exchange to chat history
    chat_history.append((user_input, bot_reply.strip()))
    
    return bot_reply
