totalLines = int(input('Number of lines: '))

for line in range(1, totalLines + 1):
    print('') #Prin break line
    
    spaces = totalLines - line
    totalStar = line + (line-1)

    for space in range(1, spaces + 1):
        print(' ', end = '') #Print front space

    for star in range(1, totalStar + 1):
        print('*', end = '') #Print stars