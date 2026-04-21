#!/bin/bash

#Hace una carpeta para filtrar nuestro archivo
mkdir filtros

#Creamos un archivo que elimine las primeras lineas aclaratorias y tome solo las columnas 1 a 5
grep -v '^#' GRCh38_latest_clinvar.vcf | awk '{print $1, $2, $3, $4, $5}' > filtros/archivo_sin_encabezados.txt 

#Creamos un archivo con la columna 8 y que separe por tabulaciones toda la informacion en vez de con ;
grep -v '^#' GRCh38_latest_clinvar.vcf | awk '{print $8}' | sed 's/;/\t/g' > filtros/mas_info.txt 

#Unimos la informacion de los dos archivos anteriores en un archivo final al que hemos eliminado la informacion inservible
paste filtros/archivo_sin_encabezados.txt filtros/mas_info.txt > filtros/archivo_final.txt

#Con el archivo generado podemos trabajar, por ejemplo, contando el numero de variantes por cromosoma:
awk '{print $1}' filtros/archivo_final.txt | uniq -c > filtros/conteo_variantes_por_cromosoma.txt

#Aunque tambien podemos imprimir lo mismo a partir del archivo original 
echo 'Aqui tienes el numero de variantes que ha experimentado cada cromosoma:'
(echo "Variantes Cromosomas" && grep -v '^#' GRCh38_latest_clinvar.vcf | awk '{print $1}'| uniq -c) 

#Por ultimo vamos a estudiar las variaciones que provocan enfermedades, vamos a seleccionar solo la informacion mas relevante, organizarlas en columnas tabuladas y eliminar identificadores que no hacen falta
grep -i 'CLNSIG=Pathogenic' filtros/archivo_final.txt | awk '{print $1, $2, $3, $4, $5, $8, $12}'| sed 's/CLNDN=//g' | sed 's/CLNVC=//g' | sed 's/ /    /g' > filtros/m_patogenicas.txt

#Para probar if podemos hacer que si se genero el archivo anterior me imprima una frase 
if [ -s "filtros/m_patogenicas.txt" ]; then
    echo "Se han filtrado con exito las mutaciones que provocan alguna enfermedad y su informacion mas relevante."
fi
