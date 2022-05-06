def greet():
    print("Hello!")

hello = greet

hello()

avg = lambda seq: sum(seq) / len(seq)


operations = {
    "average" : avg,
    "total": sum,
    "top": max,
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    op = input("Enter 'average', 'total', or 'top': ")

    op_function = operations[op]
    print(op_function(grades)) 