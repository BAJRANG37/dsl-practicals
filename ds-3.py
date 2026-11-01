# Sample list of Employee Salaries
salaries = [45000.0, 38000.5, 52000.75, 61000.0, 47000.0, 70000.0, 56000.0, 49000.5]

#------a) Selection Sort------
def selection_sort(sal_list):
    n = len(sal_list)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if sal_list[j] < sal_list[min_index]:
                min_index = j
        sal_list[i], sal_list[min_index] = sal_list[min_index], sal_list[i]
    return sal_list


#------b) Bubble Sort------
def bubble_sort(sal_list):
    n = len(sal_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sal_list[j] > sal_list[j + 1]:
                sal_list[j], sal_list[j + 1] = sal_list[j + 1], sal_list[j]
    return sal_list


#------Run both sorts & display top 5 salaries------
# Using selection sort
sorted_salaries = selection_sort(salaries.copy())
print(sorted_salaries)
print("Top 5 salaries (Selection Sort):", sorted_salaries[-5:][::-1])

# Using bubble sort
sorted_salaries = bubble_sort(salaries.copy())
print(sorted_salaries)
print("Top 5 salaries (Bubble Sort):", sorted_salaries[-5:][::-1])
