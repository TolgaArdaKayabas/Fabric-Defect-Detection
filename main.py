import tkinter as tk
from numba import jit, cuda
import keras
from PIL import Image
from tkinterdnd2 import DND_FILES, TkinterDnD
from tkinter import filedialog, messagebox
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import cv2
from matplotlib import pyplot as plt

model_path = "densenet_single_class_model.h5"
model = keras.models.load_model(model_path)

def predict_image(path):
    try:
        image = load_img(path, target_size=(224, 224))

        image_array = img_to_array(image)
        image_array = np.expand_dims(image_array, axis=0)

        image_array = image_array / 255.0

        prediction = model.predict(image_array)
        print(prediction)

    finally:
        if prediction < 0.55:
            messagebox.showinfo(message="Fabric in the image is defected")
            return False
        else:
            return True


def on_drop(event):
    # Get the dropped file(s) path
    file_paths = root.tk.splitlist(event.data)
    for file_path in file_paths:
        predict_image(file_path)


def browse_files():
    # Open a file dialog to select files
    files = filedialog.askopenfilenames()
    for file in files:
        predict_image(file)


def detect():
    flag = True
    while (flag):
        file_name = "photo.jpg"
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        cv2.imwrite(file_name, frame)
        cap.release()
        flag = predict_image(file_name)


root = TkinterDnD.Tk()
root.title("Defect Detection")
root.geometry("500x400")

file_listbox = tk.Listbox(root, width=60, height=15)
file_listbox.pack(pady=10)

file_listbox.drop_target_register(DND_FILES)
file_listbox.dnd_bind("<<Drop>>", on_drop)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

browse_button = tk.Button(button_frame, text="Browse Files", command=browse_files)
browse_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Start Detection", command=detect)
clear_button.grid(row=0, column=2, padx=5)

root.mainloop()
