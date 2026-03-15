from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return {"message": "Hola Mundo desde Docker y Python!", "status": "OK"}

if __name__ == '__main__':
    # Render asigna un puerto dinámico mediante la variable de entorno PORT
    # Si no existe (como en tu PC local), usará el 5000 por defecto
    port = int(os.environ.get('PORT', 5000))
    
    # host='0.0.0.0' es obligatorio para que el contenedor escuche peticiones externas
    app.run(host='0.0.0.0', port=port)