import gspread
from datetime import datetime

def registrar_chat(rol, mensaje):
    try:
        gc = gspread.service_account(filename='ocr-ruc-9bb6b695ec5d.json')
        hoja = gc.open("BITACORA-ASISTENTE IA").sheet1

        if not hoja.row_values(1):
            hoja.append_row(["Fecha y Hora", "Rol", "Mensaje"])
            hoja.format("A1:C1", {"textFormat": {"bold": True}})

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hoja.append_row([fecha_hora, rol, mensaje])

        return True
    except Exception as e:
        print(f"Error al conectar con Sheets: {e}")
        return False

def registrar_perfil(nombre, edad, medicamentos):
    try:
        gc = gspread.service_account(filename='ocr-ruc-9bb6b695ec5d.json')
        hoja = gc.open("PERFILES-ASISTENTE IA").sheet1

        if not hoja.row_values(1):
            hoja.append_row(["Fecha de Registro", "Nombre", "Edad", "Medicamentos"])
            hoja.format("A1:D1", {"textFormat": {"bold": True}})

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        hoja.append_row([fecha_hora, nombre, edad, medicamentos])

        return True
    except Exception as e:
        print(f"Error al conectar con Sheets (Perfil): {e}")
        return False