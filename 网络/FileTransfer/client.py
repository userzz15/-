import socket
import threading

def main(select_file):
    # 创建客户端
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 目标地址
    target_addres = ("192.168.3.17", 9999)
    client_socket.connect(target_addres)
    # 选择
    # select_file = input("请选择需要的")
    client_socket.send(select_file.encode("utf-8"))
    file_data = client_socket.recv(1024)
    with open("下载的"+select_file, "wb+") as f:
        f.write(file_data)
    print("over")

    #关闭
    client_socket.close()


if __name__ == "__main__":
    # main()
    # for i in range(100):
    threading.Thread(target=main, args=("test.txt",)).start()
    threading.Thread(target=main, args=("下载的test.txt",)).start()