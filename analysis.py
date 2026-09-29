def marks_obtained(marks):
    total = 0
    for a in marks.values():
         total =total+a
    return total

def average(marks):
    totalmark=int(input("Maximum number of marks a student can score in one subject:"))
    totalmarks=len(marks)*totalmark
    total = marks_obtained(marks) 
    average =total/len(marks)
    percentage = total*100/totalmarks
    average_data={
        "average": average,
        "Percentage": percentage,
        "totalmark": totalmark
    }
    return average_data

def failed_subjects(marks,totalmark):
    failed=[]
    for subjects,mark in marks.items():
        if mark < totalmark*40/100:
            failed.append(subjects)
    return failed

def highest_marks(marks):
    highest=max(marks.values())
    for subjects,mark in marks.items():
        if mark == highest:
            return subjects,highest


def lowest_marks(marks):
    lowest=min(marks.values())
    for subjects,mark in marks.items():
        if mark == lowest:
            return subjects,lowest

def grade(percentage):
    if percentage>=90:
        sgrade="S"
    elif percentage>=80:
        sgrade="A"
    elif percentage>=70:
            sgrade="B"
    elif percentage>=60:
            sgrade="C"
    elif percentage>=50:
            sgrade="D"
    elif percentage>=40:
            sgrade="E"
    else:
         sgrade="F"
    return sgrade

def final_result(failed):
     if len(failed)==0:
          return "Pass"
     else:
          return "Fail"
          
