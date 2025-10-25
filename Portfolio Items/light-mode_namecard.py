import svgwrite

SVG_WIDTH = 800
SVG_HEIGHT = 400
LEFT_PADDING = 10
RIGHT_PADDING = 10
outline = 2

# Output SVG file
dwg = svgwrite.Drawing(
    'light-mode_namecard.svg', size=('800px', '400px'))

# Colors
BG_COLOR = "#ffffff"
TERMINAL_HEADER = '#f0f0f0'
TEXT_COLOR = '#111111'
FONT = 'monospace'

# --- Base terminal window ---
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill=BG_COLOR, rx=8, ry=8,stroke=TEXT_COLOR, stroke_width=outline))

# --- Top bar ---
dwg.add(dwg.rect(insert=(outline, outline), size=(SVG_WIDTH - outline, '20px'), rx=8, ry=8,fill=TERMINAL_HEADER))
dwg.add(dwg.text("🔴🟡🟢",
                 insert=(800 - RIGHT_PADDING, 15),
                 text_anchor="end",
                 font_size="14px", font_family=FONT))
dwg.add(dwg.text("chenweida6220@github: ~", insert=(LEFT_PADDING, 15),
                 fill=TEXT_COLOR, font_size="14px", font_family=FONT))

# --- Add ASCII Image (left side) ---
# Display the ASCII image (converted PNG)
# dwg.add(dwg.image(href='Portfolio Items/headshot-ascii-art.png',
#                   insert=(10, 22), size=("380px", '380px')))

# Replaced the above step with manually converting ASCII svg file to base64 because GitHub markdown can't display external images inside SVG for security reasons.
with open('Portfolio Items/headshot-ascii-base64.txt', 'r') as f:
    base64_string = ''.join(f.read().split())  # removes all whitespace/newlines
# Prepend the required header for data URI
data_uri = f"data:image/png;base64,{base64_string}"
# Add the image to the SVG
dwg.add(dwg.image(href=data_uri,
                  insert=(LEFT_PADDING, 22), size=("380px", '380px')))

# Automatic timestamp
AUTO_UPDATE = True

if AUTO_UPDATE:
    from datetime import datetime
    import pytz
    nyc_tz = pytz.timezone("America/New_York")
    LAST_LOGIN = datetime.now(nyc_tz).strftime("%a %b %d %H:%M %Z %Y")
else:
    LAST_LOGIN = "Fri Oct 24 17:32 EDT 2025"

# --- About Me Section (right side) ---
about_x = 400
about_y = 45
line_height = 28

section_headers = [
    ("User Information", "user_information"),
    ("Specializations", "specializations")
]
user_information = [
    ("Identity", "Wei Da Chen aka William"),
    ("Coordinates", "Zone-NYC // N43.7920 W18.6543"),
    ("Email", "weida.wdc@gmail.com"),
    ("Last Login", LAST_LOGIN),
]
specializations = [
    ("Focus", "Data Analysis"),
    ("Expertise", "Risk Assessment, IT Auditing"),
    ("Tools", "SQL, Python, Tableau, Git"),
]

# Function to format with dash leaders
def dash_leader(left, right, width=40):
    dots = '-' * (width - len(left) - len(right))
    return f"{left}{dots}{right}"
# Function to format with dot leaders
def dot_leader(left, right, width):
    dots = '.' * (width - len(left) - len(right))
    return f"{left}{dots}{right}"

current_y = about_y  # Start vertical position
for section_label, section_var in section_headers:
    # Render section header with dashed leader
    header_text = dash_leader(f"[ {section_label} ] ", "", 50)
    dwg.add(dwg.text(header_text,
                     insert=(about_x, current_y),
                     fill=TEXT_COLOR, font_size="14px", 
                     font_family=FONT,
                     textLength=SVG_WIDTH - about_x - RIGHT_PADDING,
                     lengthAdjust="spacingAndGlyphs"
                 ))
    current_y += line_height

    # Get the actual section data (e.g., user_information)
    section_data = globals().get(section_var, [])

    # Render each key-value pair
    for label, value in section_data:
        text = dot_leader(label, value, 50)
        dwg.add(dwg.text(text,
                         insert=(about_x, current_y),
                         fill=TEXT_COLOR, font_size="14px", 
                         font_family=FONT,
                         textLength=SVG_WIDTH - about_x - RIGHT_PADDING,
                         lengthAdjust="spacingAndGlyphs"))
        current_y += line_height

    # Add spacing after section
    current_y += line_height

# Terminal-style footer ---
dwg.add(dwg.text("$ echo 'Welcome to my GitHub! :)'",
                 insert=(about_x, SVG_HEIGHT - 15),
                 fill=TEXT_COLOR, font_size="13px", font_family=FONT))

# --- Save SVG ---
dwg.save()

print("✅ SVG namecard generated: light-mode_namecard.svg")
