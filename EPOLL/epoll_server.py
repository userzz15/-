import socket
import select

def process_client(client_socket, recv_data):
    request = recv_data
    response_body = "<h1>hello world</h1>"
    response_header = "HTTP/1.1 200 OK\r\n"
    response_header += "Content-Length:%s" % len(response_body)
    response_header += "\r\n"

    client_socket.send((response_header + response_body).encode("utf-8"))

def main():
    # 创建服务器socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_addres = ("192.168.85.128", 9999)
    server_socket.bind(server_addres)
    server_socket.listen(128)
    # 将server_socket置为非堵塞
    server_socket.setblocking(False)
    # 创建epoll
    epl = select.epoll()
    # 将服务器socket在epoll注册
    epl.register(server_socket.fileno(), select.EPOLLIN)
    # 注册字典
    fd_event_dicts = dict()

    while True:
        fd_envnts = epl.poll()  #默认堵塞，若有数据则系统会以事件方式通知，才解堵塞
        for fd, event in fd_envnts:
            if fd == server_socket.fileno():
                client_socket, client_addres = server_socket.accept()
                client_socket.setblocking(False)
                epl.register(client_socket.fileno(), select.EPOLLIN)
                fd_event_dicts[client_socket.fileno()] = client_socket
            elif event == select.EPOLLIN:
                # 若已经链接客户有数据发送过来
                recv_data = fd_event_dicts[fd].recv(1024).decode("utf-8")
                if recv_data:
                    process_client(fd_event_dicts[fd], recv_data)
                else:
                    # 客户断开连接,解注册，并在注册字典中删除
                    fd_event_dicts[fd].close()
                    epl.unregister(fd)
                    del fd_event_dicts[fd]


    # 关闭服务器socket
    server_socket.close()

if __name__ == "__main__":
    main()