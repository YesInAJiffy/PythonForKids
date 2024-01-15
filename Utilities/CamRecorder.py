import cv2

# Open a connection to the webcam (0 is usually the default camera)
# If you have multiple cameras connected to your system, you can use different indices to select a specific camera.
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"{width}   {height}")

# Define the codec and create a VideoWriter object for MP4 file
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # H.264 codec, you can also try 'avc1'

out = cv2.VideoWriter('output_1.mp4', fourcc, 20.0, (width, height))  # Adjust resolution as needed

# Record video until you press 'q'
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Webcam Recording', frame)

    # Write the frame to the output file
    out.write(frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything when the recording is done
cap.release()
out.release()
cv2.destroyAllWindows()

