
from flask import Flask
from flask import render_template #Usado para devolver cuando el usuario hace una petición
from flaskext.mysql import MySQL

#Esto se sabe de leer la documentación

app = Flask(__name__)
#Instanciamos (el nombre de mi app)
mysql = MySQL()


if __name__ == '__main__':
    app.run(debug=True) #El debug es para que nos muestre por consola errores
    