from socket import *

class SocketClient:

    def client():
        host = gethostname()
        port = 55551
        # chamando o socket
        cli = socket(AF_INET, SOCK_STREAM)
        # conectando
        cli.connect((host, port))
        # lógica para enviar msg
        while 1:
            msg = input("Digite algo: ")
            cli.send(msg.encode()) # enviando mensagem codificada


if __name__ == "__main__": 
    cmd = SocketClient
    cmd.client()    