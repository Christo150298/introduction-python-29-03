id = 0

products_table = []

insert_into = lambda item, table: table.append(item)

class Product:
    def __init__(self, name, description, category, brand):
        global id
        id += 1
        self.id = id
        self.name = name
        self.description = description
        self.category = category
        self.brand = brand

    #DESPUES DE DEFINIR  __init__ PODEMOS DEFINIR MAS MÉTODOS
    def create(self):
        insert_into(self, products_table)

fregona = Product(
    name="Fregona de microfibra", 
    description="""Fregroma de microfibra para mejor capacidad de absorcion.
    Suelos y superficies limpias y secas en tiempo record""", 
    category="Productos de limpieza", 
    brand="Mileda"
)

print("First: ", products_table)

fregona.create()

print("Second: ", products_table)

