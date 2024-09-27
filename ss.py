import cv2
from PIL import Image
import os

def screenshot_middle_frame(video_path):
    if not os.path.isfile(video_path):
        print(f"Error: The file '{video_path}' does not exist.")
        return

    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error: Could not open the video '{video_path}'.")
        return
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    
    if total_frames <= 0:
        print("Error: Could not determine the total number of frames in the video.")
        return
    middle_frame = total_frames // 2

    video_capture.set(cv2.CAP_PROP_POS_FRAMES, middle_frame)

    success, frame = video_capture.read()
    
    if success:
        resized_frame = cv2.resize(frame, (1280, 720))

        script_dir = os.path.dirname(os.path.abspath(__file__))

        output_path = os.path.join(script_dir, 'screenshot.png')
        image = Image.fromarray(cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB))

        image.save(output_path)

        print(f"Screenshot of the middle frame saved at: {output_path}")
    else:
        print("Error: Could not read the middle frame from the video.")

    # Release the video capture object
    video_capture.release()

video_absolute_path = input("Enter the absolute path to the video: ")
screenshot_middle_frame(video_absolute_path)
