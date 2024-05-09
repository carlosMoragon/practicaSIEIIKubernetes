from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

class RelojApp:
    def __init__(self):
        self.actualizar_horas()

    def obtener_hora_en_zona_horaria(self, zona_horaria):
        hora_actual_utc = datetime.utcnow()
        zona_horaria_objeto = pytz.timezone(zona_horaria)
        hora_en_zona_horaria = hora_actual_utc.astimezone(zona_horaria_objeto)
        return hora_en_zona_horaria.strftime("%Y-%m-%d %H:%M:%S %Z")

    def obtener_horas(self):
        hora_espana = self.obtener_hora_en_zona_horaria('Europe/Madrid')
        hora_eeuu = self.obtener_hora_en_zona_horaria('America/New_York')
        hora_china = self.obtener_hora_en_zona_horaria('Asia/Shanghai')
        return hora_espana, hora_eeuu, hora_china

    def actualizar_horas(self):
        self.hora_espana, self.hora_eeuu, self.hora_china = self.obtener_horas()

reloj = RelojApp()

@app.route('/')
def index():
    reloj.actualizar_horas()
    return render_template('index.html', hora_espana=reloj.hora_espana, hora_eeuu=reloj.hora_eeuu, hora_china=reloj.hora_china)

if __name__ == "__main__":
    app.run(debug=True)
