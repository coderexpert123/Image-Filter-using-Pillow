from PIL import Image

img = Image.open("my.jpg").convert("RGB")

width, height = img.size
piexels = img.load()


def red(r, g, b):
    newr = r
    newg = 0
    newb = 0
    return (newr, newb, newg)


def skyblue(r, g, b):
    newr = g
    newg = b
    newb = r
    return (newr, newb, newg)


def lemmonyellow(r, g, b):
    newr = r
    newg = b
    newb = g
    return (newr, newb, newg)


choice = '''
Enter your Choice :
1.Red
2.Blue
3.Yellow
4.Green
5.Black

'''
print(choice)
no = int(input())

print(piexels[1, 2])
for py in range(height):
    for px in range(width):
        r, g, b = img.getpixel((px, py))
        if no == 1:
            piexels[px, py] = red(r, g, b)
        elif no == 2:
            piexels[px, py] = skyblue(r, g, b)
        elif no == 2:
            piexels[px, py] = lemmonyellow(r, g, b)
        else:
            piexels[px, py] = (r, g, b)

img.show()
img.save("newimage.jpg")
