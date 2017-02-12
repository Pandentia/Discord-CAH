from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import textwrap

def drawcard(text, color): #black is true white is false
    if color:
        card = Image.open("blackcard.png")
        fill = "#FFFFFF"
    else:
        card = Image.open("whitecard.png")
        fill = "#23272A"

    txt = Image.new('RGBA', card.size, (255,255,255,0))

    d = ImageDraw.Draw(txt)

    txtcrd = [text]
    h = 181

    size = 31
    while h > 180:
        size -= 1
        fnt = ImageFont.truetype('Whitney-Book.ttf', size)
        w, h = d.textsize(text, font=fnt)
        clip = 200
        while w > 175:
            clip -= 1
            txtcrd = textwrap.wrap(text, width=clip)
            w = max([w[0] for w in [d.textsize(t, font=fnt) for t in txtcrd]])
        w, h = d.textsize("\n".join(txtcrd), font=fnt)

    text = "\n".join(txtcrd)

    d.text((12,12), text, font=fnt, fill=fill)

    card = Image.alpha_composite(card, txt)
    return card

def joincards(clist):
    w, h = len(clist) * 192, 197

    img = Image.new('RGBA', (w, h), (255,255,255,0))

    for i, c in enumerate(clist):
        img.paste(c, ((i*192),0))

    b = BytesIO()
    img.save(b, "png")
    b.seek(0)

    return b
