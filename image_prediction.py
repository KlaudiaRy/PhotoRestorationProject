import PIL
from PIL import Image, ImageFilter

import torch
import tensorflow as tf
import torchvision.transforms as T
from PIL import Image
import keras
import numpy as np



def generate_images():
    model = tf.keras.models.load_model('models/model1/model1',compile=False)

    # Check its architecture
    #print(model.summary())
    #FOR CYCLEGAN
    """
    img = Image.open('tmp/tmp_img_modified.png')
    test_input = img
    test_input = test_input.resize((256, 256))
    image_array = np.array(test_input)
    image_array = image_array / 255.0
    image_array = image_array[None, ...]
    tensor = tf.convert_to_tensor(image_array)
    prediction = model(tensor)
    prediction = prediction * 255
    prediction = np.array(prediction, dtype=np.uint8)
    if np.ndim(prediction) > 3:
        assert prediction.shape[0] == 1
        prediction = prediction[0]
    """

    #FOR PIX2PIX
    image = tf.io.read_file('tmp/tmp_img_modified.png')
    image = tf.io.decode_jpeg(image)
    image = tf.cast(image, tf.float32)
    image = tf.image.resize(image, [256, 256], method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    image = (image / 127.5) - 1
    image = tf.expand_dims(image, 0)
    prediction = model(image, training=True)
    tf.keras.preprocessing.image.save_img('tmp/tmp_img_modified.png', prediction[0])

    return 'tmp/tmp_img_modified.png'