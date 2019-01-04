from EmoPy.src.fermodel import FERModel

from pkg_resources import resource_filename

import cv2

counter = 0

cap = cv2.VideoCapture("./test5.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)

fps = np.int32(fps)

print("Frames Per Second:",fps,"\n")

ret, frame = cap.read()

emotion ="" 


# cap = cv2.VideoCapture("./test5.mp4")
# ret, frame = cap.read()
# print(frame.shape, " " ,ret)
# while ret:
#     cv2.imwrite("test.jpg",frame)
#.    if count==0:
#
#       emotion = model.predict("test.jpg")
#.    if count==fps-1:
#       count=0
#     cv2.putText(frame, emotion, (15, 15), font, 0.5, (255, 0, 0), 2, cv2.LINE_AA)
#     cv2.imshow("Output",frame)
#.    counter=counter+1
#     if cv2.waitKey(5) == 27:
#         break
#     ret, frame = cap.read()

# cv2.destroyAllWindows()
# cap.release()
