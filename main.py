from moviepy.editor import *
import moviepy.video.fx.all as vfx
from time import sleep

BASE_STRING = "Name\n Day "
VIDEO_FILE = "./input/video.mp4"

RESIZE = 1

START = 1
END = 3

def main(start, end):
    for i in range(start,end+1):
        video = ( VideoFileClip(VIDEO_FILE)
                .resize(RESIZE)
                .set_position(("center", "center"))
                )
        title = ( TextClip(BASE_STRING + str(i),fontsize=90,color='white')
                    .set_position(('center',0.1), relative=True)
                    .set_duration(video.duration)
                    .fx(vfx.fadein, 1)
                    )


        result = CompositeVideoClip([video, title], size = (1080,1920), bg_color = (0, 0, 0))
        result.write_videofile(f"./output/result{str(i)}.mp4", bitrate='8000k', threads=8)

        print("Sleeping After Production...")
        sleep(1)

if __name__ == "__main__":
    main(START, END)