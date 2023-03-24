import cv2

# Create an object to read
# from camera
video = cv2.VideoCapture("25_fr.mp4")

# We need to check if camera
# is opened previously or not
if (video.isOpened() == False):
	print("Error reading video file")

# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))

size = (frame_width, frame_height)

# Below VideoWriter object will create
# a frame of above defined The output
# is stored in 'filename.avi' file.
result = cv2.VideoWriter('filename.avi',
						cv2.VideoWriter_fourcc(*'MJPG'),
						10, size)
		
c=1
while c<250:

    grabbed, frame = video.read()
    if c%4==0:
        result.write(frame)
        cv2.waitKey(1)
    c+=1



video.release()
result.release()
	
cv2.destroyAllWindows()

print("The video was successfully saved")
