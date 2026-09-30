
def generate_answer(question, documents):
    if not documents:
        return "I could not find anything related to your question."

    answer = "I found the following information:\n\n"

    for document in documents:
        answer += document["content"][:500]
        answer += "\n\n"

    return answer
