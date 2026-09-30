
def find_requirements(documents, question):
    results = []

    words = question.lower().split()

    for document in documents:
        content = document["content"].lower()

        for word in words:
            if word in content:
                results.append(document)
                break

    return results
