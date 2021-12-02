
from flask import Flask
from flask import render_template #Usado para devolver cuando el usuario hace una petición
from flaskext.mysql import MySQL

#Esto se sabe de leer la documentación

app = Flask(__name__)
#Instanciamos (el nombre de mi app)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '3085'
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app) #inicio la DB

@app.route('/')

def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql="insert into empleados (nombre, correo, foto) values ('Juan', 'juan@email.com', 'fotoJuan.jpg');"

    cursor.execute(sql)

    conn.commit()

    return render_template('empleados/index.html')

if __name__ == '__main__':
    app.run(debug=True) #El debug es para que nos muestre por consola errores
    