from flask import Flask, render_template, redirect, url_for, request, redirect
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_DEFAULT_SENDER'] = 'your-email@gmail.com'
mail = Mail(app)

info_evento = {
        "nombre": "Rally MTB 2025",
        "organizador": "Club Social y Deportivo Unidos por el Deporte",
        "descripcion": (
        "El evento se desarrollará en la ciudad de Tandil, Buenos Aires, organizado por nuestro club, "
        "el día 24 de Octubre de 2025 a las 8:00 AM. Existen dos modalidades corta y larga, "
        "la primera es de 30km y la segunda de 80km."
        ),
        "fecha": "24 de Octubre de 2025",
        "horario": "8:00 AM",
        "lugar": "Tandil, Buenos Aires",
        "tipo_carrera": "MTB rural",
        "modalidad_costo": {
            1: {"nombre": "Corta", "valor": "100"},
            2: {"nombre": "Larga", "valor": "200"}
        },
        "auspiciantes": ["Ausp1", "Ausp2", "Ausp3"]
}

@app.route("/")
def index():
    return render_template("index.html", info_evento=info_evento)

@app.route("/registration", methods=["GET", "POST"])
def registration():
   if request.method == "POST": 
        nombre = request.form["nombre"]
        email = request.form["email"]
        modalidad = request.form["modalidad"]

        
        return render_template("registration.html", mensaje="Inscripción enviada correctamente")
   return render_template("registration.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)