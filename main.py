import barcode
import subprocess

print("type help to get supported barcode types")
barcodetype = input("What type of barcode do you want to make? (if none specified defaults to code128)")

types = ["ean8","ean13","ean14","upca","jan","isbn10","isbn13","issn","code39","code128","pzn"]

if barcodetype == "help":
	for i in  types:
		print(i)

if barcodetype == "":
	barcodetype = "code128"

if barcodetype in types:
	barcode_text = input("what do you want your barcode to say?")

	
	code = barcode.get(barcodetype, barcode_text)
	image_filename = input("what do you want to save the file as?")	
	filename = code.save(image_filename)
	print("file saved as " + image_filename + ".svg")

elif barcodetype not in types:
	print("incorrect barcode type!")
	
	



