#!/usr/local/bin/python
#-*- coding: utf-8 -*-
import socket
import json
import base64
import signal
import sys
from typing import NoReturn


def signal_handler(sig, frame) -> NoReturn:
    print('¡Hasta luego!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def servidor() -> None:
    """
        Servidor que envía un mensaje al cliente
    Details:
    --------
        message: dict[str,str] = {
            "mensaje": "Hola, cliente",
            "status": "200",
            "error": ""
        }
        conn.sendall(base64.b64encode(json.dumps(message).encode("utf-8")))
    args
    ----
    None

    return
    ------
    None

    example
    -------
        servidor()
    
    """
    s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print("Socket creado exitosamente")
        s.bind(("192.168.1.39", 1234))
        s.listen(5)
        print("Esperando conexión...")
        while True:
            conn, addr = s.accept()
            print(f"Conexión establecida con {addr}")
            message: dict[str,str] = {
                "mensaje": "Hola, cliente",
                "status": "200",
                "error": ""
            }
            conn.sendall(
                base64.b64encode(
                    json.dumps(message).encode("utf-8")
                )
            )  # Se separó en múltiples líneas por legibilidad
            conn.close()
    except socket.error as err:
        print(f"Error al crear el socket: {err}")
    finally:
        print("¡Cerrando socket!")
        s.close()


if __name__ == "__main__":
    servidor()

