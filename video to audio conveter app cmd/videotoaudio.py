from moviepy.editor import *
import sys
clip=VideoFileClip(r'filename')
clip.audio.write_audiofile(r'audioname')