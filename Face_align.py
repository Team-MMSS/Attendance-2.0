from matplotlib import pyplot
from mtcnn import MTCNN
import imutils
from imutils import face_utils
import matplotlib.pyplot as plt
import numpy as np
import cv2
detector = MTCNN()
class FaceAligner:
    def __init__(self, desiredLeftEye=(0.30, 0.30),
        desiredFaceWidth=224, desiredFaceHeight=None):
        self.desiredLeftEye = desiredLeftEye
        self.desiredFaceWidth = desiredFaceWidth
        self.desiredFaceHeight = desiredFaceHeight
        if self.desiredFaceHeight is None:
            self.desiredFaceHeight = self.desiredFaceWidth
    def align(self, image, left_eye, right_eye):  
        dY = right_eye[1] - left_eye[1]
        dX = right_eye[0] - left_eye[0]
        angle = np.degrees(np.arctan2(dY, dX))
        desiredRightEyeX = 1.0 - self.desiredLeftEye[0]
        dist = np.sqrt((dX ** 2) + (dY ** 2))
        desiredDist = (desiredRightEyeX - self.desiredLeftEye[0])
        desiredDist *= self.desiredFaceWidth
        scale = desiredDist / dist
        eyesCenter = (int((left_eye[0] + right_eye[0]) // 2),
                      int((left_eye[1] + right_eye[1]) // 2))
        M = cv2.getRotationMatrix2D(eyesCenter, angle, scale)
        tX = self.desiredFaceWidth * 0.5
        tY = self.desiredFaceHeight * self.desiredLeftEye[1]
        M[0, 2] += (tX - eyesCenter[0])
        M[1, 2] += (tY - eyesCenter[1])
        (w, h) = (self.desiredFaceWidth, self.desiredFaceHeight)
        output = cv2.warpAffine(image, M, (w, h),flags=cv2.INTER_CUBIC)
        return output
def detect_face(img):
    pixels = pyplot.imread(img)
    faces = detector.detect_faces(pixels)
    return faces
img = 'test-data/test.jpg'
fa = FaceAligner(desiredFaceWidth=500,desiredFaceHeight=500)
original_img= cv2.imread(img)
faces = detect_face(img)

if len(faces)>0:
    i=0
    for face in faces:
        path = str(i)+'.jpg'
        aligned_img = fa.align(cv2.imread(img), face['keypoints']['left_eye'], face['keypoints']['right_eye'])
        cv2.imwrite("test-data/Aligned_images/"+path,aligned_img)
        i+=1   