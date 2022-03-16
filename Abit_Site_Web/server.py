import socket
import sqlite3


def find_most_pop():
    con = sqlite3.connect('fuckults.db')
    cur = con.cursor()
    m = list()
    for row in cur.execute('SELECT * FROM fuck ORDER BY size DESC'):
        m.append(row)
        if len(m) == 3:
            con.close()
            return m
    return m

def load_page(request_data):
    hdrs_for_css = 'HTTP/1.1 200 OK\r\nContent-type: text/css; charset=utf-8\r\n\r\n'
    hdrs = 'HTTP/1.1 200 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n'
    hdrs_404 = 'HTTP/1.1 404 OK\r\nContent-type: text/html; charset=utf-8\r\n\r\n'
    print("_________________________\n", request_data.split('.'), "\n_________________________\n")
    path = request_data.split(' ')[1]
    print(path)
    try:
        if path == "/main_page.html":
            file = open('web' + path, "r")
            x = str()
            for i in file:
                x += i
                if '<div class="con_pop_blocks">' in i:
                    for i2 in list(find_most_pop()):
                        x += '<div class="pop_block"><a href = "#" ><p>'\
                             + i2[2] + '<p><img src="'\
                             + i2[3] + '"><p>' + \
                             i2[1] + '</p></a></div>'
            return hdrs.encode('utf-8') + x.encode('utf-8') # .encode("1251")
        else:
            with open('web' + path,  'rb') as file:
                respones = file.read()
            if path.split('.')[1] == 'css':
                return hdrs_for_css.encode('utf-8') + respones
            return hdrs.encode('utf-8') + respones

    except FileNotFoundError:
        return (hdrs_404 + 'Sorry').encode('utf-8')


# Набор серверных инструкций
def start_server():
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        serv.bind(('127.0.0.1', 9100))
        serv.listen(4)
        while 1:
            client_socket, address = serv.accept()
            data = client_socket.recv(1024).decode('utf-8')
            print(data)
            content = load_page(data)
            client_socket.send((content))
            client_socket.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        serv.close()
        print('shut down')


if __name__ == '__main__':
    start_server()
