import barcode

ean = barcode.get('code128', 'Liam')
filename = ean.save('New_Liam')

print("Hello World")
