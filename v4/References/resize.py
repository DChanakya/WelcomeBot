from PIL import Image

def scale_and_resize():
    img=Image.open("source.gif")
    width,height=img.size
    img.resize((720,480)).save("gif.gif")

scale_and_resize()
