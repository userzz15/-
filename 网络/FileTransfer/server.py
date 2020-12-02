import socket
import threading

def process_client(socket_con, client_ip, client_port):
    print("用户%s:%s连接" % (client_ip, client_port))
    client_data = socket_con.recv(1024)
    if client_data:
        need_file = client_data.decode("utf-8")
        print("用户需要:", need_file)

        with open(need_file, "rb") as f:
            file_data = f.read()
        socket_con.send(file_data)

    socket_con.close()
    print("用户%s:%s退出" % (client_ip, client_port))

def main():
    # 创建服务器sockt
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addres = ("", 9999)
    server_socket.bind(addres)
    server_socket.listen(128)
    print("server listen!")
    while 1:
        socket_con, (client_ip, client_port)= server_socket.accept()
        # process_client(socket_con, client_ip, client_port)
        threading.Thread(target=process_client, args=(socket_con, client_ip, client_port,), daemon=True).start()
    server_socket.close()


if __name__ == "__main__":
    main()