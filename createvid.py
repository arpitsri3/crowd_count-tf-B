from moviepy.editor import VideoFileClip
import numpy as np
import cv2
import argparse

font = cv2.FONT_HERSHEY_SIMPLEX
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Crowd Counting')
    parser.add_argument(
        'InputVideo',
        type=str,
        help='Path to INput VIdeo.'
    )
    parser.add_argument(
        'Avfile',
        type=str,
        help='Path to av count'
    )
    parser.add_argument(
        'OutputVideo',
        type=str,
        help='Path to output video'
    )
parser.add_argument(
    'countFile',
    type=str,
    help='Path to occupied count'
)
args = parser.parse_args()

vid_path = args.InputVideo
out_path = args.OutputVideo
countFile = args.countFile
avfile = args.Avfile

feed_vid = cv2.VideoCapture(vid_path)
success = True

fps = feed_vid.get(cv2.CAP_PROP_FPS)

fps = np.int32(fps)
print("Frames Per Second:",fps,"\n")

counter = 0
tm = 0
counts = []
avai = []

out = open(countFile, "r")
for line in out: 
    counts.append(line)
    counts.append(line)
    counts.append(line)
out.close()

out = open(avfile, "r")
for line in out: 
    avai.append(line)
    avai.append(line)
    avai.append(line)
out.close()

def pipeline(img):
    global counter, tm, font
    counter += 1
    if tm>=len(counts):
        tm = len(counts)-1
    txt ='Available Slots:'+ avai[tm]
    txt2 ='Occupied Slots:'+ counts[tm]
    #print(txt)
    if counter <= fps:
        cv2.putText(img, txt[:-1], (30, 30), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, txt2[:-1], (30, 45), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
    else:
        cv2.putText(img, txt[:-1], (30, 30), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(img, txt2[:-1], (30, 45), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        counter = 0
        tm += 1
    return img


video_output = out_path #'./test_videos_output/project_video_output.mp4'
## To speed up the testing process you may want to try your pipeline on a shorter subclip of the video
## To do so add .subclip(start_second,end_second) to the end of the line below
## Where start_second and end_second are integer values representing the start and end of the subclip
## You may also uncomment the following line for a subclip of the first 5 seconds
##clip1 = VideoFileClip("test_videos/solidWhiteRight.mp4").subclip(0,5)
clip1 = VideoFileClip(vid_path)
out_clip = clip1.fl_image(pipeline) #NOTE: this function expects color images!!
out_clip.write_videofile(video_output, audio=False)

"""
feed_vid = cv2.VideoCapture(vid_path)
success = True
fourcc = cv2.VideoWriter_fourcc(*'H264')
if success:
    success, im = feed_vid.read()
    print("success-", success)

    fps = feed_vid.get(cv2.CAP_PROP_FPS)

    fps = np.int32(fps)
    print("Frames Per Second:",fps,"\n")

    counter = 0
    tm = 1
    if success:
        video = cv2.VideoWriter(out_path, cv2.VideoWriter_fourcc(*'H264'), fps, (im.shape[1], im.shape[0]))

    out = open(countFile, "r")

    while success:
        counter +=1
        img = np.copy(im)
        txt = out.readline(tm)
        if counter <= fps:
            cv2.putText(img, txt, (0, 0), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(img, txt, (0, 0), font, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            counter = 0
            tm += 1
        video.write(img)
        success, im = feed_vid.read()
"""

#video.release()
feed_vid.release()
cv2.destroyAllWindows()

