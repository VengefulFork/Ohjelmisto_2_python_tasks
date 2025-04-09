from flask import Flask, request

app = Flask(__name__)
@app.route('/prime/<number>')

def prime (number) :
    lippu = True
    args = request.args
    num = int(number)
    if num > 1:
            for i in range(2, num //2):
                    if (    num % i) == 0:
                            lippu = False
    if lippu :
        response = {
            "Number" : num,
            "isPrime": True
        }
    else :
        response = {
            "Number" : num,
            "isPrime" : False
        }
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)