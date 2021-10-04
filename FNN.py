import tensorflow as tf
from tensorflow.keras import datasets, models
from tensorflow.keras.layers import Flatten, Dense, Dropout, Conv2D, MaxPool2D
from tensorflow.keras.utils import plot_model
print(tf.__version__)

mnist = datasets.mnist
(train_x, train_y), (test_x,test_y) = mnist.load_data()
train_x, test_x = train_x / 255.0, test_x / 255.0
import matplotlib.pyplot as plt
for col1 in range(16):
  plt.subplot(4,4,col1+1)
  plt.imshow(train_x[col1].reshape(28,28),cmap=plt.cm.binary)
plt.show()

digit = train_x[0]
print("digit :", digit.shape)
print("train images :", train_x.shape)
print("test images :", test_x.shape)

model1 = models.Sequential([
  Flatten(input_shape=(28,28)),
  Dense(512,activation='relu'),
  Dense(10,activation='softmax')
])
model1.summary()
plot_model(model1,to_file="model1_mnist.png",show_shapes=True)

model1.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
               metrics=['accuracy'])
hist = model1.fit(train_x, train_y, epochs=12,batch_size=256,
                  validation_split=0.25)

plt.plot(hist.history['accuracy'],'b-')
plt.plot(hist.history['val_accuracy'],'r--')
plt.legend(['train','test'],loc='upper left')
plt.ylim([0.94,1.005])
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()
sc=model1.evaluate(test_x, test_y)
print("accuracy : ", sc[1], " loss : ",sc[0])