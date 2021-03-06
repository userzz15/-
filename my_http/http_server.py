import socket
import time

def process_client(client_con):

    client_request = client_con.recv(1024)
    print(client_request)
    # response = "HTTP/1.1 200 OK\r\n"
    # response += "\r\n"
    # response += "<h1>hello world</h1>"
    # client_con.send(response.encode("utf-8"))
    response_body = "<h1>hello world</h1>"
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "Content-Length:%s\r\n" % len(response_body)
    response_header += "\r\n"

    client_con.send((response_header + response_body).encode("utf-8"))
    time.sleep(2)
    client_con.close()
    print("close")

def main():
    http_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close时，资源能释放
    http_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_addres = ("192.168.3.17", 9999)
    http_socket.bind(my_addres)
    http_socket.listen(128)
    while 1:
        client_con, client_addr = http_socket.accept()
        process_client(client_con)
    http_socket.close()

if __name__ == "__main__":
    main()