
import cv2
def whatsapp_compress(in_path, out_path, quality=75, max_size=1600):
    img=cv2.imread(in_path)
    h,w=img.shape[:2]
    if max(h,w)>max_size:
        scale=max_size/max(h,w)
        img=cv2.resize(img, (int(w*scale), int(h*scale)))
    cv2.imwrite(out_path, img, [int(cv2.IMWRITE_JPEG_QUALITY), quality])

# Simulate 5x forward
for i in range(1,6):
    whatsapp_compress("stego.png" if i==1 else f"stego_wa_{i-1}.jpg", f"stego_wa_{i}.jpg")
    print(f"Forward {i}: done")

print("Now test: python stegstr-cli.py detect stego_wa_5.jpg --json")
