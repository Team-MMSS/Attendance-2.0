import cv2
from time import sleep
key = cv2. waitKey(1)
class capture_Photo:
    webcam = cv2.VideoCapture(0)
    sleep(2)
    while True:

        try:
            check, frame = webcam.read()
            print(check) #prints true as long as the webcam is running
            print(frame) #prints matrix values of each framecd 
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'): 
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                img_ = cv2.resize(img_,(1000,1000))
                print("Resized...")
                img_resizeqd = cv2.imwrite(filename='test-data/test.jpg', img=img_)
                print("Image saved!")
                
                break
            
            elif key == ord('q'):
                webcam.release()
                cv2.destroyAllWindows()
                break
        
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break