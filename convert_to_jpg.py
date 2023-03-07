from pathlib import Path
import cv2
import matplotlib.pyplot as plt

def convert_to_8bit(path):
    print(f"converting {path}" )
    img16 = cv2.imread(str(path), cv2.IMREAD_UNCHANGED)
    plt.imsave(f"images_8bit/{path.stem}.jpg", img16, cmap="gray")

path = Path("images")
for i,p in enumerate(path.rglob("*")):
    print(i)
    convert_to_8bit(p)