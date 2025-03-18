import glob
import imutils
import cv2
import itertools
import numpy as np


# scales the pictures down
# (Quelle: https://www.tutorialkart.com/opencv/python/opencv-python-resize-image/)
def scale(img):
    scale_perc = 15
    width = int(img.shape[1] * scale_perc / 100)
    height = int(img.shape[0] * scale_perc / 100)
    dim = (width, height)
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized


# change "train" to "test" or vice versa to change data set
path = glob.glob("C:/Users/mkilc/Desktop/Flaschendatensatz/test/0/*.JPG")
path2 = glob.glob("C:/Users/mkilc/Desktop/Flaschendatensatz/test/25/*.JPG")
path3 = glob.glob("C:/Users/mkilc/Desktop/Flaschendatensatz/test/50/*.JPG")
path4 = glob.glob("C:/Users/mkilc/Desktop/Flaschendatensatz/test/75/*.JPG")
path5 = glob.glob("C:/Users/mkilc/Desktop/Flaschendatensatz/test/100/*.JPG")
table = np.zeros((6, 5), dtype=int)

for file in itertools.chain(path, path2, path3, path4, path5):
    image = cv2.imread(file)

    # down scale
    result = scale(image)
    img_gray = cv2.split(result)[2]

    # smoothing
    bottle = cv2.GaussianBlur(img_gray, (7, 7), 0)

    # threshold of 20 was picked and inverted binary image was created
    (T, img_threshold) = cv2.threshold(bottle, 20, 255, cv2.THRESH_BINARY_INV)

    # morphological transformations helps to get rid of any shapes marked outside the liquid
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    bottle_open = cv2.morphologyEx(img_threshold, cv2.MORPH_OPEN, kernel)

    # finds all contours of the marked liquid
    contours = cv2.findContours(bottle_open.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    bottle_clone = result.copy()

    # areas helps to find the largest contour
    areas = [cv2.contourArea(contour) for contour in contours]

    # if bottle is empty, it will throw a ValueError here, since there is no marked liquid at all
    # we catch the error, show that the bottle is empty and continue with the next iteration (next picture)
    try:
        (contours, areas) = zip(*sorted(zip(contours, areas), key=lambda a: a[1]))
    except ValueError:
        cv2.putText(bottle_clone, "0", (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        table[0, 0] += 1
        cv2.imshow('result', bottle_clone)
        cv2.waitKey(0)
        continue

    # print contour
    # cv2.drawContours(bottle_clone, [contours[-1]], -1, (255, 0, 0), 2)

    # draw box and calculate how full the water is by using the aspect Ratio of the contours
    (x, y, w, h) = cv2.boundingRect(contours[-1])
    aspectRatio = float(w) / h
    if 0 < aspectRatio < 0.35:
        cv2.rectangle(bottle_clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(bottle_clone, "100", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        table[4, 4] += 1
    elif 0.35 < aspectRatio < 0.5:
        cv2.rectangle(bottle_clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(bottle_clone, "75", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        table[3, 3] += 1
    elif 0.5 < aspectRatio < 0.65:
        cv2.rectangle(bottle_clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(bottle_clone, "50", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        table[2, 2] += 1
    elif 1 < aspectRatio:
        cv2.rectangle(bottle_clone, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(bottle_clone, "25", (x + 10, y + 20), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
        table[1, 1] += 1

    # print(aspectRatio)
    cv2.imshow('result', bottle_clone)
    cv2.waitKey(0)

cv2.destroyAllWindows()

# Print the table
print("       0   25  50  75  100")
print("0      " + "   ".join(map(str, table[0])))
print("25     " + "   ".join(map(str, table[1])))
print("50     " + "   ".join(map(str, table[2])))
print("75     " + "   ".join(map(str, table[3])))
print("100    " + "   ".join(map(str, table[4])))
