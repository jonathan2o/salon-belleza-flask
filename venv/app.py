from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/cita', methods=['POST'])
def cita():
    nombre = request.form['nombre']
    telefono = request.form['telefono']
    fecha = request.form['fecha']
    hora = request.form['hora']

    return f"✅ Cita agendada para {nombre} el {fecha} a las {hora}. Tel: {telefono}"

if __name__ == '__main__':
    app.run(debug=True)
