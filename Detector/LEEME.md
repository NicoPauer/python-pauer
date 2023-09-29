##### (c) 2023, 29 de septiembre por Nico Pauer. Detector Pauer Py v1.7
---
# Detector de nuevos arhivos
Un script para detectar archivos agregados dentro de
una carpeta de un sistema GNU/Linux. licenciado
bajo licencia MIT, ver archivo 'LICENCIA.md'.
---
## Funcionamiento
Obtiene el nombre de una carpeta, lista
los nuevos archivos y agrega un listado
con los arhivos de la carpeta y sus
sub-carpetas en archivo 'anteriores.md'. 
### Algoritmo:
* obtener archivos en carpeta y guardar en lista 'arhivos_actuales'
* leer archivo 'anteriores.txt' y guardar en lista 'archivos_viejos'
* mostrar de 'archivos_actuales' los que no estén en 'archivos_viejos'
* almacenar 'archivos_actuales'  sin 'archivos_viejos' en 'anteriores.md'
---
#### Novedades:
* cambiado formato de texto plano a Mardown para mejor visualizacion del listado
* listado de sub-carpetas dentro de la que ingresa el usuario
* manejo de algunas excepciones que puedan ocurrir como nombre mal ingresado o encontrar archivo en vez
de carpeta
