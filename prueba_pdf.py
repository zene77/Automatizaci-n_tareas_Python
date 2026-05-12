from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
report = SimpleDocTemplate("prueba.pdf")

titulo = Paragraph("Mi primer PDF", styles["h1"])

report.build([titulo])
