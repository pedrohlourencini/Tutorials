from PIL import Image
from utils import in_file, out_file

def media_grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            #media das coordenadas RGB
            lum = (pxl[0] + pxl[1] + pxl[2])//3
            img.putpixel((x,y), (lum, lum, lum))
    return img

def grayscale(colored):
    w, h = colored.size
    img = Image.new("RGB", (w, h))

    for x in range(w):
        for y in range(h):
            pxl = colored.getpixel((x,y))
            lum = int(0.3*pxl[0] + 0.59*pxl[1] + 0.11*pxl[2])
            img.putpixel((x,y), (lum, lum, lum))
    return img

if __name__ == '__main__':
    img = Image.open(in_file("Firefox_wallpaper.png"))
    print(img.getpixel((100, 100)))
    print(img.getpixel((500, 300)))
    print(img.getpixel((300, 500)))

    wallpaper = Image.open(in_file("Firefox_wallpaper.png"))
    gs_wallpaper = grayscale(wallpaper)
    gs_wallpaper.save(out_file("gs_wallpaper_2.jpg"))
