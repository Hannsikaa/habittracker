from pydantic import BaseModel, Field, field_validator

class HabitCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)

    @field_validator("name") # idi decorator ante name ni validate chese appudu kinda function run cheyyi ani
    def remove_blank_names(cls, v): # cls ante paina cls
        # v ante value ade name 
        if not v.strip():# strip removes spaces at starting and ending of strings
            raise ValueError("Habit name cannot be empty")
        return v

class HabitRename(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    newname: str = Field(min_length=1, max_length=50)

class HabitIndex(BaseModel):
    index: int = Field(gt=0) # gt ante greater than 0

class HabitResponse(BaseModel):
    id: int
    name: str
    status: bool
    streak: int

class MessageResponse(BaseModel):
    message: str

class UserCreate(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    token: str