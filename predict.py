import tkinter as tk
from tkinter import filedialog
from ultralytics import YOLO
from PIL import Image, ImageTk
import cv2
import os

# สร้างหน้าต่างหลักของ tkinter
root = tk.Tk()
root.title("YOLOv8 Prediction")
root.geometry("800x600")

# โหลดโมเดล YOLO
model = YOLO('runs/detect/train/weights/best.onnx')

# ฟังก์ชันสำหรับเลือกไฟล์ภาพ
def open_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")])
    if file_path:
        # แสดงเส้นทางของภาพที่เลือก
        label_path.config(text=file_path)

        # ทำนายผลลัพธ์จาก YOLO และแสดงภาพ
        predict_image(file_path)

# ฟังก์ชันสำหรับโหลดและแสดง confusion matrix
def load_confusion_matrix():
    confusion_matrix_path = "runs/detect/train2/confusion_matrix.png"  # พาธของ confusion matrix
    confusion_image = Image.open(confusion_matrix_path)

    # ปรับขนาดภาพ confusion matrix (กำหนดขนาดที่ต้องการ เช่น 400x300)
    confusion_image = confusion_image.resize((600, 400))

    confusion_image_tk = ImageTk.PhotoImage(confusion_image)
    
    # ป้ายสำหรับแสดง confusion matrix
    label_confusion.config(image=confusion_image_tk)
    label_confusion.image = confusion_image_tk


# ฟังก์ชันสำหรับการทำนายภาพ
def predict_image(file_path):
    try:
        # ทำนายด้วย YOLO และบันทึกภาพผลลัพธ์
        results = model.predict(file_path, save=True, conf=0.6)
        
        # ตรวจสอบผลลัพธ์การทำนาย
       
    except Exception as e:
        print(f"Error during prediction: {e}")
        label_path.config(text=f"Error during prediction: {e}")



# เพิ่มป้ายสำหรับแสดง confusion matrix ใน UI
label_confusion = tk.Label(root)
label_confusion.pack(pady=10)


# ปุ่มสำหรับเลือกภาพ
btn_open = tk.Button(root, text="Open Image", command=open_image)
btn_open.pack(pady=20)

# ป้ายแสดงเส้นทางของภาพที่เลือก
label_path = tk.Label(root, text="No image selected")
label_path.pack(pady=10)
load_confusion_matrix()
# ป้ายสำหรับแสดงภาพที่ทำนาย
label_image = tk.Label(root)
label_image.pack(pady=10)

# เริ่มโปรแกรม tkinter
root.mainloop()
