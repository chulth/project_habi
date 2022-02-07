
from core.real_states_service import RealStatesHandler
import http.server


def main():
    """Init service in host 127.0.0.1 in port 8080
    """
    PORT = 8080
    HOST = '127.0.0.1'
    server = http.server.HTTPServer((HOST, PORT), RealStatesHandler)
    print(f"Server started http://{HOST}:{PORT}")
    server.serve_forever()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
