from fake_math import divide as fake_divide
from true_math import divide as true_divide

first_number = 10 # произвольное число, например 10
second_number = 0 # деление на ноль

result_fake = fake_divide(first_number, second_number)
result_true = true_divide(first_number, second_number)

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)


print("Результат fake_divide:", result_fake) # Ожидаем 'Ошибка'
print("Результат true_divide:", result_true) # Ожидаем бесконечность