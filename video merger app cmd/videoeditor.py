from moviepy.editor import *
import sys
clip1=VideoFileClip(str(sys.argv[1]))
clip2=VideoFileClip(str(sys.argv[2]))
final=concatenate_videoclips([clip1,clip2])
final.write_videofile(str(sys.argv[3]))