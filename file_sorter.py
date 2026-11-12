import os
import shutil
import sys

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = input("Enter folder path: ").strip()
    if folder == "":
        folder = "."

if not os.path.isdir(folder):
    print("Folder not found!")
    sys.exit(1)

img_exts = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp"]
word_exts = [".doc", ".docx"]

pdf_count = 0
img_count = 0
word_count = 0

files = os.listdir(folder)

for f in files:
    full_path = os.path.join(folder, f)

    if not os.path.isfile(full_path):
        continue

    if f == os.path.basename(__file__):
        continue

    name, ext = os.path.splitext(f)
    ext = ext.lower()

    if ext == ".pdf":
        target_dir = os.path.join(folder, "PDF")
        pdf_count += 1
    elif ext in img_exts:
        target_dir = os.path.join(folder, "Image")
        img_count += 1
    elif ext in word_exts:
        target_dir = os.path.join(folder, "Word")
        word_count += 1
    else:
        continue

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    dest = os.path.join(target_dir, f)
    i = 1
    while os.path.exists(dest):
        dest = os.path.join(target_dir, f"{name}_{i}{ext}")
        i += 1

    shutil.move(full_path, dest)
    print(f"Moved {f} -> {target_dir}")

print("Done!")
print("PDF:", pdf_count)
print("Image:", img_count)
print("Word:", word_count)
