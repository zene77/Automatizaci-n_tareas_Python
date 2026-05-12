from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
report = SimpleDocTemplate("prueba.pdf")

titulo = Paragraph("Mi primer PDF", styles["h1"])
texto = Paragraph("Este es un párrafo de prueba para practicar ReportLab.", styles["BodyText"])
espacio = Spacer(1, 20)

report.build([titulo, espacio, texto])
