def human_escalation(query):
    print("\n" + "="*50)
    print("🚨 ESCALATING TO HUMAN AGENT")
    print("="*50)
    print(f"Customer Query: {query}")
    print("Bot could not answer confidently.")
    print("="*50)
    human_response = input("Human Agent - Type your response: ")
    return human_response