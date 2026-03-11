import operations
import time

print("========================\nHABIT TRACKER CLI v1.0\n========================")
time.sleep(1)
print("1.add habit   2.show habits   3.change habit name   4.change habit status    5.delete habit    6.reset all    7.search habit    8.Leaderboard    9.exit")
while True:
    n=int(input("Enter your choice:"))
    match n :
        case 1:
            n=input("Enter name:")
            operations.add_habits(n)
        case 2:
            operations.show_habits()
        case 3:
            n=input("Enter habit name:")
            nn=input("Enter new habit name:")
            operations.change_habit_name(n,nn)
        case 4:
            print("Choose habit to mark done:")
            n=list(map(int,input().split()))
            operations.mark_habit_done(n)
        case 5:
            n=input("Enter habit name:")
            operations.delete_habit(n)
        case 6:
            operations.reset_all()
        case 7:
            n=input("Enter habit you want to search:")
            operations.search_habit(n)
        case 8:
            operations.leaderboard_sort()
        case 9:
            exit()
        case _:
            print("wrong choice")
