from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
import time
import os

video_directory = "videos"


def get_filename(postfix: int):
    return os.path.abspath(f'{os.getcwd()}\\{video_directory}\\{postfix:04}.h264')

if not os.path.exists(video_directory):
    os.mkdir(video_directory)

try:
    picam2 = Picamera2()
except IndexError:
    print("No camera available")
    exit(1)
    
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

file_index = 0

while True:
    encoder = H264Encoder()
    filename = get_filename(file_index)
    picam2.start_recording(encoder, filename, quality=Quality.MEDIUM)
    time.sleep(60)
    picam2.stop_recording()
    file_index += 1
    if file_index > 11:
        file_index = 0