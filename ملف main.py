def ai_assistant():
    print("AI Assistant activated. Type 'exit' to quit.")
    while True:
        query = input("Ask me anything: ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        # Simple echo AI placeholder - replace with smarter logic later
        print(f"AI says: I heard you ask '{query}'. Sorry, I'm a simple AI for now.")