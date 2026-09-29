from student import multiple_students
from analysis import marks_obtained,average,failed_subjects,highest_marks,lowest_marks,grade,final_result

#Average contains student average as well as percentage
students_data=multiple_students()
for student_data in students_data:
       marks=student_data["marks"]
       total=marks_obtained(marks)
       result=average(marks)
       failed=failed_subjects(marks,result["totalmark"])
       top=highest_marks(marks)
       low=lowest_marks(marks)

       print("-----Students Performamce-----")
       print("student name:",student_data["name"])
       print("Registration Number:",student_data["Registration Number"])
       print("Number of Subject Registered:",len(marks))

       for subject in marks:
              print(subject,end="  ")
       print()

       print("Total marks obtained in all the subjects registered  by the student",total)
       print("Average:",result['average'])
       print("Percentage obtained by the student:",result["Percentage"])
       print("Subjects that student failed in ",failed)
       print("Highest marks:",top)
       print("Lowest marks:",low)

       student_grade=grade(result["Percentage"])
       print("Grade Obtained:",student_grade)

       output=final_result(failed)
       print("Overall Result:",output)