from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from app.rag.vector_store import load_vector_store


llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)


def ask_question(question):

    vectorstore = load_vector_store()

    docs = vectorstore.similarity_search(
        question,
        k=3
    )

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer only from the provided context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content