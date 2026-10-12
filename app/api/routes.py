from fastapi import APIRouter
from fastapi import UploadFile

from app.rag.pdf_reader import extract_text
from app.rag.vector_store import create_vector_store
from app.rag.qa import ask_question

router = APIRouter()


@router.post("/upload")
async def upload_pdf(file: UploadFile):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)

    text = extract_text(file_path)

    create_vector_store(text)

    return {
        "message": "PDF uploaded successfully"
    }


@router.get("/ask")
def ask(question: str):

    answer = ask_question(question)

    return {
        "question": question,
        "answer": answer
    }