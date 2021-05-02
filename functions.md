# Grading Student Based on Marks Obtained by Making Functions and prints it

```def ave(marks):
    numsubj = len(marks)
    totalmarks = sum(marks)
    aveofmarks = totalmarks / numsubj
    return aveofmarks
    
def grades(aveofmarks):
    if aveofmarks >= 80:
        grade = 'A'
    if aveofmarks >=50:
        grade = 'B'
    else:
        grade = 'C'
        
    return grade
        
marks = [55,64,75,80,65]

aveofmarks = ave(marks)
grade = grades(aveofmarks)

print(aveofmarks)
print(grade)```



    
