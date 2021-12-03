
from flask import Flask
from flask import render_template, request, redirect #Usado para devolver cuando el usuario hace una petición
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

    sql="SELECT * FROM empleados;"

    cursor.execute(sql)

    empleados = cursor.fetchall()

    conn.commit()

    return render_template('empleados/index.html', empleados=empleados)

@app.route('/create')
def create():
    return render_template('empleados/create.html')

@app.route('/store', methods=["POST"]) #Debo aclararlo porque sino queda como un GET
def store():
    _nombre = request.form['txtNombre']
    _correo = request.form['txtCorreo']
    _foto = request.files['txtFoto']

    sql = "INSERT INTO empleados (nombre, correo, foto) values (%s, %s, %s);"
    datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True) #El debug es para que nos muestre por consola errores
    