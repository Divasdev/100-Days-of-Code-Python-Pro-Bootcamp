student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
sum_scores = sum(student_scores)
print(sum_scores)

max_scores = 0
for score in student_scores:
    if score > max_scores:
        max_scores = score
print(max_scores)
