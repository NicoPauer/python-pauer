#!/usr/bin/python3
'''

 Autor: Nicolas Pauer 
 Mail: <nicolaspauer20@gmail.com>
 Fecha: 26/08/2023

Descripción:
 
 Permite analizar archivos csv buscando lineas donde 
 aparece determinada palabra para no leer todo y que te
 ardan los ojos.
 
''' 
# A partir de una palabra busca las lineas del archivo donde aparece y muestra tres columnas de datos(nombres en primera linea de csv)

import re, sys


def separar(n=1, c='*'):
	'''
	  Muestra n veces un caracter.
	'''
	caracteres = ''
	for iteracion in range(0, n):
		caracteres += c
	print(caracteres)	
# Defino variables a usar

archivo = open(sys.argv[1], 'r')
# Obtengo palabra a buscar en el archivo
separar(72, '°')
palabra = input('Ingrese termino de busqueda: ')
separar(72, ' ')
separar(72, '°')
# Muestro separador
separar(72, '-')
# Muestro fila de nombre de variables del csv
print(archivo.readline().replace(',','\t\t|\t'))
# Muestro seprador
separar(72, '-')
# Busco las lineas que matchean con la palabra y las muestro
for linea in archivo:
	if (re.search(palabra, linea)):
		print(linea.replace(',','\t|\t'))
		separar(72, '-')
# Cierro el archivo para que este disponible para la proxima
archivo.close()
sys.exit(0)
