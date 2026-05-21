from app.vectorstore.search import search

query = "What is the main objective of the ML portfolio roadmap?"

results = search(query)

print("\nTop Retrieved Chunks:\n")

for i, result in enumerate(results):

    print(f"\nResult {i+1}")
    print("-" * 50)

    print(result.payload["text"])

    print("\nScore:", result.score)