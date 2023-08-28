#!/usr/bin/python3
'''

Autor:

 <nicolaspauer20@gmail.com> del 27/08/2023 al 27/08/2023. 

Descripción:

Hace recomendaciones basado en una palabra y un grupo de 
características suministradas por el usuario.

Dependencias:

 - Python v3
 
 - módulo Python v3: re
 
Licenciado bajo licencia MIT:

Copyright 2023 Nicolás Pauer

Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software. EL SOFTWARE SE PROPORCIONA "COMO ESTÁ", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.
'''
import re

def mostrar(cadena_csv):
	'''
		Muestra en una tabla una cadena
		de valores separados por comas.
	'''
	# Muestro valores en formato legible
	print('({})'.format(cadena_csv.replace(',', ') (')))
	# Muestro separador
	separadores = ''
	for separador in range(0, 80):
		separadores += '-'
	print(separadores)	
	
def encontrar(buscada, descripcion) -> list:
	'''
		Devuelve una lista de cadenas de texto con recomendaciones
		encontradas en el archivo "recomendaciones.csv".
	'''
	# Defino lista de posibles concidencias para la busqueda
	resultados = []
	datos = open('recomendaciones.csv', 'r')
	lineas = datos.readlines()
	# Muestro primera fila que tiene nombre de los datos de las columnas
	mostrar(lineas[0])
	# Agrego si tiene algo de lo solicitud	
	for linea in lineas:
		# Busco coincidencias en termino de busqueda a descripcion  	
		if (re.match(buscada, linea) or re.search(descripcion, linea)):
			resultados.append(f'{linea} Encontrada para "{buscada}" o "{descripcion}".')
	# Cierro archivo porque ya no lo necesito y se pueda seguir usando
	datos.close()		
	# Devuelvo lista de coincidendias 
	return resultados	
	
if __name__ == '__main__':
  # Programa principal, obtiene datos y busca en el archivo
	palabra = input('Termino de busqueda: ')
	caracteristicas = input('Nombre algunas caracteristicas: ')
  # Muestro resultado de las lineas que coinciden con la busqueda
	for coincidencia in encontrar(palabra, caracteristicas):
		mostrar(coincidencia)
