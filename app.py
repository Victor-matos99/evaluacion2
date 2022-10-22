# app.py
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

def _find_next_id():
    return max(country["id"] for country in countries) + 1

@app.get("/countries")
def get_countries():
    return jsonify(countries)

@app.get("/clientes")
def get_mysql():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        port="3306",
        user="root",
        password="example",
        database="examen"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'id': result[0], 'nombre': result[1], 'apellido': result[2],  'telefono': result[3],  'direccion': result[4],  'email': result[5],  'ciudad': result[6],  'estado': result[7],  'Codigo Postal': result[8]}
        registro_json.append(registro)
        registro = {}

    return jsonify(registro_json)

@app.get("/productos")
def productos():
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        port="3306",
        user="root",
        password="example",
        database="examen"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM productos")
    myresult = mycursor.fetchall()
    registro_json = []
    registro = {}
    for result in myresult:
        registro = {'id': result[0], 'descripcion': result[1], 'cantidad_disponible': result[2],  'costo': result[3],  'precio': result[4]}
        registro_json.append(registro)
        registro = {}

    return jsonify(registro_json)



@app.get("/facturas")
def facturas():
    name = request.args.get('id')
    mydb = mysql.connector.connect(
        #host="mysql-db-1",
        host="db",
        port="3306",
        user="root",
        password="example",
        database="examen"
        )
    mydb.set_charset_collation('latin1')
    mycursor = mydb.cursor()
    if name is None:
        mycursor.execute("SELECT * FROM facturas")
        myresult = mycursor.fetchall()
        registro_json = []
        registro = {}
        for result in myresult:
            registro = {'id': result[0], 'id producto': result[1], 'cantidad': result[2],  'subtotal': result[3],  'IVA': result[4],  'total': result[5],  'cliente_id': result[6],  'registro_id': result[7]}
            registro_json.append(registro)
            registro = {}
        return jsonify(registro_json)
    else:
        mycursor.execute("SELECT * FROM facturas where factura_id = " + name)
        myresult = mycursor.fetchall()
        registro_json = []
        registro = {}
        for result in myresult:
            registro = {'id': result[0], 'id producto': result[1], 'cantidad': result[2],  'subtotal': result[3],  'IVA': result[4],  'total': result[5],  'cliente_id': result[6],  'registro_id': result[7]}
            registro_json.append(registro)
            registro = {}
        return jsonify(registro_json)




@app.post("/clientes")
def post_mysql():
    if request.is_json:
        registro = request.get_json()
        sql = "insert into clientes values ('" + registro['id'] + "','" + registro['nombre'] + registro['apellido'] + registro['telefono'] + registro['email']+ registro['direccion'] + registro['ciudad'] + registro['estado'] + registro['cp'] + ");"
        mydb = mysql.connector.connect(
            #host="mysql-db-1",
            host="localhost",
            port="3306",
            user="root",
            password="example",
            database="prueba"
        )
        mycursor=mydb.cursor()
        mycursor.execute(sql)

        return sql



    return "no",402

@app.route('/hello', methods = ['GET'])
def hello():
    name = request.args.get('name')
    if name is None:
        text = 'Hello!'
    else:
        text = 'Hello ' + name + '!'
    return jsonify({"message": text})

@app.post("/countries")
def add_country():
    if request.is_json:
        country = request.get_json()
        country["id"] = _find_next_id()
        countries.append(country)
        return country, 201
    return {"error": "Request must be JSON"}, 415
