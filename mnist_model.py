from keras.models import model_from_json
import cv2 as cv
import numpy as np

mnist_file = open('models/mnist/model2.json', 'r')
loaded_mnist = mnist_file.read()
mnist_file.close()
model_mnist = model_from_json(loaded_mnist)
model_mnist.load_weights('models/mnist/mnist_weights.h5')
print("Loaded the model")


def preprocess(src):
    img = cv.imread(src)
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret, tresh = cv.threshold(gray_img, 100, 255, cv.THRESH_BINARY_INV)
    img_resized = cv.resize(tresh, (28, 28), interpolation=cv.INTER_AREA)
    img_norm = img_resized / 255
    img_norm = img_norm.reshape(28, 28, 1)
    img_processed = img_norm.reshape(1, 28, 28, 1)
    return img_processed


def prediction():
    img_processed = preprocess('pic.jpg')
    my_prediction = model_mnist.predict(img_processed)
    my_prediction = str(np.argmax(my_prediction))
    print(my_prediction)
    return my_prediction


# The next function might seem redundant, didnt work the other way due to kerases problems with asynchronicity
def do_prediction():
    answer = prediction()
    return answer


print(do_prediction())
