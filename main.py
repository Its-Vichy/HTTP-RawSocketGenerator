import socket, threading, httpx

class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 1337))
        s.listen(1)

        while True:
            conn, _ = s.accept()
            data = conn.recv(1024)
            print(f'[SOCKET] {data}')

if __name__ == '__main__':
    Server().start()

    try:
        # Build your requests and send it to "http://127.0.0.1:1337".

        payload = {
            "content": "wow !"
        }

        header = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"
        }

        httpx.post('http://127.0.0.1:1337', json=payload, headers=header)
    except:
        pass
