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


def cliente() -> NoReturn:
	"""
		Cliente que recibe un mensaje del servidor
	Details:
	--------
		s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("
		data = s.recv(1024)
		message: dict[str,str] = json.loads(
			base64.b64decode(data).decode("utf-8"))
		print("Mensaje recibido: \n{}"
				.format(json.dumps(message, indent=4)))
	args
	----
	None

	return
	------
	None

	example
	-------
		cliente()

	"""
	# file deepcode ignore MissingAPI: Not a real API
	s: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect(("192.168.1.39", 1234))
		data: bytes = s.recv(1024)
		message: dict[str,str] = json.loads(
            base64.b64decode(data).decode("utf-8")
		)
		print("Mensaje recibido: \n{}"
              .format(json.dumps(message, indent=4)))
	except Exception as err:
		print("Error de conexión")
		print("Error: {}".format(err))
	finally:
		print("¡Cerrando socket!")
		s.close()

if __name__ == "__main__":
	cliente()

