numbers = input("Введите любые цифры через запятую, либо через ';' либо '/':  ")
numbers = numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()

unique_numbers = []
for i in numbers:
    if numbers.count(i) == 1:
        unique_numbers.append(i)

print(f"\nВведенные элементы:  {numbers}")
print(f"Уникальные элементы:  {unique_numbers}")
