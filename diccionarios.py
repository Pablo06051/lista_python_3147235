pais1 = {
    "nombre":"colombia",
    "capital":"bogota",
    "moneda":"peso_colombiano",
    
    "ciudades" :[
                    "cordoba",
                    "bogota",
                    "medellin",
                ],
    "poblacion" :{
        "censo":46,
        "densidad":16,
        
    }
}
#acceder a la informacion del pais 
print (pais1["moneda"])
print(pais1["capital"])
print(pais1["ciudades"][1])
print("...")
# iterar las ciudades del pais uno
for ciudad in pais1["ciudades"]:
    print(ciudad)

print("censo:",
    pais1["poblacion"]["censo"],
    "millones de hab")
print("densidad:",
    pais1["poblacion"]["censo"],
    " por km2")

paises = [
    {
        "nombre": "venezuela",
        "capital": "caracas",
        "poblacion":
            {
            "censo": "213",
            "densidad": "25"
            },
        "ciudades": 
            [
            "maracaibo",
            "caracas",
            "valencia"
            ]
    },
    {
        "nombre": "argentina",
        "capital": "buenos aires",
        "poblacion": 
            {
            "censo": "45",
            "densidad": "16"
            },
        "ciudades": 
            [
            "buenos aires",
            "cordoba",
            "rosario"
            ]
    },
    {
        "nombre": "brasil",
        "capital": "brasilia",
        "poblacion": 
            {
            "censo": "212",
            "densidad": "25"
            },
        "ciudades": 
            [
            "salvador",
            "rio de janeiro",
            "curitiva"
            ]
    },
    {
        "nombre": "paraguay",
        "capital": "asuncion",
        "poblacion": 
            {
            "censo": "7.3",
            "densidad": "18"
            },
        "ciudades": 
            [
            "ciudad del este",
            "luque",
            "encarnacion"
            ]
    }
]
for pais in paises :
    print ("nombre:", pais  ["nombre"])
    print ("capital:", pais ["capital"])
    print("poblacion:")
    print("- censo :",
        pais ["poblacion"]["censo"],
        "millones")
    print ("densidad:",
        pais ["poblacion"]["densidad"],
        "por km2")
    print("......")
    for ciudad in pais ["ciudades"]:
        print("ciudad:", ciudad)
    print("......")



