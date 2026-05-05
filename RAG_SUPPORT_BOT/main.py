from graph import build_graph

def main():
    print("="*50)
    print("Welcome to TechCare Customer Support Bot!")
    print("="*50)
    print("Type 'quit' to exit\n")

    graph = build_graph()

    while True:
        query = input("You: ")
        if query.lower() == "quit":
            print("Goodbye!")
            break

        result = graph.invoke({
            "query": query,
            "context": "",
            "answer": "",
            "escalate": False
        })

        print(f"\nBot: {result['answer']}\n")
        print("-"*50)

if __name__ == "__main__":
    main()