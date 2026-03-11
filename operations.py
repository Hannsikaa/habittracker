import time
import json

try:
    with open("habits.json", "r") as file:
        habits = json.load(file)
    # file exist ayte ok lekapote new list create chestam
except:
    habits = []

def save_habits():
    with open("habits.json", "w") as file:
        json.dump(habits, file, indent=4)
    # everytime vadadam kanna once function better kada

def add_habits(name):
    habit={
        'name': name,
        'status': False,
        'streak': 0
    }
    for h in habits:
        if h['name'].lower()==name.lower():
            print("Habit already exists.")
            return
    habits.append(habit) # obviously add cheyyanike
    save_habits()

def show_habits():
    print("Loading habits....\n") # loadingggg....
    time.sleep(1) # delay for effect
    if len(habits) == 0:
        print("No habits found")
        return
    for i, h in enumerate(habits, start=1):
        # numbering kosam
        status = "Done" if h["status"] else "Pending"
        streak = h.get("streak", 0)
        # get ante if streak exits print asalu lekunte take it as 0
        print(f"{i}. {h['name']} : {status} : {streak}")
        # format kosam

def change_habit_name(name,newname):
    for h in habits:
        if name.lower()==h['name'].lower():
            h['name']=newname
            save_habits()
            return
    print("Habit not Found")
    

def delete_habit(name):
    for h in habits:
        if name.lower()==h['name'].lower():
            habits.remove(h)
            save_habits()
            return
    print("Habit not Found")

def search_habit(name):
    for h in habits:
        if h['name'].lower()==name.lower():
            status = "Done" if h["status"] else "Pending"
            print(f"{h['name']} : {status} : {h['streak']}")
            return
        print("Habit not found")

def mark_habit_done(done_habits):
    for i in done_habits:
        if 1<= i <=len(habits):
            habits[i-1]['status']=True
            habits[i-1]['streak']=habits[i-1].get("streak", 0)+1
        else: print("Habit not Found")
    save_habits()

def reset_all():
    for h in habits:
        h['status']=False
    save_habits()

def leaderboard_sort():
    h=sorted(habits, key=lambda x: x['streak'])