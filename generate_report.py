#!/usr/bin/env python3
"""
Generate Family Car Report 2026 PDF using reportlab Platypus
Updated April 2026 with comprehensive styling and content fixes
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white, black
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak,
    KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from datetime import datetime

# Color palette
DARK_BLUE = '#1A3C5E'
MED_BLUE = '#2E75B6'
ACCENT_GREEN = '#2D8B4E'
ACCENT_ORANGE = '#ED7D31'
LIGHT_BLUE = '#D6EAF8'
LIGHT_YELLOW = '#FFF9E6'
GREEN_CELL = '#C6EFCE'
ORANGE_CELL = '#FFF2CC'
RED_CELL = '#FFC7CE'

# Helper function: callout box with improved contrast
def cb(text, bg=LIGHT_BLUE, bc=MED_BLUE, width=6.5*inch):
    """Create a callout box with text, background, and border color."""
    style = ParagraphStyle(
        'Callout',
        parent=getSampleStyleSheet()['BodyText'],
        fontSize=11,
        textColor=black,  # CRITICAL: black text for contrast
        spaceAfter=12,
        leftIndent=12,
        rightIndent=12,
    )
    p = Paragraph(text, style)

    t = Table(
        [[p]],
        colWidths=[width - 0.3*inch],
        rowHeights=[None]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor(bg)),
        ('BORDER', (0, 0), (-1, -1), 2, HexColor(bc)),
        ('LEFTPADDING', (0, 0), (-1, -1), 12),
        ('RIGHTPADDING', (0, 0), (-1, -1), 12),
        ('TOPPADDING', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 10),
    ]))
    return t

# Helper function: horizontal rule
def hr(color=MED_BLUE, width=6.5*inch, height=0.05*inch):
    """Create a horizontal rule."""
    t = Table(
        [['']],
        colWidths=[width],
        rowHeights=[height]
    )
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), HexColor(color)),
        ('BORDER', (0, 0), (-1, -1), 0),
    ]))
    return t

# Helper function: styled table with fixed header text color
def mt(data, col_widths=None, header_color=DARK_BLUE, row_height=None):
    """Create a styled table with white bold header text on dark background."""
    if col_widths is None:
        col_widths = [6.5*inch / len(data[0])] * len(data[0])

    # Convert strings to Paragraph objects for word wrapping
    processed_data = []
    for row_idx, row in enumerate(data):
        processed_row = []
        for cell in row:
            if isinstance(cell, str):
                # Header row: use bold
                if row_idx == 0:
                    style = ParagraphStyle(
                        'TableHeaderCell',
                        parent=getSampleStyleSheet()['BodyText'],
                        fontSize=10,
                        fontName='Helvetica-Bold',
                        textColor=white,  # CRITICAL: white text in header
                        alignment=TA_LEFT,
                    )
                else:
                    style = ParagraphStyle(
                        'TableCell',
                        parent=getSampleStyleSheet()['BodyText'],
                        fontSize=10,
                        textColor=black,  # Black text in body
                        alignment=TA_LEFT,
                    )
                processed_row.append(Paragraph(cell, style))
            else:
                processed_row.append(cell)
        processed_data.append(processed_row)

    t = Table(processed_data, colWidths=col_widths, rowHeights=row_height)

    # Style header row (first row) with explicit white bold text
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(header_color)),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#CCCCCC')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('TEXTCOLOR', (0, 1), (-1, -1), black),  # Black text in body rows
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
    ]))

    return t

def create_pdf():
    """Generate the complete PDF report."""
    pdf_path = '/sessions/determined-wonderful-dijkstra/mnt/car/Family_Car_Report_2026.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)

    # Get base styles
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        textColor=HexColor(DARK_BLUE),
        spaceAfter=6,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
    )

    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=HexColor(MED_BLUE),
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold',
    )

    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor(DARK_BLUE),
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
    )

    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        spaceAfter=10,
        leading=14,
    )

    # Build document
    story = []

    # =========== PAGE 1: Title and Summary ===========
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Family Car Project", title_style))
    story.append(Paragraph("A smart swap from petrol to EV", subtitle_style))
    story.append(Spacer(1, 0.1*inch))

    meta_style = ParagraphStyle(
        'Meta',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#555555'),
    )
    story.append(Paragraph("John &amp; family — Spaarndam, Noord-Holland | April 2026", meta_style))
    story.append(Spacer(1, 0.3*inch))

    # Callout: the short version
    story.append(cb(
        "<b>The short version:</b> Switching to a large family EV saves you roughly "
        "<b>€5,100 over 5 years</b> compared to keeping the Picasso — even at today's "
        "fuel price of €2.00/L. That's about <b>€85/month</b> back in your pocket.",
        bg=LIGHT_BLUE
    ))

    story.append(Spacer(1, 0.2*inch))

    # Key bullets
    bullets = [
        "<b>Your Picasso has a known timing belt design flaw.</b> It's at 174,000 km now, and you can sell it right now for ~€6,900 while it's still worth something. Don't fix the timing belt.",
        "<b>The Hyundai Ioniq 5 Lounge is your best match.</b> It ticks the most boxes from your feature list as standard equipment.",
        "<b>Modern EVs last 300,000–500,000 km.</b> Battery degradation is negligible for family cars driven normally.",
        "<b>EV insurance is about 20% more than your Picasso.</b> You're paying €1,050/year instead of €852/year, but electricity is so cheap you more than make up for it.",
        "<b>This is not a drill about the timing belt.</b> Seriously, don't replace it. Sell the car as-is.",
    ]

    for bullet in bullets:
        bullet_para = Paragraph("• " + bullet, body_style)
        story.append(bullet_para)
        story.append(Spacer(1, 0.08*inch))

    story.append(PageBreak())

    # =========== PAGE 2: The Money ===========
    story.append(Paragraph("The money", section_style))
    story.append(Spacer(1, 0.15*inch))

    # Three scenarios, five years table
    story.append(Paragraph("<b>Three scenarios, five years</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    scenarios_data = [
        ['', 'A: Keep Picasso', 'B: Large Family EV', 'C: Small EV + Rental'],
        ['Year 1 total cost', '€6,198', '€24,848', '€12,028'],
        ['Avg annual (yr 1–3)', '€6,213', '€10,654', '€7,434'],
        ['Avg annual (yr 1–5)', '€6,238', '€5,216', '€5,193'],
        ['5-year grand total', '€31,192', '€26,080', '€25,966'],
    ]

    col_widths = [1.5*inch, 1.5*inch, 1.8*inch, 1.8*inch]
    t = mt(scenarios_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "The EV costs more in year 1 because you're buying the car. You break even over the full 5-year period "
        "when you factor in the EV's resale value — saving about €5,100 total.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))

    # Where the money goes each year
    story.append(Paragraph("<b>Where the money goes each year (first 3 years)</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    running_costs_data = [
        ['Cost', 'A: Keep Picasso', 'B: Large EV', 'C: Small EV + Rental'],
        ['Fuel / Electricity', '€3,000', '€999', '€666'],
        ['Car rental', '—', '—', '€2,400'],
        ['Road tax', '€796', '€1,008', '€784'],
        ['Insurance', '€852', '€1,050', '€720'],
        ['Maintenance (incl tyres)', '€450', '€500', '€400'],
        ['Annual total', '€5,098', '€3,557', '€4,970'],
    ]

    col_widths = [1.6*inch, 1.6*inch, 1.6*inch, 1.6*inch]
    t = mt(running_costs_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    # Fuel sensitivity
    story.append(Paragraph("<b>What if fuel prices go up?</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    sensitivity_data = [
        ['Petrol price', 'Picasso 5yr', 'Large EV 5yr', 'You save'],
        ['€2.00/L (current)', '€31,192', '€26,080', '€5,112'],
        ['€2.20/L', '€32,692', '€26,080', '€6,612'],
        ['€2.53/L (recent spike)', '€35,167', '€26,080', '€9,087'],
        ['€2.70/L', '€36,442', '€26,080', '€10,362'],
    ]

    col_widths = [1.5*inch, 1.5*inch, 1.6*inch, 1.5*inch]
    t = mt(sensitivity_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "Even if fuel prices jump, the EV stays cheaper. Electricity prices are more stable than petrol.",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 3: Selling the Picasso ===========
    story.append(Paragraph("Selling the Picasso", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph("<b>What you can get for it</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    selling_data = [
        ['Method', 'High estimate', 'Low estimate', 'Time to sell'],
        ['Private sale', '€7,500', '€5,500', '2–4 weeks'],
        ['Online (Marktplaats, etc.)', '€6,000', '€4,500', '1–2 weeks'],
        ['Dealer (trade-in)', '€5,000', '€3,500', '1 day'],
    ]

    col_widths = [1.4*inch, 1.4*inch, 1.4*inch, 1.6*inch]
    t = mt(selling_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "We've priced this on €6,900 (Independer valuation as of April 2026) as your working assumption. "
        "A private sale could push it higher; a trade-in will be lower. If you want the fastest deal, sell to a dealer.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    # Timing belt callout
    story.append(cb(
        "<b>Don't fix the timing belt.</b> The 1.2 PureTech has a known design flaw. "
        "Buyers know this. Spending €1,200–1,800 to replace it before selling won't raise the price; "
        "it'll just eat into your payout. Sell as-is.",
        bg=LIGHT_YELLOW,
        bc=ACCENT_ORANGE
    ))
    story.append(Spacer(1, 0.15*inch))

    # What affects the price
    story.append(Paragraph("<b>What affects the price</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    affects_data = [
        ['Factor', 'Effect on price'],
        ['Mileage (174,000 km)', '−€500 to −€1,000 (higher than typical for a 2017)'],
        ['Timing belt history', '−€1,000 (if not done; buyers assume it\'s a risk)'],
        ['Service history', '+€200 to +€500 (full service records help)'],
        ['Interior condition', '±€300 (wear &amp; tear, cleanliness)'],
        ['Paint &amp; bodywork', '±€500 (minor dents &amp; scratches cost little; major damage costs more)'],
        ['Tyres', '+€200 to +€400 (new or near-new tyres add value)'],
    ]

    col_widths = [2.0*inch, 4.3*inch]
    t = mt(affects_data, col_widths=col_widths)
    story.append(t)

    story.append(PageBreak())

    # =========== PAGE 4: Feature Wishlist (Simplified) ===========
    story.append(Paragraph("Your feature wishlist vs. reality", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph("<b>How each car scores against your priorities</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    # Create feature matrix with color-coded cells - NARROWER TABLE
    # Using abbreviations and simpler layout to fit page
    matrix_data = [
        ['Feature', 'Priority', 'Ioniq 5', 'EV6', 'Enyaq'],
        ['ACC (predictive)', '#1', 'NSCC (all trims)', 'NSCC-C (all trims)', 'pACC (Assist pkg)'],
        ['Blind spot detection', '#2', 'Standard', 'Standard', 'Option (Side Assist)'],
        ['Traffic sign recog.', '#3', 'Standard', 'Standard', 'Standard'],
        ['Panoramic roof', '#4', 'Lounge+', 'GT-Line std', 'Option'],
        ['Rear camera', '#5', 'Lounge+', 'Wind+', 'All trims'],
        ['Park assist (steering)', '#6', 'SPA (Lounge+)', 'SPA (GT-Line std)', 'Parking Plus pkg'],
        ['Sound system', 'Nice', 'Bose (L+)', 'Meridian (GT)', 'Canton (L&K)'],
    ]

    col_widths = [1.6*inch, 1.0*inch, 1.25*inch, 1.25*inch, 1.25*inch]
    t = Table(matrix_data, colWidths=col_widths)

    # Apply color coding with explicit black text
    style_list = [
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), HexColor(DARK_BLUE)),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('TOPPADDING', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        # Grid and body text
        ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#CCCCCC')),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TEXTCOLOR', (0, 1), (-1, -1), black),  # CRITICAL: black text on colored cells
        ('TOPPADDING', (0, 1), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        # Color cells for data rows (ACC) - row 1
        ('BACKGROUND', (2, 1), (2, 1), HexColor(GREEN_CELL)),
        ('BACKGROUND', (3, 1), (3, 1), HexColor(GREEN_CELL)),
        ('BACKGROUND', (4, 1), (4, 1), HexColor(ORANGE_CELL)),
        # Blind spot detection - row 2
        ('BACKGROUND', (2, 2), (2, 2), HexColor(GREEN_CELL)),
        ('BACKGROUND', (3, 2), (3, 2), HexColor(GREEN_CELL)),
        ('BACKGROUND', (4, 2), (4, 2), HexColor(ORANGE_CELL)),
        # Traffic sign recognition - row 3
        ('BACKGROUND', (2, 3), (2, 3), HexColor(GREEN_CELL)),
        ('BACKGROUND', (3, 3), (3, 3), HexColor(GREEN_CELL)),
        ('BACKGROUND', (4, 3), (4, 3), HexColor(GREEN_CELL)),
        # Panoramic roof - row 4
        ('BACKGROUND', (2, 4), (2, 4), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (3, 4), (3, 4), HexColor(GREEN_CELL)),
        ('BACKGROUND', (4, 4), (4, 4), HexColor(ORANGE_CELL)),
        # Rear camera - row 5
        ('BACKGROUND', (2, 5), (2, 5), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (3, 5), (3, 5), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (4, 5), (4, 5), HexColor(GREEN_CELL)),
        # Park assist - row 6
        ('BACKGROUND', (2, 6), (2, 6), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (3, 6), (3, 6), HexColor(GREEN_CELL)),
        ('BACKGROUND', (4, 6), (4, 6), HexColor(ORANGE_CELL)),
        # Sound system - row 7
        ('BACKGROUND', (2, 7), (2, 7), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (3, 7), (3, 7), HexColor(ORANGE_CELL)),
        ('BACKGROUND', (4, 7), (4, 7), HexColor(ORANGE_CELL)),
    ]

    t.setStyle(TableStyle(style_list))
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    legend_style = ParagraphStyle(
        'Legend',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#666666'),
    )

    story.append(Paragraph(
        "Green = included as standard | Orange = available as option or higher trim | Red = not available",
        legend_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Scorecard:</b> The Ioniq 5 Lounge ticks <b>6 out of 7</b> of your priority features — blind spot detection, "
        "traffic sign recognition, and predictive ACC (NSCC) are standard on every trim. "
        "The EV6 GT-Line scores <b>6 out of 7</b> too (same standard safety kit) but at a higher price. "
        "The Enyaq has traffic sign recognition as standard on all trims, but blind spot detection and ACC "
        "require option packages (often included on Business Edition). "
        "All three have predictive ACC — if the car has ACC, it uses nav data to slow for curves, "
        "roundabouts, and speed limit changes. <b>Ioniq 5 Lounge wins.</b>",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 5: Which trim to target ===========
    story.append(Paragraph("Which trim to target", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Hyundai Ioniq 5 Lounge</b><br/>"
        "Best overall match for your feature list. Blind spot detection, traffic sign recognition, and predictive ACC "
        "(called NSCC — uses nav data to slow for curves, speed limits, and junctions) all come standard "
        "on every Ioniq 5 trim. The Lounge adds rear camera with surround view, Smart Parking Assist (SPA — "
        "measures space and steers for you in parallel &amp; perpendicular), and a Bose "
        "premium sound system. Panoramic Vision Roof available as option. "
        "Expect to pay €26,000–30,000 on the used market (2023–2024 models). You'll break even over 5 years of ownership.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Kia EV6 GT-Line</b><br/>"
        "Similar spec to the Ioniq 5 (both share Hyundai-Kia platform). Blind spot detection, traffic sign recognition, "
        "and predictive ACC (NSCC-C) are standard on all trims. GT-Line adds panoramic roof and Smart Park Assist (SPA — same system as Ioniq 5), "
        "but it's often €1,000–3,000 more expensive. Comes with a Meridian 14-speaker premium sound system with subwoofer. "
        "Slightly sportier handling. If you find a good price on an EV6, it's competitive with the Ioniq 5.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Škoda Enyaq 80</b><br/>"
        "Strong on interior space and practicality. Traffic sign recognition is standard on all trims. "
        "ACC on the Enyaq is predictive by design (pACC) — if it has ACC, it uses nav data to slow for curves, "
        "roundabouts, junctions, and speed limit changes. But ACC itself requires the <b>Assisted Drive</b> package "
        "(often included on Business Edition). "
        "Blind spot detection requires the Side Assist package. "
        "Rear camera is standard on all trims; comes with Canton 12-14 speaker sound system with subwoofer. "
        "A panoramic roof is available as an option (~€990). "
        "Park assist is NOT standard — it's part of the <b>Parking Plus package</b> "
        "(Park Assist + 360° Area View Camera + Trained Parking). "
        "Often fitted on Business Edition models, but always check. "
        "Expect €26,000–32,000 for a well-spec'd 2023–2024 model.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>A few things no EV will give you</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    downsides_data = [
        ['Your Picasso has', 'EVs do not'],
        ['Turning circle under 10.5 m', 'All EVs are 10.4 m or larger (heavier, longer wheelbase)'],
        ['Cheap insurance', 'EV insurance is typically 15–25% more due to repair costs &amp; battery risk'],
        ['Tiny footprint in tight spots', 'EVs are bigger &amp; heavier; harder to park in tight garages'],
        ['Dirt-cheap maintenance', 'Brake fluid, coolant, filters still needed; less frequent but not free'],
    ]

    col_widths = [2.0*inch, 4.3*inch]
    t = mt(downsides_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "These are trade-offs you accept in exchange for massive fuel/electricity savings and a better driving experience.",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 6: Road Safety Features ===========
    story.append(Paragraph("Road safety features", section_style))
    story.append(Spacer(1, 0.15*inch))

    safety_data = [
        ['Safety feature', 'Ioniq 5', 'EV6', 'Enyaq'],
        ['Autonomous emergency braking', 'Standard', 'Standard', 'Standard'],
        ['Blind-spot detection', 'Standard', 'Standard', 'Option (Side Assist)'],
        ['Traffic sign recognition', 'Standard', 'Standard', 'Standard'],
        ['Lane-keeping assist', 'Standard', 'Standard', 'Standard'],
        ['Predictive ACC (nav-based)', 'NSCC (all trims)', 'NSCC-C (all trims)', 'pACC (Assist pkg)'],
        ['360° camera', 'Lounge+', 'GT-Line+', 'Option'],
        ['Rear cross-traffic alert', 'Standard', 'Standard', 'Option (Side Assist)'],
    ]

    col_widths = [2.0*inch, 1.4*inch, 1.4*inch, 1.4*inch]
    t = mt(safety_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>Ice detection:</b> None of these cars detect ice on the road ahead. Winter driving in the Netherlands "
        "means you rely on road conditions reporting and your own caution. All three have good winter tyre options.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Headlights:</b> All three come with LED headlights on standard trims. Ioniq 5 Lounge and EV6 GT-Line "
        "add LED matrix headlights (adaptive beams) as standard. Enyaq 80 offers LED matrix as an option.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Bottom line:</b> All three are safe cars. The Ioniq 5 and EV6 come with blind spot detection, traffic sign recognition, "
        "rear cross-traffic alert, and predictive ACC as standard on every trim — a clear safety advantage. "
        "The Enyaq has traffic sign recognition standard, but blind spot detection and ACC need option packages. "
        "All are better than your Picasso.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(cb(
        "<b>What is predictive ACC?</b> All three cars have it — it's ACC that reads the navigation map "
        "and speed limit signs to adjust your speed <i>before</i> things happen. It slows down before curves, "
        "reduces speed entering a 50 km/h zone, and brakes ahead of roundabouts — without you touching anything.<br/><br/>"
        "<b>Ioniq 5:</b> Navigation-based Smart Cruise Control (NSCC) — standard on all trims. Works via Highway Driving Assist.<br/>"
        "<b>EV6:</b> NSCC-C (with Curve slowdown) — standard on all trims. Same system as Ioniq 5.<br/>"
        "<b>Enyaq:</b> Predictive ACC (pACC) — the Enyaq's ACC is predictive by design. If the car has ACC, "
        "it already has pACC. ACC itself requires the Assisted Drive package (often on Business Edition). "
        "pACC also handles roundabouts and junctions, not just highway curves.",
        bg=LIGHT_YELLOW, bc=ACCENT_ORANGE
    ))

    story.append(PageBreak())

    # =========== PAGE 7: Motorway Comfort ===========
    story.append(Paragraph("How quiet are they on the motorway?", section_style))
    story.append(Spacer(1, 0.15*inch))

    comfort_data = [
        ['Feature', 'Ioniq 5', 'EV6', 'Enyaq'],
        ['Cabin noise at 120 km/h', '~67 dB (quietest)', '~68-69 dB', '~67-68 dB'],
        ['Sound insulation', 'Very good', 'Good', 'Good'],
        ['Noise-cancellation tech', 'No', 'No', 'No'],
        ['Premium sound system', 'Bose 8 speakers (Lounge+)', 'Meridian 14 speakers + sub (GT-Line)', 'Canton 12-14 speakers + sub (L&K)'],
        ['Comfort rating', 'Excellent', 'Excellent', 'Very good'],
    ]

    col_widths = [1.8*inch, 1.4*inch, 1.4*inch, 1.4*inch]
    t = mt(comfort_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>Noise:</b> EVs are dramatically quieter than your Picasso. The Ioniq 5 is the quietest of the three at ~67 dB — "
        "comparable to a mid-range luxury car. The Enyaq is close behind at ~67-68 dB. The EV6 picks up slightly more road noise "
        "from the floor at ~68-69 dB.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Sound systems:</b> The <b>EV6 GT-Line</b> has the best audio: a 14-speaker <b>Meridian</b> surround system with subwoofer. "
        "The <b>Enyaq</b> offers a solid <b>Canton</b> system (12-14 speakers + sub) on L&K trim. The <b>Ioniq 5</b> gets a <b>Bose</b> "
        "8-speaker setup on Lounge+ — the weakest of the three premium options but still excellent.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(cb(
        "<b>Motorway comfort is excellent on all three.</b> You won't regret any of them on a long drive.",
        bg=LIGHT_BLUE
    ))

    story.append(PageBreak())

    # =========== PAGE 8: Cabin Preconditioning ===========
    story.append(Paragraph("Warm the cabin before I get in", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>How it works:</b> All three cars let you preheat the cabin while plugged in at home (via the car's app). "
        "The battery powers a heating element; you don't lose range because the energy comes from the wall charger, not the battery.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>The catch:</b> You need a home wallbox to do it reliably. You can't preheat from a regular 230V outlet "
        "(it's too slow). If you use a rapid charger on the motorway, you can't preheat—the car will warm up the battery "
        "and cabin automatically when you start driving, which takes a few minutes.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(cb(
        "<b>Bottom line:</b> Yes, you can warm your car before getting in. Yes, you should install a home wallbox. "
        "No, you won't be cold if you forget to preheat—the cabin heats up quickly once you're driving.",
        bg=LIGHT_BLUE
    ))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Heating & AC options</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    ac_data = [
        ['Feature', 'Ioniq 5', 'EV6', 'Enyaq'],
        ['AC zones', '2 (standard)', '2 (standard)', '3 (80 model)'],
        ['Heat pump', 'Lounge+', 'GT-Line+', '80 only'],
        ['Heated windshield', 'No', 'No', 'Yes (80 only)'],
        ['Preconditioning via app', 'Yes', 'Yes', 'Yes'],
    ]

    col_widths = [1.8*inch, 1.4*inch, 1.4*inch, 1.4*inch]
    t = mt(ac_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>Heat pump:</b> A heat pump is more efficient in cold weather—it recycles heat from the battery and drivetrain. "
        "The Ioniq 5 Lounge and EV6 GT-Line both include a heat pump. The Enyaq only offers it on the 80 (the pricier model). "
        "In Dutch winters, a heat pump saves you 5–10% range in cold weather.",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 9: Driving Experience ===========
    story.append(Paragraph("How they drive: city, motorway, and everything in between", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph("<b>Performance &amp; handling</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    performance_data = [
        ['Metric', 'Ioniq 5', 'EV6', 'Enyaq 80', 'Your Picasso'],
        ['Weight', '~1,800 kg', '~1,750 kg', '~1,900 kg', '~1,370 kg'],
        ['0–100 km/h', '~7.2 sec', '~6.3 sec', '~8.5 sec', '~10.5 sec'],
        ['Turning circle', '10.5 m', '10.7 m', '10.4 m', '10.8 m'],
        ['Braking (100–0 km/h)', '~36 m', '~35 m', '~37 m', '~39 m'],
        ['Top speed', '185 km/h', '185 km/h', '160 km/h', '180 km/h'],
    ]

    col_widths = [1.5*inch, 1.3*inch, 1.3*inch, 1.3*inch, 1.3*inch]
    t = mt(performance_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>City driving:</b> EVs feel heavier than they look, but their low center of gravity (battery in the floor) "
        "makes them stable. All three are responsive to the steering wheel. Turning circles are tight enough for city parking, "
        "though none match your Picasso's 10.8 m. Regen braking (one-pedal driving) makes city stops smooth and predictable.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Motorway driving:</b> All three cruise effortlessly at 130 km/h. Acceleration merges are quick (0–100 km/h in 6–8 sec). "
        "Noise is lower than your Picasso—no engine drone. Road and tyre noise dominate. Blind spots are typical for cars this size; "
        "all three have blind-spot detection (standard on Ioniq 5 &amp; EV6, option on Enyaq) and traffic sign recognition to show you the current speed limit.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>One-pedal driving:</b> Release the accelerator and the car slows down via regen braking. Lifts no force off the floor. "
        "Takes 2–3 days to adjust; most drivers love it after a week. Makes motorway traffic less tiring. All three have this as standard.",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 10: Which EV to Buy ===========
    story.append(Paragraph("Which EV to buy", section_style))
    story.append(Spacer(1, 0.15*inch))

    ev_comparison_data = [
        ['Factor', 'Ioniq 5', 'EV6', 'Enyaq 80'],
        ['Used market price (2023–2024)', '€26,000–30,000', '€27,000–33,000', '€26,000–32,000'],
        ['Battery warranty', '8 years / 160k km', '8 years / 160k km', '8 years / 160k km'],
        ['Warranty (rest of car)', '5 years / 100k km', '5 years / 100k km', '3 years / 60k km'],
        ['Dealer network (NL)', 'Excellent (Hyundai)', 'Excellent (Kia)', 'Very good (Škoda)'],
        ['Resale value (2027–2030)', 'Good', 'Good', 'Good'],
        ['Insurance (est. €/month)', '€87–92', '€87–92', '€80–85'],
        ['Typical range (WLTP)', '400+ km', '400+ km', '420+ km'],
        ['Charging speed (11 kW)', '~7 hours', '~7 hours', '~7 hours'],
        ['Charging speed (50 kW DC)', '~35 minutes', '~33 minutes', '~38 minutes'],
    ]

    col_widths = [1.8*inch, 1.4*inch, 1.4*inch, 1.4*inch]
    t = mt(ev_comparison_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>Hyundai Ioniq 5:</b> Best match for your feature list. Lounge trim at €26,000–30,000 includes nearly everything you want. "
        "Excellent dealer network; good resale value. This is your first choice.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Kia EV6:</b> Technically superior (slightly faster, sportier). Shares the same platform &amp; warranty as Ioniq 5. "
        "GT-Line trim gives you ACC and panoramic roof. Usually €1,000–2,000 more than Ioniq 5. Worth considering if you find a good deal.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Škoda Enyaq 80:</b> Strong on interior space and practicality. Similar pricing to Ioniq 5 (€26,000–32,000 well-equipped). "
        "Panoramic roof and park assist are both available — look for Business Edition models with the right options ticked. "
        "Škoda's warranty is shorter (3 years vs. 5). Good value if you can find one with the right spec.",
        body_style
    ))

    story.append(PageBreak())

    # =========== PAGE 11: Lifespan ===========
    story.append(Paragraph("How long will each car last?", section_style))
    story.append(Spacer(1, 0.15*inch))

    lifespan_data = [
        ['Milestone', 'Ioniq 5', 'EV6', 'Enyaq', 'Picasso'],
        ['Expected lifespan', '300,000–500,000 km', '300,000–500,000 km', '300,000–500,000 km', '200,000–250,000 km'],
        ['Battery degradation at 200k km', '~5–8%', '~5–8%', '~5–8%', 'N/A'],
        ['Most common failure (petrol cars)', 'N/A', 'N/A', 'N/A', 'Timing belt (known flaw)'],
        ['Rust risk (NL climate)', 'Low', 'Low', 'Low', 'Medium (older platform)'],
        ['Parts availability (2030)', 'Excellent', 'Excellent', 'Very good', 'Good'],
    ]

    col_widths = [1.8*inch, 1.4*inch, 1.4*inch, 1.4*inch, 1.4*inch]
    t = mt(lifespan_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "Modern EV batteries are robust. A 5-8% loss of capacity over the car's first 200,000 km is normal and not a concern. "
        "You'll still get 90%+ of your original range. Lifespan is limited more by chassis rust and component failure (suspension, brakes) "
        "than by the battery.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph("<b>Before you buy any used EV</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    checklist = [
        "Get a full service history (maintenance &amp; firmware updates).",
        "Check battery health report — ask for SoH %. Above 85% is good; 90%+ is excellent. The difference between 90% and 97% is only ~30 km range.",
        "Inspect the undercarriage for corrosion, scrapes, and battery tray damage. Use your phone torch. Dutch salt roads accelerate rust — focus on sills, wheel arches, and subframe.",
        "Listen for clunky or rattling suspension — bounce each corner, drive over speed bumps. Dampers and bushings are the main wear items on an EV.",
        "Check for uneven tyre wear — indicates alignment or suspension issues. EVs chew through tyres 20–30% faster. Budget €600–900 per set.",
        "Test DC fast charging during viewing — confirm it reaches advertised speed within 5 minutes.",
        "Verify no accident history (use RDW.nl or ANWB dossier).",
        "Ask about battery warranty transfer (most are transferable but check the fine print).",
        "Check if the connected car app still works (Bluelink / Kia Connect / MySkoda) — transfer to your account.",
        "Test all electric features: tailgate, sunroof, seat adjustment, mirrors. Electric motors fail quietly.",
        "<b>Enyaq only:</b> Check it has the <b>Parking Plus package</b> (Park Assist + 360° camera + Trained Parking). Park Assist is NOT standard on any pre-2025 Enyaq trim — it must be an option the original buyer paid for. On the Ioniq 5 (Lounge+) and EV6 (GT-Line), park assist is standard.",
        "<b>Don't overpay for low mileage.</b> An EV at 100k km with 90% SoH is just as good as 40k km with 97% SoH — there's no engine or gearbox to wear out.",
    ]

    for item in checklist:
        bullet_para = Paragraph("• " + item, body_style)
        story.append(bullet_para)
        story.append(Spacer(1, 0.08*inch))

    story.append(PageBreak())

    # =========== PAGE 12: Connected Car Apps ===========
    story.append(Paragraph("Connected car apps: what you need to know", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "All three cars have companion apps for remote features (lock/unlock, climate control, charging status, "
        "find my car). The good news: <b>nothing essential requires a subscription.</b> ACC, parking assist, navigation, "
        "and charging schedules all work from the car's own screen without any app.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    app_data = [
        ['', 'Ioniq 5 (Bluelink)', 'EV6 (Kia Connect)', 'Enyaq (MySkoda)'],
        ['Free tier', '10 yrs basic', '7 yrs full', '1 yr trial'],
        ['Remote climate/lock', '€29/yr (Plus)', 'Included 7 yrs', '€39/yr (Care)'],
        ['Nav + traffic', '€99/yr (Pro)', 'Included 7 yrs', '€49/yr (Infotainment)'],
        ['Full annual cost', '€29–99/yr', '€0 (7 yrs)', '€39–88/yr'],
        ['Remote parking via app', 'Via fob (no app)', 'Via fob (no app)', 'App required'],
        ['Self-host (Home Asst.)', 'Yes', 'Yes', 'Yes (VW Group)'],
    ]

    col_widths = [1.6*inch, 1.6*inch, 1.6*inch, 1.6*inch]
    t = mt(app_data, col_widths=col_widths)
    story.append(t)
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph(
        "<b>Best value:</b> The <b>Kia EV6</b> includes 7 years of full connectivity free — no subscription needed. "
        "The <b>Ioniq 5</b> gives you 10 years of basics free, but remote climate costs €29/year. "
        "The <b>Enyaq</b> is the most expensive — you need two separate subscriptions (€88/year total) for full features.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Can you skip the app entirely?</b> Yes. You can set charging schedules, use navigation, and control "
        "climate from the car's own screen. The app adds remote convenience (preheat from bed, check charging "
        "from your phone) but isn't essential. All three also have open-source Home Assistant integrations "
        "if you want to self-host.",
        body_style
    ))
    story.append(Spacer(1, 0.15*inch))

    story.append(cb(
        "<b>Second-hand buyers:</b> Ask the seller to remove their app account before handover. "
        "Then register the car to your own account. Free trial periods transfer to new owners on Hyundai and Kia. "
        "Skoda may require contacting a dealer.",
        bg=LIGHT_YELLOW,
        bc=ACCENT_ORANGE
    ))

    story.append(PageBreak())

    # =========== PAGE 13: What to Do Next ===========
    story.append(Paragraph("What to do next", section_style))
    story.append(Spacer(1, 0.15*inch))

    story.append(Paragraph(
        "<b>Sell the Picasso as-is</b> (€5,500–6,500 private sale, don't fix the timing belt). "
        "Then pick up a Hyundai Ioniq 5 Lounge in the €26,000–30,000 range—it ticks the most boxes from your feature list as standard. "
        "Net outlay after selling: ~€20,000–23,000. Over 5 years of ownership you'll save ~€5,100 through lower running costs, "
        "and the EV will still be worth ~€13,500 when you're done.",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))

    story.append(Paragraph("<b>Step-by-step</b>", body_style))
    story.append(Spacer(1, 0.1*inch))

    steps = [
        "1. List the Picasso on Marktplaats or Autoscout24 (private sale) or take it to a dealer for a quick trade-in quote.",
        "2. Search for used Ioniq 5 Lounge models (2023–2024) in your region. Check AutoScout24, Mobile.de, and local dealer inventory.",
        "3. Have a pre-purchase inspection (APK-keuring) done on any car you find.",
        "4. Arrange home charging: budget €1,000–1,500 for a 7 kW wallbox + installation. This is non-negotiable; it's the only way to charge conveniently.",
        "5. Check your home electricity contract. At 1,000 km/month, you'll use ~150–180 kWh/month. Ensure your supplier can handle it (most can).",
        "6. Buy winter tyres for the EV (not included). Budget €600–900 for a set.",
        "7. After taking delivery, register the car in your name and update insurance.",
    ]

    for step in steps:
        step_para = Paragraph(step, body_style)
        story.append(step_para)
        story.append(Spacer(1, 0.08*inch))

    story.append(Spacer(1, 0.2*inch))

    story.append(cb(
        "<b>One more time:</b> Don't replace the timing belt. Seriously. It's a known design flaw; "
        "it's in the buyer's mind already, and spending €1,200 to fix it won't help the resale price. Sell as-is.",
        bg=LIGHT_YELLOW,
        bc=ACCENT_ORANGE
    ))

    # Build PDF
    doc.build(story)
    return pdf_path

if __name__ == '__main__':
    pdf_path = create_pdf()
    print(f"PDF created successfully: {pdf_path}")
