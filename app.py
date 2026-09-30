from src.ingest import load_documents
from src.retrieve import find_requirements
from src.generate import generate_answer


documents = load_documents()

print("Requirements Assistant")
print("Documents loaded:", len(documents))

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break

    results = find_requirements(documents, question)
    answer = generate_answer(question, results)

    print("\n" + answer)
