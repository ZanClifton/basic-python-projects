import csv

file = open("log.csv")

reader = csv.reader(file)

list = []

for row in reader:
    list.append(row)

cars_that_left = []

for i in list:
    if i[2] == "Car" and i[3] == "Exit":
        cars_that_left.append(i)

list_of_times = []
list_of_timestamps = []

for i in cars_that_left:
    for j in list:
        if i[1] == j[1] and i[3] != j[3] and j[0] not in list_of_timestamps:
            exit_time = i[0]
            entry_time = j[0]
            list_of_timestamps.append(j[0])

            hours_stayed = int(
                exit_time.split(" ")[1].split(".")[0].split(":")[0]
            ) - int(
                entry_time.split(" ")[1].split(".")[0].split(":")[0]
            )
            minutes_stayed = int(
                exit_time.split(" ")[1].split(".")[0].split(":")[1]
            ) - int(
                entry_time.split(" ")[1].split(".")[0].split(":")[1]
            )
            seconds_stayed = int(
                exit_time.split(" ")[1].split(".")[0].split(":")[2]
            ) - int(entry_time.split(" ")[1].split(".")[0].split(":")[2])

            if seconds_stayed < 0:
                seconds_stayed = 60 + seconds_stayed
                minutes_stayed -= 1

            if minutes_stayed < 0:
                minutes_stayed = 60 + minutes_stayed
                hours_stayed -= 1

            if hours_stayed < 0:
                hours_stayed = 24 + hours_stayed

            list_of_times.append(
                [hours_stayed, minutes_stayed, seconds_stayed])

all_hours = 0
all_minutes = 0
all_seconds = 0

for i in list_of_times:
    all_hours += i[0]
    all_minutes += i[1]
    all_seconds += i[2]

all_hours_in_seconds = all_hours * 3600
all_minutes_in_seconds = all_minutes * 60

total_seconds_stayed = all_hours_in_seconds + \
    all_minutes_in_seconds + all_seconds

length = len(list_of_times)

avg_stay_in_seconds = total_seconds_stayed / length

avg_hours = 0
avg_minutes = 0

while avg_stay_in_seconds > 59:
    avg_stay_in_seconds -= 60
    avg_minutes += 1

while avg_minutes > 59:
    avg_minutes -= 60
    avg_hours += 1

if avg_hours < 10:
    avg_hours = f"0{avg_hours}"

if avg_minutes < 10:
    avg_minutes = f"0{avg_minutes}"

if avg_stay_in_seconds < 10:
    avg_stay_in_seconds = f"0{round(avg_stay_in_seconds)}"
else:
    avg_stay_in_seconds = round(avg_stay_in_seconds)

print(
    f"Average length of stay: {avg_hours}:{avg_minutes}:{avg_stay_in_seconds}")


for i in cars_that_left:
    count = 0
    registration = i[1]
    for j in cars_that_left:
        if j[1] == registration:
            count += 1
    print(f"{registration} visited the car park {count} times")
