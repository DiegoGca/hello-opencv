import cv2

index = 0
cap = cv2.VideoCapture(index=index, apiPreference=cv2.CAP_ANY)
# https://docs.opencv.org/master/d8/dfe/classcv_1_1VideoCapture.html#aabce0d83aa0da9af802455e8cf5fd181
# https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html#ga023786be1ee68a9105bf2e48c700294d


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print(f"[INFO] No frame read from the stream {index} - Exiting...")
        break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the frames
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
