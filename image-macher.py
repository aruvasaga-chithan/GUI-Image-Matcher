import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np
import os
from PIL import Image, ImageTk

class ImageMatcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Matching Tool")
        self.root.geometry("800x600")

        # Left side - Scrolling Image Display
        self.left_frame = tk.Frame(root)
        self.left_frame.pack(side=tk.LEFT, padx=10, pady=10)

        self.image_label = tk.Label(self.left_frame)
        self.image_label.pack()

        # Right side - Search Image Display
        self.right_frame = tk.Frame(root)
        self.right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.search_image_label = tk.Label(self.right_frame)
        self.search_image_label.pack()

        # Bottom Buttons
        self.bottom_frame = tk.Frame(root)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=20)

        self.browse_button = tk.Button(self.bottom_frame, text="Select Search Image", command=self.select_search_image)
        self.browse_button.pack(side=tk.LEFT, padx=10)

        self.folder_button = tk.Button(self.bottom_frame, text="Select Image Folder", command=self.select_image_folder)
        self.folder_button.pack(side=tk.LEFT, padx=10)

        self.search_button = tk.Button(self.bottom_frame, text="Search for Matches", command=self.search_images)
        self.search_button.pack(side=tk.LEFT, padx=10)

        self.search_image_path = None
        self.image_folder_path = None

    def select_search_image(self):
        self.search_image_path = filedialog.askopenfilename(
            title="Select Search Image", 
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if self.search_image_path:
            search_img = Image.open(self.search_image_path)
            search_img = search_img.resize((300, 300))
            search_img_tk = ImageTk.PhotoImage(search_img)
            self.search_image_label.config(image=search_img_tk)
            self.search_image_label.image = search_img_tk  # Keep reference to avoid garbage collection
        else:
            messagebox.showwarning("No Image", "Please select a search image.")

    def select_image_folder(self):
        self.image_folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
        if self.image_folder_path:
            messagebox.showinfo("Folder Selected", f"Selected folder: {self.image_folder_path}")

    def search_images(self):
        if not self.search_image_path or not self.image_folder_path:
            messagebox.showwarning("Input Missing", "Please select both search image and folder.")
            return

        # Load the search image
        search_img = cv2.imread(self.search_image_path, cv2.IMREAD_GRAYSCALE)
        orb = cv2.ORB_create(nfeatures=500)  # Increase the number of features

        # Find the keypoints and descriptors in the search image
        kp1, des1 = orb.detectAndCompute(search_img, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # Search in the selected folder
        for image_file in os.listdir(self.image_folder_path):
            img_path = os.path.join(self.image_folder_path, image_file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            if img is None:
                continue

            # Display the current image on the left side
            self.show_image_left(img_path)

            # Find keypoints and descriptors in the current image
            kp2, des2 = orb.detectAndCompute(img, None)

            if des2 is not None:
                matches = bf.match(des1, des2)
                matches = sorted(matches, key=lambda x: x.distance)

                if len(matches) > 0:
                    avg_distance = sum([m.distance for m in matches]) / len(matches)

                    # Assuming a threshold to consider an image as a match
                    if avg_distance < 50:  # Adjust the threshold based on your needs
                        messagebox.showinfo("Match Found", f"Match found: {image_file}")
                        self.show_image_left(img_path)
                        return

        messagebox.showinfo("No Match", "No matching image found in the folder.")

    def show_image_left(self, image_path):
        img = Image.open(image_path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        self.image_label.config(image=img_tk)
        self.image_label.image = img_tk  # Keep reference to avoid garbage collection
        self.root.update()
        self.root.after(200)  # Pause for 200 ms between image slides (reduce delay)

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageMatcherApp(root)
    root.mainloop()
