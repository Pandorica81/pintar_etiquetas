from PIL import Image, ImageDraw, ImageFont, ImageChops
from elaphe import barcode

###Datos
nro_remitente = "123450001"
remitente = "REMITENTE"
prueba_direccion = "Prueba Direccion"
telf = "TELF: "
nro_telefono = "96868585"
P_DESTINATARIO = "P_DESTINATARIO "

#Expedicion
exp = "EXP: "
nro_exp = "565685874845478"

#Bultos
BULTOS = "BULTOS: "
BULTOS1de1 = "1 DE 1"
COD_BULTO = "COD.BULTO: "
CODE_BULTO = "63123410000001201280200"

concatenacion = nro_remitente + remitente + prueba_direccion + telf + nro_telefono + P_DESTINATARIO + exp + nro_exp + BULTOS + BULTOS1de1 + COD_BULTO + CODE_BULTO

bc = barcode('code128', concatenacion, options=dict(eclevel=2, compact=True, columns=100, rows=10), margin=0, scale=11)
bc.save('codigo_barras.png')

im = Image.new('RGBA', (1980, 1080), (255,255,255,255))
im.save('etiqueta_sencilla.jpg', dpi =(100,100))

base = Image.open('etiqueta_sencilla.jpg').convert('RGBA')
nuevoAncho=2980
nuevoAlto=4200
nImg = base.resize((nuevoAncho, nuevoAlto))
        # Guarda la imagen
nImg.save('etiqueta_sencilla_paso1.png')
print base.size

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt60 = ImageFont.truetype('ArialBold.ttf', 60)
fnt80 = ImageFont.truetype('ArialBold.ttf', 80)
fnt100 = ImageFont.truetype('ArialBold.ttf', 100)
fnt120 = ImageFont.truetype('ArialBold.ttf', 120)
fnt160bold = ImageFont.truetype('ArialBold.ttf', 160)


# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
# draw text, full opacity

d.text((200,40), exp, font=fnt100, fill=(0,0,0,255))
d.text((750,40), nro_exp, font=fnt100, fill=(0,0,0,180))

d.text((200,140), remitente, font=fnt80, fill=(0,0,0,255))
d.text((800,140), nro_remitente, font=fnt80, fill=(0,0,0,180))

d.text((200,240), prueba_direccion, font=fnt80, fill=(0,0,0,255))
d.text((900,240), P_DESTINATARIO, font=fnt80, fill=(0,0,0,180))

d.text((200,340), telf, font=fnt80, fill=(0,0,0,255))
d.text((600,340), nro_telefono, font=fnt80, fill=(0,0,0,180))

d.text((200,440), BULTOS, font=fnt80, fill=(0,0,0,255))
d.text((600,440), BULTOS1de1, font=fnt80, fill=(0,0,0,180))


d.text((200,540), COD_BULTO, font=fnt80, fill=(0,0,0,255))
d.text((750,560), CODE_BULTO, font=fnt60, fill=(0,0,0,180))

out = Image.alpha_composite(base, txt)


out.save('etiqueta_sencilla2.png')

img = Image.open('etiqueta_sencilla2.png')
 

# open an image file (.bmp,.png,.png,.gif) you have in the working folder


nuevoAncho=2980

nuevoAlto=4200


nImg = img.resize((nuevoAncho, nuevoAlto))




        # Guarda la imagen
nImg.save('etiqueta_sencilla3.png')

# abrimos una imagen




#abrimos la imagen


 

# cogemos la anchura y altura

width, height = nImg.size
print nImg.size


catIm = Image.open('etiqueta_sencilla3.png')
catCopyIm = catIm.copy()

img = Image.open('codigo_barras.png')
nuevoAncho=2400
nuevoAlto=1200

nImg = img.resize((nuevoAncho, nuevoAlto))
nImg.save('codigo_barras222.png')

OTRA_LINEA111 = Image.open('codigo_barras222.png')

width, height = OTRA_LINEA111.size
print OTRA_LINEA111.size

catCopyIm.paste(OTRA_LINEA111, (300, 2600))


catCopyIm.save('CorreosExpress.png')

CorreosExpress= Image.open('CorreosExpress.png')
CorreosExpress = CorreosExpress.resize((400, 1400))

catCopyIm.paste(CorreosExpress, (50, 100))

catCopyIm.save('pasted.png')