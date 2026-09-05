import csv,os
from datetime import date
print("="*40,end="")
print("Login-Page",end="")
print("="*40)
user = input("Username :- ")
pwd = input("Password :- ")
f1= "students.csv"
f2="attendance.csv"
aec = "aec_att.csv"
de = "de_att.csv"
etc = "etc_att.csv"
maths = "maths_att.csv"
dsa = "dsa_att.csv"
aec_lab = "aec_lab_att.csv"
de_lab = "de_lab_att.csv"
dsa_lab = "dsa_lab_att.csv"
it_lab = "it_lab_att.csv"
project_lab = "project_lab_att.csv"
ai="ai_att.csv"
ai_lab="ai_lab_att.csv"
subjects = {
    "1": ("AEC", aec),
    "2": ("DE", de),
    "3": ("ETC", etc),
    "4": ("Maths", maths),
    "5": ("DSA", dsa),
    "6": ("IT Lab", it_lab),
    "7": ("AEC Lab", aec_lab),
    "8": ("DE Lab", de_lab),
    "9": ("DSA Lab", dsa_lab),
    "10": ("Project Lab", project_lab),
    "11": ("AI", ai),
    "12": ("AI Lab", ai_lab)
}
def initialize_file():
    files = [
        f1, aec, de, etc, maths, dsa,
        aec_lab, de_lab, dsa_lab,
        it_lab, project_lab, ai, ai_lab
    ]

    for file in files:
        if not os.path.exists(file):
            with open(file, "w", newline="") as f:
                writer = csv.writer(f)

                if file == f1:
                    writer.writerow(["Roll number", "Name", "Branch"])
                else:
                    writer.writerow(
                        ["Date", "Roll number", "Name", "Branch", "Status"]
                    )
def AddStudent():
    roll = input("Enter Roll Number :- ")
    name = input("Enter Name :- ")
    branch = input("Enter Branch :- ")
    with open (f1,"a",newline="") as f:
        writer = csv.writer(f)
        writer.writerow([roll,name,branch])
def ViewStudent(b):
    with open(f1,"r") as f:
        reader=  csv.reader(f)
        if b=="1":
            for i in reader:
                if i[2].lower()=="cse":
                    print(i)
        elif b=="2":
            for i in reader:
                if i[2].lower()=="ai":
                    print(i)
        elif b == "3":
            for i in reader:
                print(i)
        else:
            print("Invalid Choice !")
def MarkAttendance(s):

    subject_name, attendance_file = subjects[s]

    today = date.today().strftime("%d-%m-%Y")

    with open(f1, "r") as student_file:
        reader = csv.reader(student_file)

        students = list(reader)

    with open(attendance_file, "a", newline="") as att_file:

        writer = csv.writer(att_file)

        print("\n" + "=" * 50)
        print(f"        MARK ATTENDANCE - {subject_name}")
        print("=" * 50)

        for student in students:

            roll = student[0]
            name = student[1]
            branch = student[2]

            print(f"\n{roll} :- {name}")

            while True:
                att = input("Mark P/A :- ").upper()

                if att in ["P", "A"]:
                    break

                print("Please enter P or A only!")

            writer.writerow([
                today,
                roll,
                name,
                branch,
                att
            ])

    print("\nAttendance marked successfully!")
def ViewAttendance(s):

    if s not in subjects:
        print("Invalid Choice!")
        return

    subject_name, filename = subjects[s]

    print("\n" + "=" * 70)
    print(f"{subject_name} ATTENDANCE")
    print("=" * 70)

    with open(filename, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            print(
                f"Date: {row[0]} | "
                f"Roll: {row[1]} | "
                f"Name: {row[2]} | "
                f"Branch: {row[3]} | "
                f"Status: {row[4]}"
            )
def ViewAllAttendance():

    for key, value in subjects.items():

        subject_name = value[0]
        filename = value[1]

        print("\n" + "=" * 60)
        print(subject_name)
        print("=" * 60)

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                print(row)
def ViewStudentRecord():

    roll = input("Enter Roll Number :- ")

    # Pehle student ka naam aur branch find karenge
    student_name = None
    student_branch = None

    with open(f1, "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0] == roll:
                student_name = row[1]
                student_branch = row[2]
                break

    if student_name is None:
        print("Student not found!")
        return

    print("\n" + "=" * 70)
    print("              STUDENT ATTENDANCE RECORD")
    print("=" * 70)

    print(f"Roll Number : {roll}")
    print(f"Name        : {student_name}")
    print(f"Branch      : {student_branch}")

    print("\n" + "-" * 70)
    print(f"{'Subject':<20}{'Present':<10}{'Absent':<10}{'Total':<10}{'Percentage'}")
    print("-" * 70)

    total_present = 0
    total_classes = 0

    for subject_name, filename in subjects.values():

        present = 0
        absent = 0

        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:

                if row[1] == roll:

                    if row[4].upper() == "P":
                        present += 1

                    elif row[4].upper() == "A":
                        absent += 1

        total = present + absent

        if total > 0:
            percentage = (present / total) * 100
        else:
            percentage = 0

        total_present += present
        total_classes += total

        print(
            f"{subject_name:<20}"
            f"{present:<10}"
            f"{absent:<10}"
            f"{total:<10}"
            f"{percentage:.2f}%"
        )

    print("-" * 70)

    if total_classes > 0:
        overall_percentage = (total_present / total_classes) * 100
    else:
        overall_percentage = 0

    print(
        f"{'OVERALL':<20}"
        f"{total_present:<10}"
        f"{total_classes - total_present:<10}"
        f"{total_classes:<10}"
        f"{overall_percentage:.2f}%"
    )

    print("=" * 70)
if user == "admin":
    if pwd == "Admin@corp236":
        print("Login Successfully !")
        print("Hello Admin !",end="")
        while True:
            print("\nWhat you want to do ?")
            ch = input('''
1. Add Student
2. View Student
3. Mark Attendnace 
4. View Attendnace
5. View Student Record
6. Exit :- ''')
            
            if int(ch) == 1:
                AddStudent()
            elif int(ch) == 2:
                b = input('''
1. CSE
2. AI
3. Both :-''')
                ViewStudent(b)
            elif int(ch) == 3:
                s = input('''
1. Analog Electronics (AEC)
2. Digital Electronics (DE) 
3. Effective Technical Communication (ETC)
4. Mathematics-III (Calculus)
5. Data Structure and Algorithm (DSA)
6. IT Workshop
7. Analog Electronics Lab (AEC-LAB)
8. Digital Electronics Lab (DE-LAB)
9. Data Structure and Algorithm Lab (DSA-LAB) 
10. Capstone Project (Project-LAB)
11. Introudction To AI (AI)
12. Introduction to AI Lab (AI-LAB):- ''')
                MarkAttendance(s)
            elif int(ch) == 4:
                s = input('''
1. Analog Electronics (AEC)
2. Digital Electronics (DE) 
3. Effective Technical Communication (ETC)
4. Mathematics-III (Calculus)
5. Data Structure and Algorithm (DSA)
6. IT Workshop
7. Analog Electronics Lab (AEC-LAB)
8. Digital Electronics Lab (DE-LAB)
9. Data Structure and Algorithm Lab (DSA-LAB) 
10. Capstone Project (Project-LAB) 
11. Introudction To AI (AI)
12. Introduction to AI Lab (AI-LAB)
13. All Subjects :- ''')
                if s=="13":
                    ViewAllAttendance()
                else:
                    ViewAttendance(s)
                
            elif int(ch) == 5:
                roll = input("Enter Roll number :- ")
                ViewStudentRecord()
            elif int(ch) == 6:
                break
            else:
                print("Invalid Choice")
            