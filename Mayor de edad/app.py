## Importamos flask
from flask import Flask
app=Flask(__name__)

## Definimos la ruta principal
@app.route("/")
def HolaFlask():
    return "<h1>¡Hola Flask!</h1><hr>"

## Ahora tomamos la tercer ruta y la reemplazamos por 
## el siguiente ejemplo 2.) Haga un programa que al 
## capturar la edad de una persona diga si es:
## Menor de edad (Menor a 18 años)
## Adulto (Mayor o igual a 18 años y menor a 60 años)
## Adulto mayor (Mayor o igual a 60 años)

@app.route("/edades")
@app.route("/edades/<int:edad>")

def edades(edad=0):
    if edad<18:
        R='menor de edad'
    elif(edad<60):
        R='Adulto'
    else:
        R='Adulto mayor'
    return f"<h1>La persona es : {R}</h1> <hr>"


if __name__ == '__main__':
    ## El valor True indica que la app se dejo en modo debug
    app.run(debug=True)
    
    

