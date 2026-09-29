from validation import valid_marks

def student():
    name=str(input("Enter the student name:"))
    registration_number=input("Enter students Registration Number:")
    marks={}
    n=int(input("Enter the number of subjects enrolled in this semester:"))
    for i in range(1,n+1):
        subject=input("Enter the subject name:")
        mark=float(input("Enter the marks:"))
        while not valid_marks(mark):
            print("Invalid marks Entered")
            mark=float(input("Enter the marks again:"))

        marks[subject]=mark
    data={
        "name":name,
        "Registration Number":registration_number,
        "marks":marks,
        }
    return data

def multiple_students():
    student_data = []

    x=int(input("Enter the number of students:"))

    for i in range(x):
        print("Enter students details",i+1)
        data = student()
        student_data.append(data)

    return student_data