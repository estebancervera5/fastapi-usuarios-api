from pydantic import BaseModel

class Libro(BaseModel):
   # nombre: str
    #email: str
    #password: str
   nombre: str
   autor: str
   isbn: str