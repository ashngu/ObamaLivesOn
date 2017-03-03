# -*- coding: utf-8 -*-

from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
import csv

import csv

imgWidth = 512
margin = offset = 50
maxTextLength = 950

with open('obamaScheduleSummaries.txt', 'rb') as file:
	reader = csv.DictReader(file, delimiter='\t')
	for row in reader:
		content = row['content']
		date = row['date']
		filename = row['filename']

		offset = 50
		im = Image.new("RGB", (imgWidth, imgWidth), "white")
		draw = ImageDraw.Draw(im)

		font = ImageFont.truetype("AdobeCaslonPro.otf", 20)
		draw.text((margin, offset), date, font=font, fill=(0,0,0))

		font = ImageFont.truetype("AdobeCaslonPro.otf", 15)
		if len(content) > maxTextLength:
			content = content[:maxTextLength] + "..."

		offset = 90

		for line in wrap(content, width = 60):
			draw.text((margin, offset), line, font=font, fill=(0,0,0))
			offset += font.getsize(line)[1] + 5

		draw.text((margin, offset + 20), row['url'],font=font, fill=(0,0,0))
		im.save(filename +".png")
