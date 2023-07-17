import vlc
import time
import sys
player=vlc.MediaPlayer(str(sys.argv[1]))
player.play()
time.sleep(0.5)
dur=player.get_length()
player.play()
time.sleep(dur)