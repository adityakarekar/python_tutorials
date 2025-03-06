def calualte_avg_homework_grade(homework_grades):
    sum_grades=0
    for home_work in homework_grades.values():
        sum_grades+=home_work
    average_grade=round(sum_grades/len(homework_grades),2)
    return average_grade