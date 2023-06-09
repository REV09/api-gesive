from pydantic import BaseModel

class Foto(BaseModel):
    idfoto: int
    data: bytes
    idReporte: int

    class Config:
        orm_mode = True