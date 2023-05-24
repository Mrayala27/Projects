with open('./text.txt','w+') as file:
    for line in file:
        print(line)
    file.write('una linea mas para el archivo')
    file.write('una linea mas para el archivo\n')
    file.write('\n una linea mas para el archivo')
