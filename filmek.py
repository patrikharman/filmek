import Film


def beolvas():
    lista = []
    beFajl = open("film.txt","r",encoding="utf-8")
    beFajl.readline()
    soraim = beFajl.readlines()
    beFajl.close()
    for index in range(len(soraim)):
        tisztitottSor = soraim[index].strip()
        #print(tisztitottSor)
        daraboltSor = tisztitottSor.split(";")
        #print(daraboltSor)
        filmeim = Film.Film(daraboltSor[0],daraboltSor[1],daraboltSor[2],daraboltSor[3],daraboltSor[4])
        lista.append(filmeim)
    return lista

def kiiras(lista):
    for index in range(len(lista)):
        print(lista[index])

def minimumkereses(lista):
    index = 0
    legKisebb = 0
    while index < len(lista):
        if lista[index].perc < lista[legKisebb].perc:
            legKisebb = index
        index += 1
    print(f"A legrövidebb film: {lista[legKisebb].cim}")

def megSzamolas(lista):
    kiFajl = open("110perces.txt", "w", encoding="utf-8")
    db = 0
    for index in range(len(lista)):
        if int(lista[index].perc) >= 110:
            db += 1
    print(f"{db} film van ami legalább 110 perces")
    kiFajl.write(f"{db} film van ami legalább 110 perces")
    kiFajl.close()

def szineszek(lista):
    index = 0
    vanE = False
    szinesz = input("Kérem adjon meg egy színész nevet: ")
    for index in range(len(lista)):
        if szinesz == lista[index].foszereplo:
            vanE = True
            print(f"{lista[index].cim}")

    if vanE == False:
        print("Nincs ilyen a fájlban!")
