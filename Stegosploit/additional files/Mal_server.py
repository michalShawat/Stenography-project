import threading
import socket
import time

'''read the resouse in binary way and create the 
response with proper header '''
def read_file(path):
    str1 = ""
    inx = path.find('?')
    if inx != -1:
        path = path[:inx]
    try:
        if path.find("Files/") == -1:
            path = "Files/" + path
        fp = open(path, "rb")
    except:
        return get_header("HTTP/1.1 404 Not Found\n", 0, path)
    for line in fp:
        str1 += line
    fp.close()
    header = get_header("HTTP/1.1 200 OK\n", len(str1), path)
    print header
    return header + str1


'''consotrct a header with lack of type so the browser will 
go to defualt type of file, which is HTML'''
def get_header(header, length, path):
    if length == 0:
        end = "Connection: keep-alive\n\n"
    else:
        end = "Connection: keep-alive\n\n"
    date = time.asctime(time.localtime(time.time())) + " GMT"
    header += "Date: " + date
    header += "\nLast-Modified: " + date
    header += "\nContent-Length: " + str(length) + '\n'
    header += "X-Content-Type-Options: nosniff\n"
    # if ptype in ["png","jpg","gif"]:
    #     header += "Content-Type: image/"+ptype+'\n'
    # if ptype in ["html","css"]:
    #     header += "Content-Type: text/"+ptype+'\n'
    # elif ptype=="min.css":
    #     header += "Content-Type: text/css\n"
    # elif ptype in [ "otf","eof","ttf","woff"]:
    #     header += "Content-Type: font/"+ptype+'\n'
    # elif ptype=="svg":
    #     header+="Content-Type: image/svg+xml\n"
    # elif ptype.find("js") !=-1:
    #     header +="Content-Type:text/javascript\n"
    return header + end


'''find the get reqest of 
given web request'''
def find_get(request):
    print request
    begining = request.find("GET ")
    end = request.find("HTTP/1.")
    return request[begining + 5:end]


'''tread function to allow mulit clients ,
listening to web requests to resource '''
def listen2client(client, address):
    size = 2048
    data = client.recv(size)
    while not data == '':
        try:
            path = find_get(data)
            if data.find("If-Modified-Since") != -1:
                msg = get_header("HTTP/1.1 304 Not Modified\n", 0, path)
            else:
                msg = read_file(path)
            client.send(msg)
            data = client.recv(size)
        except:
            break
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 80
server.bind((server_ip, server_port))
server.listen(5)
threads = []
while True:
    client_socket, client_address = server.accept()
    threading.Thread(target=listen2client, args=(client_socket, client_address)).start()
