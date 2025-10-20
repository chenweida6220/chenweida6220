import svgwrite

dwg = svgwrite.Drawing("test_namecard.svg", size=("700px", "400px"), profile="tiny")

# Colors & fonts
bg_color = "#1e1e1e"
text_color = "#00ff90"
font_family = "Courier New, monospace"

# --- Terminal frame background ---
dwg.add(dwg.rect(insert=(20, 40), size=("660px", "330px"), rx=8, ry=8,
                 fill=bg_color, stroke="#00ff90", stroke_width=2))

# --- Top bar (outside frame) ---
dwg.add(dwg.rect(insert=(20, 10), size=("660px", "25px"), rx=6, ry=6,
                 fill="#333333"))
dwg.add(dwg.text("🔴🟡🟢", insert=(30, 27), font_size="16px",
                 font_family=font_family))  # mimic macOS dots

# --- ASCII Image (pre-converted PNG) ---
dwg.add(dwg.image(href="Portfolio Items/headshot-ascii-art.png",
                  insert=(40, 70), size=("300px", "300px")))

# --- About Me Section ---
about_text = [
    "Wei Chen",
    "----------------------------",
    "💻 IT Staff Auditor @ NYC Comptroller’s Office",
    "🎓 MS Business Analytics | BS Psychology & Public Science",
    "📍 NYC | ☁️ Cloud & Data Enthusiast",
    "🧠 Building: WriteVibe — writing app for neurodivergent users"
]

x_offset = 370
y_start = 100
line_height = 28

for i, line in enumerate(about_text):
    dwg.add(dwg.text(line, insert=(x_offset, y_start + i * line_height),
                     fill=text_color, font_size="16px", font_family=font_family))

dwg.save()
