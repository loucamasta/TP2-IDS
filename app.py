from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

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

@app.route("/registration")
def registration():
    return render_template("registration.html")

if __name__ == "__main__":
    app.run("127.0.0.1", port="5001", debug=True)
