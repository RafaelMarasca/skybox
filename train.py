import cv2
import numpy as np
import os

def load_images(dir):
    images = []
    for img_file in os.listdir(dir):
        img = cv2.imread(os.path.join(dir, img_file))
        if img is not None :
            images.append((str(img_file).replace(".jpg", ""), img))

    return images

def split(img, width, height):

    M = 2048
    N = 2048

    i = 0
    for x in range(0, width, M):
        for y in range(0, height, N):
            tiles = img[1][y:y+2048, x:x+2048]

            cv2.imwrite("save/" + img[0] + '_' + str(i) + ".jpg", tiles,)

            # rotationMatrix = cv2.getRotationMatrix2D((35/2, 35/2), 90, 1.0)
            # rotated = cv2.warpAffine(tiles, rotationMatrix, (36,36))
            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + str(90) + ".png", rotated)

            # rotationMatrix = cv2.getRotationMatrix2D((35/2, 35/2), 180, 1.0)
            # rotated = cv2.warpAffine(tiles, rotationMatrix, (36,36))
            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + str(180) + ".png", rotated)

            # rotationMatrix = cv2.getRotationMatrix2D((35/2, 35/2), 270, 1.0)
            # rotated = cv2.warpAffine(tiles, rotationMatrix, (36,36))
            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + str(270) + ".png", rotated)

            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + 'x' + ".png", cv2.flip(tiles, 0))
            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + 'y' + ".png", cv2.flip(tiles, 1))
            # cv2.imwrite("save/" + img[0] + '_' + str(i) + '_' + 'xy' + ".png", cv2.flip(tiles, -1))
            
            i = i+1



if __name__ == "__main__":
    images = load_images(os.getcwd())

    if not os.path.exists("save"):
        os.makedirs("save")

    for img in images:
        split(img, 8192, 6144)

