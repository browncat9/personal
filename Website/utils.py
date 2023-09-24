#calculations for the website

from .models import Config, db

# Initialize variables of module taken in semester and weighted credit for each module
total_module_taken_this_sem = 0
total_weighted_credit_module = 0.0

# Define a function to calculate GPA for a given mark
def marks_gpa(module_mark):

   # if module_mark == "W":
       # return 0.0
    try:
        module_mark = float(module_mark)
    except ValueError:
        return 0.0

    if module_mark >= 70 and module_mark <= 100:
        return 4.0
    elif module_mark >= 60 and module_mark <= 69:
        return 3.0
    elif module_mark >= 50 and module_mark <= 59:
        return 2.0
    elif module_mark >= 40 and module_mark <= 49:
        return 1.0
    else:
        return 0.0

   
  
    
        
def cumulative_gpa(student_id):
    gpa = 0.0
    total_module_taken = 0
    total_weighted_credit = 0.0
    for module_gpa in Config.query.filter_by(student_id = student_id):
        gpa = module_gpa.gpa
        if gpa != 0.0:
            total_module_taken += 1
            total_weighted_credit += gpa
    if total_module_taken == 0:
        gpa = 0.0
    else:
        gpa = total_weighted_credit / total_module_taken
    return round(gpa,2)
    

#def semester_gpa_compare(student_id):
    

## Sample list of grades (you should replace this with your actual grades)
#grades = [85, 72, 95, "W", 58]
#
#for grade in grades:
#    gpa = marks_gpa(grade)
#    if grade != "W":
#        total_module_taken_this_sem += 1
#        total_weighted_credit_module += gpa
#
## Calculate GPA
#if total_module_taken_this_sem == 0:
#    gpa = 0.0  # Avoid division by zero
#else:
#    gpa = total_weighted_credit_module / total_module_taken_this_sem
#
## Calculate the modified GPA by multiplying it by 0.8
#modified_gpa = gpa * 0.8
#
#print(f"Total Module taken this semester: {total_module_taken_this_sem}")
#print(f"GPA: {gpa:.2f}")
#print(f"Modified GPA (multiplied by 0.8): {modified_gpa:.2f}")
#
## Example: Previous semester's GPA (you should replace this with the actual previous semester's GPA)
#previous_semester_gpa = 3.5
#
## Compare the modified GPA with the previous semester's GPA
#if modified_gpa <= previous_semester_gpa:
#    print("Alert: Your modified GPA is equal or less than the previous semester's GPA.")
