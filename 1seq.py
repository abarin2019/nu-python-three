size_list = int(input('Введите количество элементов:  '))
num_list = []

for i in range(size_list):
    num_list.append(int(input(f'Введите {i+1} элемент:  ')))

num_list.sort()
print(num_list)
