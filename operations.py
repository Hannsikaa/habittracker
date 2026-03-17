import time
import json
from database import get_connection
from auth import *
from schemas import *
from fastapi import HTTPException

def get_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

def add_habits(name):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO habits (name, status, streak) VALUES (?, ?, ?)",
            (name, False, 0)
        )
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

def show_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits")

    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        print("No habits found")
        return
    for i, h in enumerate(rows, start=1):
        # numbering kosam
        status = "Done" if h["status"] else "Pending"
        streak = h.get("streak", 0)
        # get ante if streak exits print asalu lekunte take it as 0
        print(f"{i}. {h['name']} : {status} : {streak}")
        # format kosam

def change_habit_name(name,newname):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("UPDATE habits SET name = ? WHERE name = ?", (newname, name))
        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()
    

def delete_habit(name):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM habits WHERE name = ?", (name,))
        if cursor.rowcount == 0:
            return False
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

def search_habit(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits WHERE name = ?", (name,))

    row = cursor.fetchone()

    conn.close()

    if row:
        status = "Done" if row['status'] else "Pending"
        return (f"{row['name']} : {status} : {row['streak']}")
    return "Habit not found"

def mark_habit_done(id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE habits SET status = 1, streak = streak + 1 WHERE id = ?",
            (id,)
        )
        conn.commit()
        return True

    except Exception as e:
        print(e)
        return False    

    finally:
        conn.close()

def reset_all():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "UPDATE habits SET status = 0, streak = 0"
        )
        conn.commit()
        return True

    except:
        return False

    finally:
        conn.close()

def leaderboard_sort():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM habits ORDER BY streak DESC")

    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]

def total_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM habits")

    rows = cursor.fetchone()[0]

    conn.close()

    return rows

def completed_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM habits WHERE status = 1")

    rows = cursor.fetchone()[0]

    conn.close()

    return rows

def highest_streak():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT MAX(streak) FROM habits")

    rows = cursor.fetchone()[0]

    conn.close()

    return rows

def stats_habits():
    total = total_habits()
    completed = completed_habits()
    highest = highest_streak()
    return {"total": total, "completed": completed, "highest": highest}

def signup(user: UserCreate):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (user.username,))
    existing_user = cursor.fetchone()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash password
    hashed_password = hash_password(user.password)

    # Insert user
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)",
        (user.username, hashed_password)
    )

    conn.commit()
    conn.close()

    return {"message": "User created successfully"}