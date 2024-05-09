import datetime
import pytz

def obtener_fecha_en_paises():
    
    hora_actual_utc = datetime.datetime.utcnow()

    zona_horaria_espana = pytz.timezone('Europe/Madrid')
    zona_horaria_eeuu = pytz.timezone('America/New_York')
    zona_horaria_china = pytz.timezone('Asia/Shanghai')

    hora_espana = hora_actual_utc.astimezone(zona_horaria_espana)
    hora_eeuu = hora_actual_utc.astimezone(zona_horaria_eeuu)
    hora_china = hora_actual_utc.astimezone(zona_horaria_china)

    fecha_hora_espana = hora_espana.strftime("%Y-%m-%d %H:%M:%S %Z")
    fecha_hora_eeuu = hora_eeuu.strftime("%Y-%m-%d %H:%M:%S %Z")
    fecha_hora_china = hora_china.strftime("%Y-%m-%d %H:%M:%S %Z")

    print("Fecha y hora en España:", fecha_hora_espana)
    print("Fecha y hora en Estados Unidos (Nueva York):", fecha_hora_eeuu)
    print("Fecha y hora en China:", fecha_hora_china)

if __name__ == "__main__":
    obtener_fecha_en_paises()