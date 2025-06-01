import cv2
import numpy as np
import matplotlib.pyplot as plt
from tifffile import imread
import os
import imagecodecs

def detect_star_streak(image_path, output_dir='output'):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    img = imread(image_path)
    if len(img.shape) != 2:
        raise ValueError("Input image must be grayscale.")
    output = np.copy(img)
    
    img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
    img[img > 5] = 255
    blur = cv2.GaussianBlur(img, (5, 5), 0)

    _, thresh = cv2.threshold(blur, 225, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 10:
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = w / h if h != 0 else 0
        label = "Star" if 0.75 <= aspect_ratio <= 1.3 else "Streak"
        color = (0, 255, 0) if label == "Star" else (0, 0, 255)
        cv2.rectangle(output, (x, y), (x + w, y + h), color, 1)
        cv2.putText(output, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)


    filename = os.path.splitext(os.path.basename(image_path))[0] + '_detected_feature.png'
    output_image_path = os.path.join(output_dir, filename)
  
    cv2.imwrite(output_image_path, output)

    
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.title("Detected Features")
    plt.axis('off')
    plt.show()

    print(f"Processed image saved at: {output_image_path}")


    folder = 
    output_dir = 
    for file in os.listdir(folder):
        if file.lower().endswith(".tiff"):
            detect_star_streak(os.path.join(folder, file), output_dir= )