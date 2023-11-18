# link: https://www.math.tecnico.ulisboa.pt/~ccal/python/ex0{k}.html

with open('links.txt', 'w') as txt:
    for i in range(1,7):
        txt.write(f'https://www.math.tecnico.ulisboa.pt/~ccal/python/ex0{i}.html\n')