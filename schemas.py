from pydantic import BaseModel

class HabitCreate(BaseModel):
    name: str

class HabitRename(BaseModel):
    name: str
    newname: str

class HabitIndex(BaseModel):
    index: int

