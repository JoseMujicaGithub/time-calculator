def add_time(start_time, duration_time, starting_day_of_the_week=None):
    days_index = {"Monday": 0,"Tuesday": 1,"Wednesday": 2,"Thursday": 3,"Friday": 4,"Saturday": 5,"Sunday": 6}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
    start_time_ = (start_time.partition(" "))[0]
    am_pm = str((start_time.partition(" "))[2]).strip().upper()
    start_time_hours = int((start_time_.partition(":"))[0])
    duration_time_hours = int((duration_time.partition(":"))[0])
    start_time_minutes = int((start_time_.partition(":"))[2])
    duration_time_minutes = int((duration_time.partition(":"))[2])
    hours_added_from_munites, minutes = divmod(start_time_minutes + duration_time_minutes, 60)
    cycles, hours = divmod(start_time_hours + duration_time_hours + hours_added_from_munites, 12)
    minutes = str(minutes) if minutes > 9 else "0" + str(minutes)
    am_pm_flip = {"AM": "PM", "PM": "AM"}
    amount_of_days_added = int((duration_time_hours + hours_added_from_munites +(int(minutes) / 60)) / 24)
    if am_pm == "PM" and start_time_hours + duration_time_hours + hours_added_from_munites >= 12:
        amount_of_days_added += 1
    if amount_of_days_added == 1:
        later = ' (next day)'
    if amount_of_days_added > 1:
        later = f' ({amount_of_days_added} days later)'
    if amount_of_days_added==0:
        later=""
    if hours == 0 :
        hours = 12
    if cycles % 2 != 0:
        am_pm = am_pm_flip[am_pm]
    else:
        am_pm = am_pm
    if starting_day_of_the_week:
        starting_day_of_the_week=starting_day_of_the_week.lower().title()
        index = int((days_index[starting_day_of_the_week]) +
                    amount_of_days_added) % 7
        new_day = days[index]
        return str(
            hours) + ':' + minutes + " " + am_pm + ", " + new_day + f"{later}"
    else:
        return str(hours) + ':' + minutes + " " + am_pm + f"{later}"

def validate_time_long(time):
    if time[0].isnumeric() and time[1].isnumeric():
        if int(time[0])<2 and int(time[1])<10:
            if time[2]==":":
                if time[3].isnumeric() and time[4].isnumeric():
                    if int(time[3])<6 and int(time[4])<10:
                        if time[5]==" ":
                            if time[6]=="a" or time[6]=="A" or time[6]=="p" or time[6]=="P":
                                if time[7]=="m" or time[7]=="M":
                                    return time
                                else:
                                    print("===Enter a valid time format===")
                                    return None
                            else:
                                print("===Enter a valid time format===")
                                return None
                        else:
                            print("===Enter a valid time format===")
                            return None
                    else:
                        print("===Enter a valid time format===")
                        return None
                else:
                    print("===Enter a valid time format===")
                    return None
            else:
                print("===Enter a valid time format===")
                return None
        else:
            print("===Enter a valid time format===")
            return None
    else:
        print("===Enter a valid time format===")
        return None

def validate_time_short(time):
    if time[0].isnumeric():
        if int(time[0])<10:
            if time[1]==":":
                if time[2].isnumeric() and time[3].isnumeric():
                    if int(time[2])<6 and int(time[3])<10:
                        if time[4]==" ":
                            if time[5]=="a" or time[5]=="A" or time[5]=="p" or time[5]=="P":
                                if time[6]=="m" or time[6]=="M":
                                    return time
                                else:
                                    print("===Enter a valid time format===")
                                    return None
                            else:
                                print("===Enter a valid time format===")
                                return None
                        else:
                            print("===Enter a valid time format===")
                            return None
                    else:
                        print("===Enter a valid time format===")
                        return None
                else:
                    print("===Enter a valid time format===")
                    return None
            else:
                print("===Enter a valid time format===")
                return None
        else:
            print("===Enter a valid time format===")
            return None
    else:
        print("===Enter a valid time format===")
        return None

print('Enter start time in a 12 hours format example==>(12:00 AM)')
while True:
    time=input("Enter start time: ")
    if len(time)==len("12:00 AM"):
        start_time=validate_time_long(time)
        if start_time:
            break
    if len(time)==len("3:00 PM"):
        start_time=validate_time_short(time)
        if start_time:
            break
    else:
        print("===Enter a valid time format===")

def validate_added_time(duration):
    try:
        if int((duration.partition(':'))[0])>0 and int((duration.partition(':'))[2])<60:
            return duration
        else:
            return None
    except:
        return None
while True:
    duration_time=input("Enter the a valid duration time: ")
    duration=validate_added_time(duration_time)
    if duration != None:
        break
    else:
        continue           

while True:
    option=(input("Do you want to enter a day of the week? (y/n): ")).lower()
    if option=="y":
        while True:
            days=("Monday","Tuesday", "Wednesday","Thursday","Friday","Saturday","Sunday")
            starting_day_of_the_week=input("Enter the current week day: ").lower().title()
            if starting_day_of_the_week in days:
                starting_day_of_the_week=starting_day_of_the_week
                break
            else:
                print('===Enter a valid day===')
    elif option=="n":
        starting_day_of_the_week=None
        break
    else:
        print('Enter a Y or N answer')
    break

print(add_time(start_time,duration_time,starting_day_of_the_week))