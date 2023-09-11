# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
# https://www.youtube.com/watch?v=R4F4xwpBtZg

def countStudents(students, sandwiches):
    # use to break while loop
    # st = [1,1,1]
    # sa = [0,1,1]
    # it will loops forever
    student_unable_to_eat = 0

    while students and sandwiches:

        # st = [0,1,0]
        # sa = [0,1,1]
        # ==> pop both stack
        # st = [1,0]
        # sa = [1,1]
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            student_unable_to_eat = 0  # update
        else:

            # st = [1,1,0]
            # sa = [0,1,1]
            # ==> pop st and append
            # st = [1,0,1]
            # sa = [0,1,1]
            first_student = students.pop(0)
            students.append(first_student)
            student_unable_to_eat += 1

            if student_unable_to_eat == len(students):
                break

    return student_unable_to_eat


students_list = [1, 1, 1, 0, 0, 1]
sandwiches_list = [1, 0, 0, 0, 1, 1]

print(countStudents(students_list, sandwiches_list))
