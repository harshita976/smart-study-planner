print("===== SMART STUDY PLANNER =====")

name = input("Enter your name: ")
subject = input("Enter subject: ")
topic = input("Enter topic to study: ")
hours = float(input("Enter study hours: "))

print("\n===== YOUR STUDY PLAN =====")
print("Student:", name)
print("Subject:", subject)
print("Topic:", topic)
print("Study Hours:", hours)

if hours >= 3:
    print("Plan: Deep Study + Practice + Revision")
elif hours >= 2:
    print("Plan: Study + Practice")
else:
    print("Plan: Quick Study + Revision")

print("\nStudy Tips:")
print("1. Study without distractions.")
print("2. Take short breaks.")
print("3. Revise the topic after studying.")
print("4. Practice questions regularly.")

print("\n===== PLAN CREATED SUCCESSFULLY =====")
