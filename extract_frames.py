import cv2
import os

def extract_frames(video_path, output_folder, frame_skip):
    cap = cv2.VideoCapture(video_path)
    frame_number = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_number += 1

        # Skip frames according to the frame_skip value
        if frame_number % frame_skip != 0:
            continue

        frame_path = os.path.join(output_folder, f"frame_{frame_number}.jpg")
        cv2.imwrite(frame_path, frame)

    cap.release()

if __name__ == "__main__":
    video_path = "video.mp4"
    output_folder = "frames"
    frame_skip = 30  # Set the frame skipping value
    os.makedirs(output_folder, exist_ok=True)
    extract_frames(video_path, output_folder, frame_skip)
