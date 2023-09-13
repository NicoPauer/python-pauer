import bpy


if (__name__ == '__main__'):
    # Muevo si no alcanza posicion maxima sino la reinicio
    if (bpy.data.objects['Plane'].location[1] > -4):
      # Desplazo posicion de objeto en eje y    
        bpy.data.objects['Plane'].location[1] += -0.9
    else:
      # Inicio posición desde eje y = 3    
        bpy.data.objects['Plane'].location[1] = 3  