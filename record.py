from picamera2.encoders import H264Encoder, Quality
from picamera2 import Picamera2
import time
import os

video_directory = "videos"
encoder = H264Encoder()
file_index = 0

def get_file_extension(encoder):
    if (isinstance(encoder, H264Encoder)):
        return "h264"
    elif(isinstance(encoder, MJPEGEncoder)):
        return "mjpeg"
    

def get_filename(index: int):
    return os.path.abspath(f'{os.getcwd()}/{video_directory}/{index:04}.{get_file_extension(encoder)}')

if not os.path.exists(video_directory):
    os.mkdir(video_directory)

try:
    picam2 = Picamera2()
except IndexError:
    print("No camera available")
    exit(1)
    
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

while True:
    filename = get_filename(file_index)
    print ("Start " + filename)
    picam2.start_recording(encoder, filename, quality=Quality.MEDIUM)
    time.sleep(60)
    picam2.stop_recording()
    print ("Stop")
    file_index +=1
    if file_index > 11:
        file_index = 0
    