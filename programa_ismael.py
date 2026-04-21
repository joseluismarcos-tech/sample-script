
    #Tarea 
#Asignamos una variable a una secuencia de nucleótidos y la llamamos secuencia 
#Esta secuencia es real del extremo Fw de una cadena de DNA secuenciada durante mi TFG
#DEPURACION FW
secuencia= """
TTATCGCAACTCTCTACTGTTTCTCCATACCCGTTTTTTT
GGGCTAGCAGGAGGAATTAACCATGCGCGTTAACAATGGTTTGACCCCGCAAGAACTCGA
GGCTTATGGTATCAGTGACGTACATGATATCGTTTACAACCCAAGCTACGACCTGCTGTA
TCAGGAAGAGCTCGATCCGAGCCTGACAGGTTATGAGCGCGGGGTGTTAACTAATCTGGG
TGCCGTTGCCGTCGATACCGGGATCTTCACCGGTCGTTCACCAAAAGATAAGTATATCGT
CCGTGACGATACCACTCGCGATACTTTCTGGTGGGCAGACAAAGGCAAAGGTAAGAACGA
CAACAAACCTCTCTCTCCGGAAACCTGGCAGCATCTGAAAGGCCTGGTGACCAGGCAGCT
TTCCGGCAAACGTCTGTTCGTTGTCGACGCTTTCTGTGGTGCGAACCCGGATACTCGTCT
TTCCGTCCGTTTCATCACCGAAGTGGCCTGGCAGGCGCATTTTGTCAAAAACATGTTTAT
TCGCCCGAGCGATGAAGAACTGGCAGGTTTCAAACCAGACTTTATCGTTATGAACGGCGC
GAAGTGCACTAACCCGCAGTGGAAAGAACAGGGTCTCAACTCCGAAAACTTCGTGGCGTT
TAACCTGACCGAGCGCATGCAGCTGATTGGCGGCACCTGGTACGGCGGCGAAATGAAGAA
AGGGATGTTCTCGATGATGAACTACCTGCTGCCGCTGAAAGGTATCGCTTCTATGCACTG
CTCCGCCAACGTTGGTGAGAAAGGCGATGTTGCGGTGTTCTTCGGCCTTTCCGGCACCGG
TAAAACCACCCTTTCCACCGACCCGAAACGTCGCCTGATTGGCGATGACGAACACGGCTG
GGACGATGACGGCGTGTTTAACTTCGAAGG"""

#Con print mostramos en pantalla el siguiente mensaje
print("Hola Ismael, vamos a tratar de trabajar alrededor de la secuencia:","\n", secuencia)

#Espacios para que quede estetico
print("")

#Debemos eliminar los \n que pueda haber si el formato es FASTA puesto que pueden interferir en nuestro codigo, para ello:
secuencia = secuencia.replace('\n', '')

print("Esta secuencia es Fw obtenida por secuenciacion en mi TFG y aun conserva parte del vector de clonacion en el que el gen se inserto.")
print("Trataremos de depurarla.")
print("Por las caracteristicas del vector de clonacion y las enzimas de restriccion usadas durante la ligacion sabemos que la parte correspondiente a vector termina en TTAACC por lo que hemos eliminado todo lo anterior a esto.")
print("")

#designamos la posicion en la que se empezara a leer la cadena, +6 para que no cuente los TTAACC en la posicion de inicio de lectura
inicio=secuencia.find("TTAACC")+6

#estoy sobreescribiendo la secuencia empezandola por la posicion de inicio justo cuando termina el vector para quitarlo de la misma
secuencia= secuencia[inicio:]
print("Asi la secuencia queda:",'\n',secuencia)
print("")

#DEPURACION RV
print("Lo logico seria hacer el alineamiento con la secuencia rv para obtener el gen completo, esta secuencia Rv es:")

secuencia_rv= """TCCGCCAAAACAGCCAAGCTTGCATGCCTGCAGGT
CGACTCTAGAGGATCCCCGGGTACCGAGCTCGAATTCTTACAGTTTCGGACCAGCCGCTA
CCAGCGCGGCACCCGCAGGGGTGTCGGTGTATTTATCGAAGTTGTCGATAAACAGTTTCG
CCAGGGTTTCGGCTTTTTCCTGCCACTGTTCCGGAGAAGCGTAGGTGTTACGCGGATCGA
GAATCTTCGTGTCTACGCCCGGCAGTTCGGTTGGGATCGCCAGGTTAAACATCGGCAGAG
TGAAGGTTTCTGCATTATCCAGCGAACCGTTGAGGATGGCGTCGATAATGGCGCGGGTAT
CTTTAATCGAGATACGTTTGCCAGTGCCGTTCCAGCCAGTGTTAACCAGATAAGCCTGCG
CGCCCGCCGCCTGCATACGTTTCACCAGCACTTCTGCGTACTGAGTCGGGTGCAGCGACA
GGAATGCCGCGCCGAAGCAAGCGGAGAAGGTTGGCGTCGGTTCGGTGATGCCACGCTCAG
TACCGGCCAGTTTGGCGGTGAAGCCAGAGAGGAAGTGATACTGGGTTTGATCGGCAGTCA
GGCGAGAAACCGGCGGCAACACGCCGAAAGCATCAGCAGTCAGGAAGATAACCTTAGTCG
CGTGGCCCGCTTTGGAAACCGGCTTAACAATGTTATCGATGTGATAGATCGGATAAGAAA
CGCGGGTGTTCTCGGTTTTTGAACCATCATCAAAGTCGATAGTGCCATCTTCACGCACGG
TGACGTTTTCCAGCAACGCATCACGACGGATAGCGTTGTAGATTTCAGGTTCCGCTTCTT
TCGACAGCTTGATAGTTTTTGCGTAGCAGCCGCCTTCGAAGTTAAACACGCCGTCATCGT
CCCAGCCGTGTTCGTCATCGCCAATC"""

print(secuencia_rv)
print("")

#Quitamos saltos de pagina y ponemos en formato lista
secuencia_rv = secuencia_rv.replace('\n', '')
secuencia_rv_ls= list(secuencia_rv)

#Reverso y complementario
#comando reversed para revertir
reversa = ''.join(reversed(secuencia_rv_ls))

lista_rev_comp=[]
#diccionario para poner el complementario
diccionario_del_complementario={
    'A':'T',
    'G':'C',
    'C':'G',
    'T':'A',}
#por cada nucleotido te los va cambiando en funcion del diccionario y añadiendo a la lista rev_comp
for nuc in reversa:
    lista_rev_comp.append(diccionario_del_complementario[nuc])
secuencia_rv_comp= "".join(lista_rev_comp)
print("La secuencia revertida y complementaria sera:", "\n", secuencia_rv_comp)
print("")

#Elliminamos el extremo del vector de la cadena rv
print("Depuramos nuevamente sabiendo en este caso que el vector de clonacion esta al final empezando por GAATTC")
final=secuencia_rv_comp.find("GAATTC")
secuencia_rv_comp= secuencia_rv_comp[:final]
print("La secuencia queda:", secuencia_rv_comp)
print("")

#ALINEAMIENTO
#Este codigo me costo que funcionara, los 6 ultimos nucleotidos de la secuencia Fw (secuencia[-6:]) te busca su posicion en la secuencia Rv para crear la secuencia completa entre el extremo fw + el extremo rv comenzando en la posicion buscada +6 para evitar los primeros 6 nucleotidos ya incluidos en Fw.
inicio=secuencia_rv_comp.find(secuencia[-6:])+6
secuencia_extremo2 = secuencia_rv_comp[inicio:]
secuencia_consenso= secuencia + secuencia_extremo2
print("He alineado ambas secuencias, de manera que la secuencia consenso queda:")
print(secuencia_consenso)
print("")
#Nuestra secuencia_consenso la llamaremos secuencia
secuencia=secuencia_consenso
#La guardamos
nombre_archivo = "sec_consenso.txt"
with open(nombre_archivo, 'w') as archivo:
    archivo.write(">secuencia1\n")
    archivo.write(secuencia)

#Algunos parámetros de la secuencia:
#Longitud de la cadena
longitud_cadena=len(secuencia)
print("Tu cadena tiene",longitud_cadena, "nucleotidos") 

#Tripletes y nucleotidos que quedan sueltos
tripletes= longitud_cadena//3
resto= longitud_cadena % 3
print("Esta organizada formando",tripletes, "tripletes") 

if resto == 1: 
    print("Aunque queda suelto", resto, "nucleotido")
if resto == 2: 
    print("Aunque quedan sueltos", resto, "nucleotidos")

#GC
contadorGC= 0
for cada_nucleotido in secuencia:
    if cada_nucleotido == "C" or cada_nucleotido =="G":
        contadorGC += 1
pGC= contadorGC/longitud_cadena*100
print("El porcentaje GC es:", pGC, "%")

print("")

#Transcripcion.
sec_transcrita = ""
for nucl in secuencia:
    if nucl == 'T':
        sec_transcrita += 'U'
    else:
        sec_transcrita += nucl

print("La secuencia transcrita a RNA es la siguiente:", sec_transcrita)
print("")

#Colocamos la secuencia en una lista con los nucleotidos de 3 en 3
print("Para trabajar mejor con la cadena, hare una lista con los nucleotidos de 3 en 3 y creare una secuencia separando los tripletes por espacios:")

#posiciones de los nucleotidos en la secuencia inicial
posicion_inicial=0
posicion_final=3
#Lista sin elementos donde vamos a ir añadiendo tripletes 
lista=[]
#el bucle va añadiendo a la lista los nucleotidos de 3 en 3, el contador de la posicion de los nucleotidos en la secuencia añadidos aumenta en 3 por cada vuelta
while posicion_final <= longitud_cadena:
    nucleotidos= secuencia[posicion_inicial:posicion_final]
    lista.append(nucleotidos)
    #para ver como se va generando la lista puedes quitar el # en la siguiente linea
    #print(lista) 
    posicion_inicial += 3
    posicion_final += 3
#los nucleotidos sobrantes al final se añaden en funcion de si sobraron 1 o 2
if resto == 1 :
    lista.append(secuencia[-1])
elif resto ==2 :
    lista.append(secuencia[-2:])

print("")
print("Lista:", lista)

#Secuencia en texto organizada en tripletes
secuencia_separada = " ".join(lista)
print("")

print("La secuencia queda:",secuencia_separada)

print("")

#Habrá codones de stop e inicio?

if("ATG" in secuencia_separada):
    if secuencia_separada.find("ATG") == 0:
        print("La secuencia transcrita comenzará por el codon de inicio")
    else: print("No habra codon de inicio al principio de nuestra secuencia transcrita,ERROR REVISA LA SECUENCIA")
if ("TAG" in secuencia_separada) or ("TAA" in secuencia_separada) or ("TGA" in secuencia_separada):
    print("La secuencia transcrita presentara codones de terminacion")
else: print("No habra codones de terminacion en nuestra secuencia transcrita,ERROR REVISA LA SECUENCIA")
print("")

#Diccionario de tripletes a aminoacidos
codigo_genetico = {
    'TTT': 'F',
    'TTC': 'F',
    'TTA': 'L',
    'TTG': 'L',
    'TCT': 'S',
    'TCC': 'S',
    'TCA': 'S',
    'TCG': 'S',
    'TAT': 'Y',
    'TAC': 'Y',
    'TAA': '_STOP_',
    'TAG': '_STOP_',
    'TGT': 'C',
    'TGC': 'C',
    'TGA': '_STOP_',
    'TGG': 'W',
    'CTT': 'L',
    'CTC': 'L',
    'CTA': 'L',
    'CTG': 'L',
    'CCT': 'P',
    'CCC': 'P',
    'CCA': 'P',
    'CCG': 'P',
    'CAT': 'H',
    'CAC': 'H',
    'CAA': 'Q',
    'CAG': 'Q',
    'CGT': 'R',
    'CGC': 'R',
    'CGA': 'R',
    'CGG': 'R',
    'ATT': 'I',
    'ATC': 'I',
    'ATA': 'I',
    'ATG': 'M',
    'ACT': 'T',
    'ACC': 'T',
    'ACA': 'T',
    'ACG': 'T',
    'AAT': 'N',
    'AAC': 'N',
    'AAA': 'K',
    'AAG': 'K',
    'AGT': 'S',
    'AGC': 'S',
    'AGA': 'R',
    'AGG': 'R',
    'GTT': 'V',
    'GTC': 'V',
    'GTA': 'V',
    'GTG': 'V',
    'GCT': 'A',
    'GCC': 'A',
    'GCA': 'A',
    'GCG': 'A',
    'GAT': 'D',
    'GAC': 'D',
    'GAA': 'E',
    'GAG': 'E',
    'GGT': 'G',
    'GGC': 'G',
    'GGA': 'G',
    'GGG': 'G',
}

#Paso de tripletes a aminoacidos en forma de lista
lista_traduccion=[]
contadordetripletes=0
parada=tripletes-2
while contadordetripletes <= parada:
        traduccion = codigo_genetico[lista[contadordetripletes]]
        lista_traduccion.append(traduccion)
        contadordetripletes +=1
print("La lista de aminoacidos seria:","\n", lista_traduccion)
print("")

#Formato texto 
peptido= ("".join(lista_traduccion))
print("En formato FASTA quedaria:", "\n", ">peptido1", "\n", peptido)

#Guardamos la cadena en formato txt
nombre_archivo = "resultado_traduccion.txt"
with open(nombre_archivo, 'w') as archivo:
    archivo.write(">peptido1\n")
    archivo.write(peptido)

print("")
print('Se guardo en formato .txt un archivo FASTA con la secuencia consenso y otro con la secuencia de aminoacidos') 