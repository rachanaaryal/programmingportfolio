
'''this program take the required number of 
students and giives how many groups can be formed'''

students = int(input("how many students? "))
group = int(input("required group size? "))

full_group = students // group
left_over = students%group

group_word = "group" if full_group == 1 else "groups"
student_word = "student" if left_over == 1 else "students"

print(f"there will be {full_group} {group_word} with {left_over} 11{student_word} left over.")

