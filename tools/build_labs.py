"""Veriden dört föy ve birleşik PDF üretir. Makine bağlantısı kurmaz."""
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor, white
import json
from pathlib import Path
from pypdf import PdfReader, PdfWriter
ROOT=Path(__file__).resolve().parents[1]
OUTDIR=ROOT/"output"/"pdf"
OUTDIR.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('Arial',r'C:\Windows\Fonts\arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial-Bold',r'C:\Windows\Fonts\arialbd.ttf'))
OUT=str(OUTDIR/'KR_KZM_3_Speedy_LAB_1-4_Doldurulmus.pdf')
pdfmetrics.registerFontFamily('Arial',normal='Arial',bold='Arial-Bold')
c=canvas.Canvas(OUT,pagesize=(595.28,841.89))
c.setTitle('KR KZM 3 Speedy - Doldurulmuş LAB 1-4')
s=ParagraphStyle('body',fontName='Arial',fontSize=9,leading=12,textColor=HexColor('#203449'))
small=ParagraphStyle('small',parent=s,fontSize=7.4,leading=9.5)
y=0
def p(txt,size=None):
 global y
 st=size or s
 obj=Paragraph(txt,st); w,h=obj.wrap(507,y-38); obj.drawOn(c,44,y-h); y-=h+6
 if y<40: raise ValueError('Page overflow')
def head(n,title,output):
 global y
 c.setFillColor(HexColor('#123447'));c.rect(0,750,596,92,fill=1,stroke=0)
 c.setFillColor(white);c.setFont('Arial-Bold',10);c.drawString(44,815,f'LABORATUVAR {n}  /  KR KZM 3 SPEEDY')
 c.setFont('Arial-Bold',20);c.drawString(44,784,title)
 c.setFont('Arial',9);c.drawString(44,764,'Çıktı: '+output)
 y=733
 c.setFont('Arial',8);c.setFillColor(HexColor('#203449'))
 c.drawString(44,730,'Ad Soyad:');c.drawString(284,730,'Grup:');c.drawString(410,730,'Tarih: 25.10.2026')
 for name,x,w in [('ad_soyad',90,175),('grup',312,80)]:
  c.acroForm.textfield(name=f'{name}_lab{n}',tooltip=name,x=x,y=726,width=w,height=14,borderWidth=0,fillColor=HexColor('#eaf3f5'),fontSize=9)
 y=712
def label(t):
 p('<b>'+t+'</b>')
def box(t):
 global y
 obj=Paragraph(t,small);w,h=obj.wrap(485,700)
 c.setFillColor(HexColor('#eaf3f5'));c.roundRect(38,y-h-16,519,h+20,5,fill=1,stroke=0)
 obj.drawOn(c,50,y-h-6);y-=h+27
def table(rows,widths):
 global y
 data=[[Paragraph(str(z),small) for z in row] for row in rows]
 t=Table(data,colWidths=widths,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#dcecef')),('GRID',(0,0),(-1,-1),.4,HexColor('#b5c7cf')),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
 w,h=t.wrap(507,700);t.drawOn(c,44,y-h);y-=h+10
 if y<40:raise ValueError('table overflow')
def end(n,ep):
 c.setStrokeColor(HexColor('#b5c7cf'));c.line(44,38,551,38)
 c.setFont('Arial',7);c.setFillColor(HexColor('#4c6373'));c.drawString(44,26,f'Eğitim uyarlaması | {ep} | Donanım ve saha doğrulaması gerekir.');c.drawRightString(551,26,f'{n} / 4');c.showPage()

DATA=json.loads((ROOT/'data/labs.json').read_text(encoding='utf-8'))
for lab in DATA['labs']:
 for operation in lab['operations']:
  args=operation['args']
  if operation['op']=='p' and len(args)>1 and args[1]=='small':args=[args[0],small]
  globals()[operation['op']](*args)
c.save()
reader=PdfReader(OUT)
assert len(reader.pages)==4
names=['Lab1_Safety_Architecture.pdf','Lab2_IEC62443_Zone_Conduit.pdf','Lab3_Threat_Risk_Matrix.pdf','Lab4_Secure_Remote_Access.pdf']
for index,name in enumerate(names):
 writer=PdfWriter();writer.append(reader,pages=(index,index+1))
 with (OUTDIR/name).open('wb') as stream:writer.write(stream)
 print(name)
