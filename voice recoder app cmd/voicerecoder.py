import sounddevice as sd 
from scipy.io.wavfile import write
import wavio as wv 
import sys
freq=44100
dur=int(sys.argv[1])
reco=sd.rec(int(dur*freq),samplerate=freq,channels=2)
sd.wait()
write("reco.wav",freq,reco)
wv.write("reco.wav",reco,freq,sampwidth=2)