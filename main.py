f = open('scientist.txt').read()
f = f.split('\n')
a = []
for i in f:
    a.append(i.split('#'))
for el in a:
    if 'Аллопуринол' in el[1]:
        print('Разработчиками Аллопуринола были такие люди (результаты выведите в порядке возрастания даты):' + el[0])
x = []
for el in a:
    if 'Аллопуринол' in el[1]:
        x.append(el[2])
data = min(x)
for el in a:
    if data in el[2]:
        print('Оригинальный рецепт принадлежит:' + el[0])