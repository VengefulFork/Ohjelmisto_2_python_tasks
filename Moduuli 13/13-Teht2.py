from flask import Flask, request
import mariadb

connection = mariadb.connect(
        host='localhost',
        port= 3306,
        database= 'flight_game',
        user= 'flightuser',
        password= '1234',
        autocommit=True
)

app = Flask(__name__)

@app.route('/search/<icao>')



def search (icao) :
    sql = f"SELECT name, municipality FROM airport where ident = '{icao}'"
    curs = connection.cursor()
    curs.execute(sql)
    result = curs.fetchall()

    response = {
        "ICAO" : icao,
        "Name" : result[0][0],
        "Municipality" : result[0][1]
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)