from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Модели со структурой ответов сервера
class NoteCreate(BaseModel):
    text: str

class NoteID(BaseModel):
    id: int

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime

class NoteText(BaseModel):
    id: int
    text: str

class NoteList(BaseModel):
    notes: List[int]

class TokenList(BaseModel):
    tokens: List[str]
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Запрос на корневой путь")
    return {"message": "Hello World"}
# Пример маршрутов

# Маршрут для проверки работы сервера
# @app.get("/")
# def read_root():
#     return {"message": "Hello, World!"}

# Маршрут для создания заметки
@app.post("/notes", response_model=NoteID)
def create_note(note: NoteCreate):
    return {"id": 1}

# Маршрут для получения списка ID всех заметок
@app.get("/notes", response_model=NoteList)
def get_notes():
    return {"notes": [1, 2, 3]}
