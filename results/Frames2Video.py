# python3 combine.py
import cv2
from glob import glob

def frames_to_video(input_path, output_path, fps):
    frames = []

    for i in range(1,28):
        ip = "./results/" + str(i) + ".jpg"
        f = ip
        print (ip)
        #f = f"./results/{i}.jpg" 
        frame = cv2.imread(f)
        height, width, channels = frame.shape
        size = (width, height)
        frames.append(frame)

    video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

    for frame in frames:
        video_writer.write(frame)

    video_writer.release()
    return True

frames_to_video("results/*.jpg","result.mp4", 5)
