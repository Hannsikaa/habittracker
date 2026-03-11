from fastapi import FastAPI
import operations

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Habit Tracker API is running"}

@app.get("/habits")
def get_habits():
    return operations.habits

@app.post("/habits")
def add_habit(name: str):
    operations.add_habits(name)
    return {"message": "Habit added"}

@app.put("/habits/done")
def mark_done(index: int):
    operations.mark_habit_done([index])
    return {"message": "Habit marked done"}

@app.put("/habits/change_name")
def change_name(name: str,newname: str):
    operations.change_habit_name(name,newname)
    return {"message": "Habit name changed"}

@app.delete("/habits/{name}")
def delete_habit(name: str):
    operations.delete_habit(name)
    return {"message": "Habit deleted"}

@app.get("/habits/search")
def search_habit(name: str):
    result= operations.search_habit(name)
    return {"message": result}

@app.get("/habits/leaderboard")
def leaderboard_sort():
    result= operations.leaderboard_sort()
    return {"message": result}