from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog
from pillow_heif import register_heif_opener

# Activating HEIC 
register_heif_opener()

# Folder selection with TKinter
root = tk.Tk()
root.withdraw()
path = filedialog.askdirectory()

# Creation sub folder
output_dir = os.path.join(path, "converted_jpg")
os.makedirs(output_dir, exist_ok=True)

# Extensions valides
valid_images = [".heic"]

# Conversion
for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    try:
        img_path = os.path.join(path, f)
        img = Image.open(img_path).convert("RGB")  # Needed for JPEG
        new_name = os.path.splitext(f)[0] + ".jpg"
        save_path = os.path.join(output_dir, new_name)
        img.save(save_path, "JPEG", quality=95) #set a 95 so that the file doesnt become huge
        print(f"Converti : {f} -> {new_name}")
    except Exception as e:
        print(f"Erreur sur {f} : {e}")
