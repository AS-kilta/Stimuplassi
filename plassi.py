from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import csv
import operator
from collections import defaultdict


# CSV-muotoisen plassin tiedostonimi
plassi_filename = "plassi.csv"
# Taustan tiedostonimi
tausta_filename = "plassi_tausta.png"
# Fontin tiedostonimi
fontti_filename = "Chelsea III.ttf"
# Fontin väri (0-255 RGB)
font_color = (255,255,255)

tables = [
	("DI Henry Sanmark", 4, 7, 1, 24),
	("Gofore", 4, 7, 36, 59),
	("Academic Work", 4, 7, 69, 92),
	("HiQ", 10, 13, 1, 24),
	("Prosys", 10, 13, 36, 59),
	("Tuxera", 10, 13, 69, 92),
	("AS20", 16, 19, 36, 59),
	("Eficode", 16, 19, 69, 92),
	("Valmet", 22, 25, 1, 24),
	("GIM", 22, 25, 36, 59),
	("Futurice", 22, 25, 69, 92),
	("Nimetön", 28, 31, 1, 24),
	("TTER", 28, 31, 36, 59),
	("Reaktor", 28, 31, 69, 92)
]



plassi = list(csv.reader(open(plassi_filename)))
plassiH = len(plassi)
plassiW = len(plassi[0])

tableNames = defaultdict(list)
for y in range(plassiH):
	for x in range(plassiW):
		name = plassi[y][x]
		if len(name) < 2:
			continue

		for t in tables:
			if x >= t[1] and x < t[2] and y >= t[3] and y < t[4]:
				tableNames[t[0]].append((name, y+x*plassiH))

names = []
for t in tableNames:
	tableNames[t].sort(key = operator.itemgetter(1))
	place = 1
	for n in tableNames[t]:
		names.append((n[0], t, place))
		place += 1

names.sort(key = operator.itemgetter(0))
print(names)

img = Image.open(tausta_filename)
imgW, imgH = img.size
font = ImageFont.truetype(fontti_filename, 36)

draw = ImageDraw.Draw(img)
lineY = 400;
lineX = 400;
for name in names:
	draw.text((lineX, lineY), name[0], font_color, font=font)
	draw.text((lineX+400, lineY), name[1], font_color, font=font)
	draw.text((lineX+750, lineY), str(name[2]), font_color, font=font)
	lineY += 36
	if lineY > imgH - 550:
		lineX += 960
		lineY = 400

img.save("plassi/plassi.png")

# for row in plassi:
# 	for name in row:
# 		if len(name) < 2:
# 			continue

# 		print(name)

# 		imgCpy = img.copy()
# 		draw = ImageDraw.Draw(imgCpy)
# 		fontId = 0
# 		w, h = draw.textsize(name,font=fonts[fontId][0])
# 		w -= fonts[fontId][1]/10
# 		while w > imgW-2*border_size:
# 			fontId += 1
# 			w, h = draw.textsize(name,font=fonts[fontId][0])
# 			w -= fonts[fontId][1]/10

# 		draw.text(((imgW/2)-(w/2), (imgH/2)-(h/2)), name, font_color, font=fonts[fontId][0])
# 		imgCpy.save("nimikortit/nimikortti - "+name+".png")
