from datetime import datetime
from io import BytesIO

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def generate_trip_pdf(destination, trip_result):

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=40, bottomMargin=40, leftMargin=50, rightMargin=50)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle("Title2", parent=styles["Title"], fontSize=22, textColor=colors.HexColor("#0F766E"), alignment=TA_CENTER)
    subtitle_style = ParagraphStyle("Sub2", parent=styles["Normal"], fontSize=11, textColor=colors.HexColor("#64748B"), alignment=TA_CENTER, spaceAfter=20)
    heading_style = ParagraphStyle("Head2", parent=styles["Heading2"], fontSize=14, textColor=colors.HexColor("#0F172A"), spaceBefore=14, spaceAfter=6)
    body_style = ParagraphStyle("Body2", parent=styles["Normal"], fontSize=10.5, textColor=colors.HexColor("#334155"), leading=15)

    story = []

    itinerary = trip_result["itinerary"]
    research = trip_result["research"]
    budget = trip_result["budget"]
    review = trip_result["review"]

    story.append(Paragraph("✈️ AI Trip Planner", title_style))
    story.append(Paragraph(itinerary.get("trip_title", destination), subtitle_style))
    story.append(HRFlowable(width="100%", color=colors.HexColor("#E2E8F0")))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", body_style))
    story.append(Spacer(1, 8))
    story.append(Paragraph(research.get("destination_overview", ""), body_style))

    story.append(Paragraph("📅 Day-by-Day Itinerary", heading_style))
    for day in itinerary.get("daily_plan", []):
        story.append(Paragraph(f"<b>Day {day['day']}: {day['theme']}</b>", body_style))
        story.append(Paragraph(f"Morning: {day['morning']}", body_style))
        story.append(Paragraph(f"Afternoon: {day['afternoon']}", body_style))
        story.append(Paragraph(f"Evening: {day['evening']}", body_style))
        story.append(Spacer(1, 8))

    story.append(Paragraph("💰 Budget", heading_style))
    story.append(Paragraph(f"Total estimated cost: {budget.get('total_estimated_cost', '')}", body_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("🎒 Packing List", heading_style))
    packing = itinerary.get("packing_list", {})
    for category, items in packing.items():
        story.append(Paragraph(f"<b>{category.replace('_', ' ').title()}:</b> {', '.join(items)}", body_style))

    story.append(Paragraph("🛡️ Safety Tips", heading_style))
    for tip in research.get("local_safety_tips", []):
        story.append(Paragraph(f"• {tip}", body_style))

    story.append(Paragraph("💡 Travel Tips", heading_style))
    for tip in review.get("personalized_travel_tips", []):
        story.append(Paragraph(f"• {tip}", body_style))

    doc.build(story)
    return buffer.getvalue()