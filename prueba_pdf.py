from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

# Estilos
styles = getSampleStyleSheet()

# Crear PDF
report = SimpleDocTemplate("prueba.pdf")

# Título
titulo = Paragraph("Mi primer PDF completo", styles["h1"])

# Párrafo
texto = Paragraph(
    "Este es un párrafo de prueba para practicar ReportLab. "
    "Aquí puedes escribir cualquier texto que quieras.",
    styles["BodyText"]
)

# Espacio
espacio = Spacer(1, 20)

# Tabla de ejemplo
datos = [
    ["Fruta", "Cantidad"],
    ["Manzanas", 2],
    ["Bananas", 5],
    ["Cerezas", 8],
]

tabla = Table(datos)

# Imagen (opcional)
# Asegúrate de tener una imagen llamada 'foto.png' en la misma carpeta
try:
    img = Image("1.jpg", width=200, height=200)
except:
    img = Paragraph("No se encontró la imagen 'foto.png'.", styles["BodyText"])

# Construir PDF con todos los elementos
report.build([titulo, espacio, texto, espacio, tabla, espacio, img])
