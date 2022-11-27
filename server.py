from socket import *

class SocketServer:

    def initSocket():
        # definindo o host
        host = gethostname()
        #definindo porta
        port = 55551
        print(f'HOST: {host}, PORT: {port}')
        #criando socket
        socketServer = socket(AF_INET, SOCK_STREAM)
        # usando bind para receber a porta atribuir ao socket
        socketServer.bind((host, port))
        # definindo quantidade de cliente
        socketServer.listen(3)
        # lógica para aceitar todas as mensagens do cliente
        while 1:
            con, adr = socketServer.accept() # aceitando dados do cliente
            while 1:
                msg = con.recv(1024) # msg vinda do cliente, em parâmetros definimos o tamanho dela em bytes
                print(msg.decode())  # como as msgs vem criptografadas usamos o decode para descriptografar


if __name__ == "__main__": 
    cmd = SocketServer()
    cmd.initSocket()    