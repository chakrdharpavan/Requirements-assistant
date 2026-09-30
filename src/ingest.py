
from pathlib import Path

data_folder = Path("data/sample_templates")


def load_documents():
    documents = []

    for file in data_folder.glob("*.md"):
        content = file.read_text(encoding="utf-8")

        documents.append({
            "name": file.name,
            "content": content
        })

    return documents


documents = load_documents()

print("Documents loaded:", len(documents))

for document in documents:
    print("\nFile:", document["name"])
    print(document["content"][:300])
