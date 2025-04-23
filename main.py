from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    respuesta = ""
    if request.method == "POST":
        idioma = request.form["idioma"].lower()
        texto = request.form["texto"]
        
        if idioma == "español":
            if "define" in texto.lower():
                respuesta = "Esta es una respuesta clara y natural, fácil de entender y lista para entregar."
            elif "ensayo" in texto.lower() or "escribe" in texto.lower():
                respuesta = "Ensayo: Párrafo estructurado con argumentos, claridad y un tono humano limpio."
            else:
                respuesta = "Desarrollo general: explicación estilo humano, sin frases robóticas."
        elif idioma == "inglés":
            if "define" in texto.lower():
                respuesta = "This is a clear and natural answer, easy to edit and ready to submit."
            elif "essay" in texto.lower() or "write" in texto.lower():
                respuesta = "Essay: Structured paragraph with arguments, clarity and a clean human tone."
            else:
                respuesta = "General development: human-style explanation, no robotic phrases."
        else:
            respuesta = "Idioma no reconocido. Por favor escribe 'español' o 'inglés'."
    
    return render_template("index.html", respuesta=respuesta)

app.run(host="0.0.0.0", port=81)
