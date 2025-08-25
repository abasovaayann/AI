import google.generativeai as genai

# Configure with API key
genai.configure(api_key="AIzaSyA6W6emO55_KQy7UkLQJW_FvA7UATTFvhI")

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

conversation = [
    {"role": "system", "content": "You are a travel guide designed to provide information about landmarks that tourist will explore. "},
    {"role": "user", "content": "What is the most famous landmark in Paris?"},
    {"role": "assistant", "content": "The most famous landmark in Paris is the Eiffel Tower."}
]

questions = [
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?"
]

for question in questions:
    conversation.append({"role": "user", "content": question})

    # Convert conversation into one string (Gemini doesn't support role-based messages directly like OpenAI)
    history = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in conversation])

    response = model.generate_content(history)

    answer = response.text
    print("Your_Name:", question)
    print("X:", answer)

    conversation.append({"role": "", "content": answer})
