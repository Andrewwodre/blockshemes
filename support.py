from PIL import Image, ImageDraw, ImageFont

def start():
    global im
    im = Image.new('RGB', (500, 1200), (255, 255, 255))
    global draw
    draw = ImageDraw.Draw(im)
    draw.ellipse((200, 1, 300, 50), fill='white', outline=(0, 0, 0))
    global fnt
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 16)
    draw.text((220, 15), "Start", font=fnt, fill=(0, 0, 0))

def block(shag, num, text):
    draw.line(xy=(250, num * 50 + shag * num - 20, 250, num * 50 + shag * num), fill='black')
    draw.rectangle((200, num * 50 + shag * num, 300, num * 50 + shag * num + 50), fill='white', outline=(0, 0, 0))
    draw.text((220, 15 + num * 50 + num * shag), text=text, font=fnt, fill=(0, 0, 0))
    return im

def intout(shag, num, text):
    draw.line(xy=(250, num * 50 + shag * num - 20, 250, num * 50 + shag * num), fill='black')
    draw.polygon((215, num * 50 + shag * num, 300, num * 50 + shag * num, 285, num * 50 + shag * num + 50, 200, num * 50 + shag * num + 50), fill='white', outline=(0, 0, 0))
    draw.text((220, 15 + num * 50 + num * shag), text=text, font=fnt, fill=(0, 0, 0))
    return im

def fin(shag, num):
    draw.line(xy=(250, num * 50 + shag * num - 20, 250, num * 50 + shag * num), fill='black')
    draw.ellipse((200, num * 50 + shag * num, 300, num * 50 + shag * num + 50), fill='white', outline=(0, 0, 0))
    draw.text((220, 15 + num * 50 + num * shag), text="end", font=fnt, fill=(0, 0, 0))
    return im


def main():
    start()
    block(20, 1, "no no").show()
