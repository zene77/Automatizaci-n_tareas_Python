from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import TableStyle

# -----------------------------
# 1. Estilos
# -----------------------------
styles = getSampleStyleSheet()

# -----------------------------
# 2. Crear PDF
# -----------------------------
report = SimpleDocTemplate("prueba.pdf")

# -----------------------------
# 3. Título
# -----------------------------
titulo = Paragraph("Mi primer PDF completo con gráfico", styles["h1"])

# -----------------------------
# 4. Párrafo
# -----------------------------
texto = Paragraph(
    "Este PDF contiene texto, una tabla, una imagen y un gráfico circular "
    "generado con ReportLab. Perfecto para practicar.",
    styles["BodyText"]
)

espacio = Spacer(1, 20)

# -----------------------------
# 5. DICCIONARIO DE FRUTAS
# -----------------------------
fruit = {
    "Manzanas": 2,
    "Bananas": 5,
    "Cerezas": 8,
    "Peras": 3,
    "Kiwis": 1,
}

# -----------------------------
# 6. TABLA GENERADA AUTOMÁTICAMENTE
# -----------------------------
datos = [["Fruta", "Cantidad"]]

for nombre, cantidad in fruit.items():
    datos.append([nombre, cantidad])

tabla = Table(datos)

# ESTILO DE TABLA (para que se vea)
tabla.setStyle(TableStyle([
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTSIZE", (0, 0), (-1, -1), 12),
]))

# -----------------------------
# 7. IMAGEN
# -----------------------------
try:
    img = Image("1.jpg", width=120, height=120)
except:
    img = Paragraph("No se encontró la imagen '1.jpg'.", styles["BodyText"])

# -----------------------------
# 8. GRÁFICO CIRCULAR
# -----------------------------
pie = Pie()
pie.width = 3 * inch
pie.height = 3 * inch

pie.data = []
pie.labels = []

for fruta in sorted(fruit):
    pie.data.append(fruit[fruta])
    pie.labels.append(fruta)

grafico = Drawing()
grafico.add(pie)

# -----------------------------
# 9. CONSTRUIR PDF
# -----------------------------
report.build([
    titulo,
    espacio,
    texto,
    espacio,
    tabla,
    espacio,
    img,
    espacio,
    grafico
])




