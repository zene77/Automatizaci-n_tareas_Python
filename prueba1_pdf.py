from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.units import inch

# -----------------------------
# 1. Crear PDF y estilos
# -----------------------------
styles = getSampleStyleSheet()
report = SimpleDocTemplate("prueba.pdf")

report_title = Paragraph("Informe con tabla y gráfico", styles["h1"])
espacio = Spacer(1, 20)

# -----------------------------
# 2. Diccionario de frutas (como en el curso)
# -----------------------------
fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

# -----------------------------
# 3. Convertir diccionario → lista de listas
# -----------------------------
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

# -----------------------------
# 4. Crear tabla con estilo GRID y alineada a la izquierda
# -----------------------------
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# -----------------------------
# 5. Crear gráfico circular
# -----------------------------
pie = Pie()
pie.width = 3 * inch
pie.height = 3 * inch

pie.data = []
pie.labels = []

for fruta in sorted(fruit):
    pie.data.append(fruit[fruta])
    pie.labels.append(fruta)

report_chart = Drawing()
report_chart.add(pie)

# -----------------------------
# 6. Construir PDF
# -----------------------------
report.build([
    report_title,
    espacio,
    report_table,
    espacio,
    report_chart
])
