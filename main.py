from fastapi import FastAPI, HTTPException
import operations
from schemas import HabitCreate, HabitIndex, HabitRename

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Habit Tracker API is running"}

@app.get("/habits")
def get_habits():
    result=operations.get_habits()
    return {"habits":result}

@app.post("/habits")
def add_habit(name: HabitCreate):
    result= operations.add_habits(name.name)
    if not result:
        raise HTTPException(status_code=400, detail="Habit already exists")
    return {"message": "Habit added"}

@app.put("/habits/done")
def mark_done(index: HabitIndex):
    operations.mark_habit_done([index.index])
    return {"message": "Habit marked done"}

@app.put("/habits/change_name")
def change_name(name: HabitRename):
    result=operations.change_habit_name(name.name,name.newname)
    if not result:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit name changed"}

#ikkada name direct url nundi teeskunnam so pydantic model avsaram led
@app.delete("/habits/{name}")
def delete_habit(name: str):
    found = operations.delete_habit(name)
    if not found:
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": "Habit deleted"}

# so ikkada name is a path parameter search?name=smtg ani vastadi in url so ikkada string ani teeskunnam instead of a pydantic model
@app.get("/habits/search")
def search_habit(name: str):
    result= operations.search_habit(name)
    if result=="Habit not found":
        raise HTTPException(status_code=404, detail="Habit not found")
    return {"message": result}

@app.get("/habits/leaderboard")
def leaderboard_sort():
    result= operations.leaderboard_sort()
    return {"message": result}