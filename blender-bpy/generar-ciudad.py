import bpy

class Terreno():
    '''
        
        Autor: <nicolaspauer20@gmail.com>
        Fecha: 13/09/2023
        
        Crea terrenos de una ciudad sobre un plano
        en blender haciendo uso del modulo bpy.
    ''' 
    
    def __init__(self, name, x_axis, y_axis):
        
        self.nombre = name
        
        self.x = x_axis
        
        self.y = y_axis
        
    def crear(self):
        '''
            Crea un terreno sobre el piso
        '''
        # Creo objeto
        bpy.ops.mesh.primitive_cube_add()
        terreno = bpy.data.objects['Cube']
        terreno.name = self.nombre
        # lo pongo sobre el piso
        terreno.location = (self.x, self.y, 1)
        # le doy una altura moderada
        terreno.scale[2] = 0.15
        
if __name__ == '__main__':
  # Agrego piso    
    bpy.ops.mesh.primitive_plane_add()
    piso = bpy.data.objects['Plane']
    piso.name = 'piso_de_ciudad'
  # Establezco posicion en la que ubicar el piso
    piso.location = (0, 0, 0)
  # Redimensiono ancho    
    piso.scale[0] = 8
  # Redimensiono largo    
    piso.scale[1] = 8   
  # Creo cuadras y otros terrenos
    terreno_1 = Terreno('Plaza', 0, 0)
    
    terreno_2 = Terreno('Casa.001', 0, 3)
    
    terreno_3 = Terreno('Edificio.001', 3, 3)
    
    terreno_4 = Terreno('Cuadra_plaza', 0, 0)
    
    terreno_5 = Terreno('Cuadra_residencial', 0, 3)
    
    terreno_6 = Terreno('Cuadra_comercial', -3, 0)
    
    terrenos = [terreno_1, terreno_2, terreno_3, terreno_4, terreno_5, terreno_6]
    
    for terreno in terrenos:
      # Creo terrenos
      terreno.crear()