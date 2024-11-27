## Importamos flask
from flask import Flask
## from flask_cors import CORS
app=Flask(__name__)

@app.route("/ecuacion")
@app.route("/ecuacion/<int:x>/<int:z>")


def ecuacion(x=0,z=0):
    y=((x*z)+(z+x))
    return f"<h1>El valor de y es : {y}</h1> <hr>"

if __name__ == '__main__':
    ## El valor True indica que la app se dejo en modo debug
    app.run(debug=True)
    
    

