list_one = input("Введите через пробел первый список чисел:  ").split()
list_two = input("Введите через пробел второй список чисел:  ").split()

print(f"\nПервый список:  {list_one}")
print(f"Второй список:  {list_two}\n")

for i in list_one.copy():
    if i in list_two:
        list_one.remove(i)

print(f"Элементы первого списка, которых нет во втором:  {list_one}")
