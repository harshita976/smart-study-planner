# SMART STUDY PLANNER
# Python Mini Project

print("=" * 50)
print("          SMART STUDY PLANNER")
print("=" * 50)

name = input("Enter your name: ")
days = int(input("How many days do you want to plan? "))

subjects = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    print("\nSubject", i + 1)
    subject = input("Enter subject name: ")
    hours = float(input("Enter study hours for this subject: "))

    subjects.append({
        "name": subject,
        "hours": hours
    })

print("\n" + "=" * 50)
print("             YOUR STUDY PLAN")
print("=" * 50)

total_hours = 0

for subject in subjects:
    total_hours += subject["hours"]

print("Student Name :", name)
print("Planning Days:", days)
print("Total Subjects:", n)
print("Total Study Hours:", total_hours)

print("\nSubject-wise Plan")
print("-" * 50)

for subject in subjects:
    daily_hours = subject["hours"] / days

    print("Subject :", subject["name"])
    print("Total Hours :", subject["hours"])
    print("Daily Hours :", round(daily_hours, 2))
    print("-" * 50)

# Priority section
print("\nSET PRIORITY FOR SUBJECTS")

for subject in subjects:
    priority = input(
        "Priority for " + subject["name"] +
        " (High/Medium/Low): "
    )
    subject["priority"] = priority

print("\n" + "=" * 50)
print("          FINAL STUDY PLAN")
print("=" * 50)

for subject in subjects:
    print(
        subject["name"],
        " | ",
        subject["priority"],
        " | ",
        round(subject["hours"] / days, 2),
        "hours/day"
    )

print("\n" + "=" * 50)
print("          STUDY TIPS")
print("=" * 50)

print("1. Study difficult subjects when you feel fresh.")
print("2. Take short breaks between study sessions.")
print("3. Revise what you studied every day.")
print("4. Complete your daily target regularly.")
print("\nGood luck with your studies,", name + "! 🌟")
