#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import csv
import os


# CSV-muotoisen plassin tiedostonimi
plassi_filename = "plassi.csv"
# Taustan tiedostonimi
tausta_filename = "nimikortti.png"
# Fontin tiedostonimi
fontti_filename = "Chelsea III.ttf"
# Reunuksen koko pikseleinä (eli paljonko jää tilaa tekstin ja laitojen välille)
border_size = 350
# Fontin väri (0-255 RGB)
font_color = (255,255,255)
# Nimikorttien hakemisto
output_dir = "nimikortit"


plassi = list(csv.reader(open(plassi_filename)))
print(len(plassi))
print(len(plassi[0]))

img = Image.open(tausta_filename)
imgW, imgH = img.size
fonts=[]
for i in range(40):
	fonts.append((ImageFont.truetype(fontti_filename, 500-10*i), 500))

def create_card(name):
	if len(name) < 2:
		return

	print(name)

	imgCpy = img.copy()
	draw = ImageDraw.Draw(imgCpy)
	fontId = 0
	w, h = draw.textsize(name,font=fonts[fontId][0])
	w -= fonts[fontId][1]/10
	while w > imgW-2*border_size:
		fontId += 1
		w, h = draw.textsize(name,font=fonts[fontId][0])
		w -= fonts[fontId][1]/10

	draw.text(((imgW/2)-(w/2), (imgH/2)-(h/2)), name, font_color, font=fonts[fontId][0])
	imgCpy.save(output_dir + "/nimikortti - "+name+".png")

if (os.path.isdir(output_dir) == False):
    os.makedirs(output_dir)

for row in plassi:
	for name in row:
		create_card(name)

