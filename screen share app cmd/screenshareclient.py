from vidstream import ScreenShareClient
import threading
client=ScreenShareClient("127.0.0.1",9988)
t=threading.Thread(target=client.start_stream)
t.start()
while input("")!="quite":
	continue
client.stop_stream()