from google import genai

client = genai.Client()


def generate_answer(question, documents):

    if not documents:
        return "I could not find anything related to your question."

    context = ""

    for document in documents:
        context += document["content"]
        context += "\n\n"

    prompt = f"""
You are a Business Requirements Assistant.

Answer the user's question using ONLY the information provided in the document.

Document content:
{context}

User question:
{question}

Give a clear and concise business-oriented answer.

If the information is not available in the document, say:
"The provided document does not contain enough information to answer this question."

Do not invent facts or assumptions.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text
