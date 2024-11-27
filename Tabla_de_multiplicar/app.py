## Importamos flask
from flask import Flask
app=Flask(__name__)

@app.route("/")
@app.route("/<int:x>")

def ecuacion(x=0,i=0):
    ## Crear lista para almacenar resultados r = []
    r = []
    for i in range (1,11):
        m = i*x
        
        ## Agregar los resultados a la lista
        r.append(f"{i} x {x} = {m}") 
        ## Convertimos la lista de resultados en una cadena HTML con formato
        r_html = "<br>".join(r)
        
    return f"<h1> Tabla de multiplicar del {x} <h1> <hr><p>{r_html}</p>"

if __name__ == '__main__':
    ## El valor True indica que la app se dejo en modo debug
    app.run(debug=True) 
