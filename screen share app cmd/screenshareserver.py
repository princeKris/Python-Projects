from vidstream import StreamingServer
import threading
server=StreamingServer("127.0.0.1",9988)
t=threading.Thread(target=server.start_server)
t.start()
while input("")!="quite":
	continue
server.stop_server()