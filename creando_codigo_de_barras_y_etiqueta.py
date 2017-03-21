from PIL import Image, ImageDraw, ImageFont, ImageChops

from elaphe import barcode







###variables correos express
partner1 = "Correos"
partner2 = "Express"

nro_remitente = "123450001"
remitente = "REMITENTE"


prueba_direccion = "Prueba Direccion"
madrid_2820 = "MADRID 2820"


telf = "TELF: "
nro_telefono = "96868585"



envio_retorno = "Envio retorno: "

P_DESTINATARIO = "P_DESTINATARIO "
P_DIRECCION = "P_DIRECCION "
P_OBSERVACIONES1 = "P_OBSERVACIONES1 "
P_OBSERVACIONES2 = "P_OBSERVACIONES2 "

PLAZA = "28020 "
PLAZA1 = "MADRID 280 "
PLAZA2 = "MADRID "
ATT_TELF = "ATT: P_CONTACTO        TELF: 912345678   "


exp = "EXP: "
nro_exp = "565685874845478"

#bc = barcode('code128', nro_exp, options=dict(eclevel=2, compact=True, columns=100, rows=10), margin=0, scale=11)






REMBOLSO = "REMBOLSO: "
REMBOLSO10 = "10.00 Eur. "
BULTOS = "BULTOS: "
BULTOS1de1 = "1 DE 1"
FECHA = "FECHA: "
FECHA1 = "11/08/2016"
PESO = "PESO: "
NRO_PESO = "1.000 KG"
TIPO_DE_PORTE = "TIPO DE PORTE: "
TIPO_PORTE = "PAGADO"

REF = "REF: "
REFERENCIA = "PRUEBA REFERENCIA"

COD_BULTO = "COD.BULTO: "
CODE_BULTO = "63123410000001201280200"

BUL_CLI = "BUL.CLI: "
PAQ = "PAQ24: "

bc = barcode('code128', CODE_BULTO, options=dict(eclevel=2, compact=True, columns=100, rows=10), margin=0, scale=11)

bc.save('codigo_barras.png')

base = Image.open('maxresdefault.jpg').convert('RGBA')




nuevoAncho=2980

nuevoAlto=4200


nImg = base.resize((nuevoAncho, nuevoAlto))

        # Guarda la imagen
nImg.save('nommmsss.png')
print base.size




# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt10 = ImageFont.truetype('ArialBold.ttf', 10)
fnt15 = ImageFont.truetype('ArialBold.ttf', 15)
fnt20 = ImageFont.truetype('ArialBold.ttf', 20)
fnt25 = ImageFont.truetype('ArialBold.ttf', 25)
fnt30 = ImageFont.truetype('ArialBold.ttf', 30)
fnt35 = ImageFont.truetype('ArialBold.ttf', 35)
fnt40 = ImageFont.truetype('ArialBold.ttf', 40)
fnt50 = ImageFont.truetype('ArialBold.ttf', 50)
fnt60 = ImageFont.truetype('ArialBold.ttf', 60)
fnt70 = ImageFont.truetype('ArialBold.ttf', 70)
fnt80 = ImageFont.truetype('ArialBold.ttf', 80)
fnt100 = ImageFont.truetype('ArialBold.ttf', 100)
fnt120 = ImageFont.truetype('ArialBold.ttf', 120)
fnt160 = ImageFont.truetype('ArialBold.ttf', 160)
fnt160bold = ImageFont.truetype('ArialBold.ttf', 160)


# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
# draw text, full opacity

d.text((300,35), nro_remitente, font=fnt40, fill=(0,0,0,250))
d.text((530,35), remitente, font=fnt40, fill=(0,0,0,255))

d.text((310,70), prueba_direccion, font=fnt30, fill=(0,0,0,255))
d.text((310,100), madrid_2820, font=fnt30, fill=(0,0,0,255))
d.text((600,100), telf, font=fnt30, fill=(0,0,0,255))
d.text((700,100), nro_telefono, font=fnt30, fill=(0,0,0,255))


d.text((320,160), P_DESTINATARIO, font=fnt40, fill=(0,0,0,180))
d.text((320,200), P_DIRECCION, font=fnt40, fill=(0,0,0,180))
d.text((320,240), P_OBSERVACIONES1, font=fnt40, fill=(0,0,0,180))
d.text((320,280), P_OBSERVACIONES2, font=fnt40, fill=(0,0,0,180))


d.text((290,300), PLAZA, font=fnt160bold, fill=(0,0,0,255))
d.text((150,440), PLAZA1, font=fnt70, fill=(0,0,0,255))
d.text((150,510), PLAZA2, font=fnt50, fill=(0,0,0,200))
d.text((150,560), ATT_TELF, font=fnt40, fill=(0,0,0,180))



d.text((1110,40), exp, font=fnt70, fill=(0,0,0,180))
d.text((1280,40), nro_exp, font=fnt70, fill=(0,0,0,180))
d.text((1230,105), envio_retorno, font=fnt25, fill=(0,0,0,180))

d.text((1120,135), REMBOLSO, font=fnt25, fill=(0,0,0,180))
d.text((1150,160), REMBOLSO10, font=fnt40, fill=(0,0,0,220))


d.text((1380,135), BULTOS, font=fnt25, fill=(0,0,0,180))
d.text((1400,160), BULTOS1de1, font=fnt40, fill=(0,0,0,220))

d.text((1610,135), FECHA, font=fnt25, fill=(0,0,0,180))
d.text((1620,160), FECHA1, font=fnt40, fill=(0,0,0,220))


d.text((1120,215), TIPO_DE_PORTE, font=fnt25, fill=(0,0,0,180))
d.text((1150,235), TIPO_PORTE, font=fnt40, fill=(0,0,0,220))

d.text((1380,215), PESO, font=fnt25, fill=(0,0,0,180))
d.text((1400,235), NRO_PESO, font=fnt40, fill=(0,0,0,220))



d.text((1100,300), REF, font=fnt50, fill=(0,0,0,180))
d.text((1250,300), REFERENCIA, font=fnt50, fill=(0,0,0,180))
d.text((1100,360), COD_BULTO, font=fnt40, fill=(0,0,0,180))
d.text((1400,360), CODE_BULTO, font=fnt40, fill=(0,0,0,180))
d.text((1100,400), BUL_CLI, font=fnt50, fill=(0,0,0,180))


d.text((1100,460), PAQ, font=fnt50, fill=(0,0,0,180))


linea1 ="________________________________"
linea11 ="_____________________________"
linea2 ="_________________________________________________________"

###LINEAS
d.text((300,80), linea2, font=fnt50, fill=(0,0,0,220))
d.text((1100,155), linea1, font=fnt50, fill=(0,0,0,220))
d.text((1100,225), linea1, font=fnt50, fill=(0,0,0,220))
d.text((1100,400), linea1, font=fnt50, fill=(0,0,0,220))
d.text((1100,400), linea1, font=fnt50, fill=(0,0,0,220))
d.text((150,560), linea11, font=fnt50, fill=(0,0,0,220))
d.text((270,560), linea11, font=fnt50, fill=(0,0,0,220))




out = Image.alpha_composite(base, txt)


out.save('nommm.png')

img = Image.open('nommm.png')
 

# open an image file (.bmp,.png,.png,.gif) you have in the working folder


nuevoAncho=2980

nuevoAlto=4200


nImg = img.resize((nuevoAncho, nuevoAlto))




        # Guarda la imagen
nImg.save('nommmsss.png')

# abrimos una imagen




#abrimos la imagen


 

# cogemos la anchura y altura

width, height = nImg.size
print nImg.size


catIm = Image.open('nommmsss.png')
catCopyIm = catIm.copy()

imgbase = Image.new('RGB', (30, 2250), (255, 255, 255))
draw = ImageDraw.Draw(imgbase)
draw.line((10, 10, 10, 2250), (0, 0, 0), 30)
imgbase.save("lines1.png", 'PNG')
imgbase = Image.open('lines1.png')

catCopyIm.paste(imgbase, (1660, 150))

### OTRA LINEA
OTRA_LINEA = Image.new('RGB', (30, 590), (255, 255, 255))
draw = ImageDraw.Draw(OTRA_LINEA)
draw.line((10, 10, 10, 590), (0, 0, 0), 10)
OTRA_LINEA.save("lines111.png", 'PNG')
OTRA_LINEA = Image.open('lines111.png')

catCopyIm.paste(OTRA_LINEA, (2100, 500))
catCopyIm.paste(OTRA_LINEA, (2450, 500))
#catCopyIm.paste(OTRA_LINEA, (2600, 500))


img = Image.open('codigo_barras.png')
nuevoAncho=2400
nuevoAlto=1200

nImg = img.resize((nuevoAncho, nuevoAlto))
nImg.save('codigo_barras222.png')

OTRA_LINEA111 = Image.open('codigo_barras222.png')

width, height = OTRA_LINEA111.size
print OTRA_LINEA111.size

catCopyIm.paste(OTRA_LINEA111, (300, 2600))

CorreosExpress= Image.open('CorreosExpress.jpg')
CorreosExpress = CorreosExpress.resize((400, 1400))

catCopyIm.paste(CorreosExpress, (50, 100))

catCopyIm.save('pasted.png')