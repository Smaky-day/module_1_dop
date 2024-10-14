grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_1 = (sum(grades[0]) / len(grades[0]))
grades_2 = (sum(grades[1]) / len(grades[1]))
grades_3 = (sum(grades[2]) / len(grades[2]))
grades_4 = (sum(grades[3]) / len(grades[3]))
grades_5 = (sum(grades[4]) / len(grades[4]))
students_list = sorted(students)  # ашла функцию, кот. отсортированный список с рандомным положением имен, зато стабильный
print(students_list)  #  вывела для себя чтобы далее установить соттветствие
# нашла метод dict() - обратный для items
students_list_grades = [(students_list[0], grades_1), (students_list[1], grades_2), (students_list[2], grades_3), (students_list[3], grades_4), (students_list[4], grades_5)]
print(dict(students_list_grades))

