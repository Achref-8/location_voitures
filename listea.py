liste = ['azerty', 'ferst', 'hert', 'atery', 'hagdte', 'acheter']
liste2 = ['azerty', 'ferst', 'hert', 'atery', 'hagdte', 'acheter']

for i in range(0,len(liste2)):
    if liste2[i][0] =='a':
        liste.remove(liste2[i])
print(liste)