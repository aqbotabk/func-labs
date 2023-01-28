print("Имя:")
name=input()
print("Фамилия:")
surname=input()
print("Дисциплина=")
subject=input()
print("Итоговый балл=")
grade=int(input())
if grade>100:
    print("error")
elif grade>=95:
    gpa=4.00
elif grade>=90:
    gpa=3.67
elif grade>=85:
    gpa=3.33
elif grade>=75:
    gpa=2.67
elif grade>=70:
    gpa=2.33
elif grade>=65:
    gpa=2.00
elif grade>=60:
    gpa=1.67
elif grade>=55:
    gpa=1.33
elif grade>=50:
    gpa=1.00
elif grade<50:
    gpa=0.00
print("Здравствуйте, ", surname, name, ". Ваш gpa по дисциплине",subject,"=",gpa)