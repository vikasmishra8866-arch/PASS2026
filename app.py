import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import io

# --- PAGE CONFIG ---
st.set_page_config(page_title="Premium UPI Card Generator", page_icon="💳", layout="centered")

# --- UI CUSTOM CSS ---
st.markdown("""
    <style>
    .stApp { 
        background: linear-gradient(135deg, #0a0e17, #131b2c); 
        color: white; 
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    .main-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 35px; 
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(15px);
        box-shadow: 0 25px 50px rgba(0,0,0,0.3);
        margin-top: 25px;
        max-width: 550px;
        margin-left: auto;
        margin-right: auto;
    }
    h1 { 
        text-align: center; 
        font-weight: 800;
        background: linear-gradient(to right, #8b5cf6, #06b6d4); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
        margin-bottom: 25px;
    }
    .stImage {
        border-radius: 20px;
        margin-top: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Helper function to get centered coordinates for text safely
def draw_centered_text(draw, canvas_w, y, text, font, fill):
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_w = text_bbox[2] - text_bbox[0]
    text_x = (canvas_w - text_w) // 2
    draw.text((text_x, y), text, font=font, fill=fill)

def generate_premium_card(upi_id, amount, custom_note):

    # Canvas Layout
    w, h = 600, 950

    # ================= UNIQUE PREMIUM BACKGROUND =================

    card = Image.new('RGB', (w, h), '#070b14')
    draw = ImageDraw.Draw(card)

    # Gradient Background
    for y in range(h):

        r = int(10 + (y / h) * 35)
        g = int(14 + (y / h) * 25)
        b = int(22 + (y / h) * 55)

        draw.line([(0, y), (w, y)], fill=(r, g, b))

    # Premium Glow Circles
    glow_layer = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)

    glow_draw.ellipse(
        (-80, -80, 250, 250),
        fill=(139, 92, 246, 90)
    )

    glow_draw.ellipse(
        (350, 650, 700, 1000),
        fill=(6, 182, 212, 80)
    )

    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(80))

    card.paste(glow_layer, (0, 0), glow_layer)

    draw = ImageDraw.Draw(card)

    # ================= HEADER =================

    header_h = 260

    draw.rounded_rectangle(
        [25, 25, w-25, header_h],
        radius=35,
        fill=(17, 24, 39)
    )

    draw.rectangle(
        [25, header_h-18, w-25, header_h],
        fill='#06b6d4'
    )

    # ================= PREMIUM FONT SYSTEM =================

    try:
        # Premium Fonts
        font_title = ImageFont.truetype("georgiab.ttf", 44)

        font_subtitle = ImageFont.truetype("ariali.ttf", 24)

        font_label = ImageFont.truetype("arial.ttf", 22)

        font_amount = ImageFont.truetype("arialbd.ttf", 52)

        font_upi = ImageFont.truetype("arial.ttf", 28)

        font_footer = ImageFont.truetype("ariali.ttf", 20)

    except IOError:

        try:
            # Linux Fallback
            font_title = ImageFont.truetype("LiberationSerif-Bold.ttf", 44)

            font_subtitle = ImageFont.truetype("LiberationSans-Italic.ttf", 24)

            font_label = ImageFont.truetype("LiberationSans-Regular.ttf", 22)

            font_amount = ImageFont.truetype("LiberationSans-Bold.ttf", 52)

            font_upi = ImageFont.truetype("LiberationSans-Regular.ttf", 28)

            font_footer = ImageFont.truetype("LiberationSans-Italic.ttf", 20)

        except IOError:

            font_title = ImageFont.load_default()

            font_subtitle = ImageFont.load_default()

            font_label = ImageFont.load_default()

            font_amount = ImageFont.load_default()

            font_upi = ImageFont.load_default()

            font_footer = ImageFont.load_default()

    # ================= HEADER TEXTS =================

    draw_centered_text(
        draw,
        w,
        65,
        "SCAN FOR PAYMENT",
        font_title,
        fill="#ffffff"
    )

    draw_centered_text(
        draw,
        w,
        130,
        "━━━━━━━━━━━━━━━━━━━━━━",
        font_subtitle,
        fill="#8b5cf6"
    )

    draw_centered_text(
        draw,
        w,
        170,
        "USING ANY UPI APP",
        font_subtitle,
        fill="#67e8f9"
    )

    # ================= QR CODE =================

    upi_url = f"upi://pay?pa={upi_id}&pn=UPI%20Payment&am={amount}&cu=INR&tn={custom_note}"

    qr = qrcode.QRCode(
        version=3,
        box_size=8,
        border=1
    )

    qr.add_data(upi_url)

    qr.make(fit=True)

    qr_img = qr.make_image(
        fill_color="#0f172a",
        back_color="white"
    ).convert('RGB')

    qr_w, qr_h = qr_img.size

    bx, by = (w - qr_w) // 2, 310

    # ================= PREMIUM SHADOW =================

    for offset in range(10, 0, -1):

        shadow_color = (
            15 + offset * 4,
            23 + offset * 2,
            42 + offset * 2
        )

        draw.rounded_rectangle(
            [
                bx - 18 + offset,
                by - 18 + offset,
                bx + qr_w + 18 + offset,
                by + qr_h + 18 + offset
            ],
            radius=24,
            fill=shadow_color
        )

    # ================= QR FRAME =================

    draw.rounded_rectangle(
        [
            bx - 18,
            by - 18,
            bx + qr_w + 18,
            by + qr_h + 18
        ],
        radius=24,
        outline='#8b5cf6',
        fill='#ffffff',
        width=4
    )

    card.paste(qr_img, (bx, by))

    # ================= BOTTOM SECTION =================

    content_start_y = by + qr_h + 65

    # Amount Label
    draw_centered_text(
        draw,
        w,
        content_start_y,
        "AMOUNT TO PAY",
        font_label,
        fill="#94a3b8"
    )

    # Amount
    amount_str = f"{float(amount):,.2f}"

    draw_centered_text(
        draw,
        w,
        content_start_y + 45,
        amount_str,
        font_amount,
        fill="#ffffff"
    )

    # Divider
    divider_y = content_start_y + 145

    draw.line(
        [(100, divider_y), (500, divider_y)],
        fill="#334155",
        width=3
    )

    # UPI ID
    upi_label_str = f"UPI ID: {upi_id}"

    draw_centered_text(
        draw,
        w,
        divider_y + 35,
        upi_label_str,
        font_upi,
        fill="#e2e8f0"
    )

    # Note
    note_text = custom_note.strip() if custom_note else ""

    note_label_str = f"Note: {note_text}" if note_text else "Note: N/A"

    draw_centered_text(
        draw,
        w,
        divider_y + 85,
        note_label_str,
        font_subtitle,
        fill="#94a3b8"
    )

    # ================= FOOTER =================

    draw.rectangle(
        [0, h-80, w, h],
        fill='#0f172a'
    )

    draw_centered_text(
        draw,
        w,
        h-50,
        "🔒 SECURE UPI GATEWAY",
        font_footer,
        fill="#67e8f9"
    )

    return card

# --- APP UI ---
st.markdown("<h1>Premium Payment Standee</h1>", unsafe_allow_html=True)

with st.container():

    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    upi_suggestions = [
        "9696159863.wallet@phonepe",
        "9696159863@ibl"
    ]

    selected_upi = st.selectbox(
        "Select UPI ID",
        upi_suggestions
    )

    custom_upi = st.text_input(
        "Or Enter Custom ID",
        value=selected_upi
    )

    final_upi = custom_upi if custom_upi else selected_upi

    amount = st.number_input(
        "Amount (INR)",
        min_value=1.0,
        value=100.0,
        step=10.0
    )

    note = st.text_input(
        "Optional Payment Note (e.g., 'Coffee', 'Service')",
        value="Service Fee"
    )

    if st.button(
        "✨ Generate Balanced Card View",
        use_container_width=True
    ):

        final_image = generate_premium_card(
            final_upi,
            amount,
            note
        )

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st.image(
                final_image,
                use_container_width=True
            )

            # Download Button
            img_buffer = io.BytesIO()

            final_image.save(
                img_buffer,
                format="PNG"
            )

            st.download_button(
                label="⬇ Download Premium UPI Card",
                data=img_buffer.getvalue(),
                file_name="premium_upi_card.png",
                mime="image/png",
                use_container_width=True
            )

    st.markdown('</div>', unsafe_allow_html=True)
