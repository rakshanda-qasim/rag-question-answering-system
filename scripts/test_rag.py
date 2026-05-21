from app.vectorstore.search import search
from app.generation.generator import generate_answer

query = "What is the objective of the ML portfolio roadmap?"

results = search(query)

context = "\n\n".join([
    result.payload["text"]
    for result in results
])

answer = generate_answer(query, context)

print("\nGenerated Answer:\n")
print(answer)