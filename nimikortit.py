from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import csv

plassi = list(csv.reader(open("plassi.csv")))
print(len(plassi))
print(len(plassi[0]))

img = Image.open("nimikortti.png")
fonts=[]
for i in range(30):
	fonts.append((ImageFont.truetype("Chelsea III.ttf", 500-10*i), 500))


for row in plassi:
	for name in row:
		if len(name) < 2:
			continue

		print(name)

		imgCpy = img.copy()
		draw = ImageDraw.Draw(imgCpy)
		fontId = 0
		w, h = draw.textsize(name,font=fonts[fontId][0])
		w -= fonts[fontId][1]/10
		while w > 3800:
			fontId += 1
			w, h = draw.textsize(name,font=fonts[fontId][0])
			w -= fonts[fontId][1]/10

		draw.text((2250-(w/2), 750-(h/2)),name,(255,255,255),font=fonts[fontId][0])
		imgCpy.save("nimikortit/nimikortti - "+name+".png")
