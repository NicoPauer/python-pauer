#!/usr/bin/python3

import os

def obtenerArchivos(carpeta='/home/'):
	'''
		Devuelve una lista de archivos con los
		nombres de todos los archivos y carpetas
		de la que recibe como parametro, por
		defecto lista archivos de la carpeta
		de las carpetas personales de usuario.
	'''
	ficheros = set(os.listdir(carpeta))
	
	auxiliar = set()
	
	for fichero in ficheros:
	# Lista cada una de las subcarpetas de la carpeta	
		auxiliar.add(fichero)
		try:
			# Puede ocurrir el error que no sea directorio	
			for interno in set(os.listdir(carpeta + fichero)):	
				auxiliar.add(carpeta + fichero + '/' + interno)
		except:
			# Si surge esta excepcion solo cambio la forma de nombrarlo
			auxiliar.add(carpeta + fichero)	
		
	ficheros = auxiliar
		
	return ficheros

		
def almacenarListado(archivo, listado):
	'''
		Guarda en archivo que recibe como 
		parametro un listado de cadena de
		texto.
	'''
	
	archivador = open(archivo, 'a')
	
	archivador.write('# Listado de directorios y archivos nuevos\n')
	
	for nombre in listado:
		archivador.write('* ' + nombre + '\n')	
		
	archivador.close()	

nombre_carpeta = input('\nIngrese nombre de carpeta: ')

while (nombre_carpeta == '' or nombre_carpeta[0] != '/' or nombre_carpeta[len(nombre_carpeta) - 1] != '/'):
	# Mientras no tenga un nombre de carpeta valido para GNU/Linux revalido la entrada
	nombre_carpeta = input('\n\tnombre "{}" incorrecto.\n\n  * Ingrese un nombre de carpeta valido para GNU/Linux: '.format(nombre_carpeta))
	
archivos_actuales = set(obtenerArchivos(nombre_carpeta))

archivos_viejos = set()

with open('anteriores.md', 'r') as viejos:
	archivos_viejos = set(viejos.readlines())

auxiliar = set()

for nombre in archivos_viejos:
	auxiliar.add(nombre.replace('\n', '').replace('* ', '')) 

archivos_viejos = auxiliar

print('\nLos archivos nuevos son:\n')

for nuevo in archivos_actuales.difference(archivos_viejos):
	print('\t* ', nuevo)

almacenarListado('anteriores.md', archivos_actuales.difference(archivos_viejos))
