import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO

# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Premium UPI QR Generator",
    page_icon="💎",
    layout="centered"
)

# ================= PREMIUM CSS =================

st.markdown("""
<style>

.stApp{
    background:
    radial-gradient(circle at top left,#7c3aed22,transparent 25%),
    radial-gradient(circle at bottom right,#06b6d422,transparent 25%),
    linear-gradient(135deg,#050816,#0f172a,#111827);
    color:white;
}

.block-container{
    padding-top:2rem;
}

/* ================= TITLE ================= */

.main-title{
    text-align:center;
    font-size:52px;
    font-weight:900;
    line-height:1.1;
    background:linear-gradient(to right,#a855f7,#06b6d4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:12px;
}

.subtitle{
    text-align:center;
    color:#94a3b8;
    margin-bottom:40px;
    font-size:18px;
}

/* ================= FORM CARD ================= */

.glass-card{
    background:rgba(255,255,255,0.06);
    padding:35px;
    border-radius:32px;
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter:blur(24px);
    box-shadow:0 0 50px rgba(168,85,247,0.18);
}

/* ================= PAYMENT CARD ================= */

.payment-card{
    background:rgba(255,255,255,0.08);
    padding:35px;
    border-radius:35px;
    border:1px solid rgba(255,255,255,0.12);
    backdrop-filter:blur(25px);
    box-shadow:0 0 60px rgba(6,182,212,0.2);
    text-align:center;
    margin-top:30px;
}

/* ================= QR BOX ================= */

.qr-box{
    background:white;
    padding:25px;
    border-radius:32px;
    display:inline-block;
    margin-top:25px;
    box-shadow:0 10px 40px rgba(0,0,0,0.35);
}

/* ================= AMOUNT ================= */

.amount-text{
    font-size:22px;
    color:#cbd5e1;
    margin-top:24px;
}

.price{
    font-size:68px;
    font-weight:900;
    background:linear-gradient(to right,#a855f7,#06b6d4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-top:5px;
}

/* ================= FOOTER ================= */

.footer-text{
    margin-top:30px;
    color:#94a3b8;
    font-size:16px;
}

/* ================= BUTTON ================= */

.stButton>button{
    width:100%;
    border:none;
    border-radius:18px;
    background:linear-gradient(to right,#9333ea,#06b6d4);
    color:white;
    font-size:18px;
    font-weight:700;
    padding:15px;
    transition:0.3s;
}

.stButton>button:hover{
    transform:scale(1.02);
    box-shadow:0 0 30px rgba(168,85,247,0.45);
}

/* ================= INPUTS ================= */

.stTextInput input{
    border-radius:16px !important;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:16px !important;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================

st.markdown(
    "<div class='main-title'>Premium UPI QR Generator</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Luxury Secure Payment Gateway</div>",
    unsafe_allow_html=True
)

# ================= FORM =================

upi_options = [
    "9696159863-2@ibl",
    "9696159863-3@ybl",
    "9696159863@phonepe"
]

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

selected_upi = st.selectbox(
    "Select UPI ID",
    upi_options
)

custom_upi = st.text_input(
    "Custom UPI ID"
)

amount = st.number_input(
    "Amount",
    min_value=1,
    step=1
)

remark = st.text_input(
    "Note / Remark"
)

generate = st.button(
    "Generate Premium QR"
)

st.markdown("</div>", unsafe_allow_html=True)

# ================= QR GENERATION =================

if generate:

    final_upi = custom_upi if custom_upi else selected_upi

    upi_link = (
        f"upi://pay?"
        f"pa={final_upi}"
        f"&pn=Vinay"
        f"&am={amount}"
        f"&tn={remark}"
        f"&cu=INR"
    )

    # ================= QR =================

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=14,
        border=2
    )

    qr.add_data(upi_link)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color="black",
        back_color="white"
    ).convert("RGB")

    # ================= WEBSITE CARD =================

    st.markdown(
        "<div class='payment-card'>",
        unsafe_allow_html=True
    )

    st.markdown(
        "## ✨ Scan For Payment Any UPI App"
    )

    st.markdown(
        "<div class='qr-box'>",
        unsafe_allow_html=True
    )

    st.image(img, width=320)

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='amount-text'>Amount To Pay</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<div class='price'>₹{amount}</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"### {final_upi}"
    )

    if remark:
        st.markdown(
            f"📝 {remark}"
        )

    st.markdown(
        "<div class='footer-text'>🔒 Secure UPI Gateway</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "</div>",
        unsafe_allow_html=True
    )

    # ================= PREMIUM DOWNLOADABLE CARD =================

    card_width = 1200
    card_height = 1800

    card = Image.new(
        "RGB",
        (card_width, card_height),
        "#050816"
    )

    draw = ImageDraw.Draw(card)

    # ================= PREMIUM BACKGROUND =================

    for y in range(card_height):

        r = int(5 + (y / card_height) * 35)
        g = int(8 + (y / card_height) * 20)
        b = int(22 + (y / card_height) * 65)

        draw.line(
            [(0, y), (card_width, y)],
            fill=(r, g, b)
        )

    # ================= GLOW EFFECT =================

    glow = Image.new(
        "RGBA",
        (card_width, card_height),
        (0, 0, 0, 0)
    )

    glow_draw = ImageDraw.Draw(glow)

    glow_draw.rounded_rectangle(
        [(70, 70), (1130, 1730)],
        radius=60,
        outline=(0, 255, 255, 180),
        width=12
    )

    glow = glow.filter(
        ImageFilter.GaussianBlur(30)
    )

    card.paste(
        glow,
        (0, 0),
        glow
    )

    draw = ImageDraw.Draw(card)

    # ================= MAIN CARD =================

    draw.rounded_rectangle(
        [(70, 70), (1130, 1730)],
        radius=60,
        fill=(17, 24, 39),
        outline=(124, 58, 237),
        width=5
    )

    # ================= FONTS =================

    try:

        title_font = ImageFont.truetype("arial.ttf", 54)

        subtitle_font = ImageFont.truetype("arial.ttf", 44)

        amount_label_font = ImageFont.truetype("arial.ttf", 40)

        amount_font = ImageFont.truetype("arial.ttf", 90)

        body_font = ImageFont.truetype("arial.ttf", 34)

        footer_font = ImageFont.truetype("arial.ttf", 34)

    except:

        title_font = ImageFont.load_default()

        subtitle_font = ImageFont.load_default()

        amount_label_font = ImageFont.load_default()

        amount_font = ImageFont.load_default()

        body_font = ImageFont.load_default()

        footer_font = ImageFont.load_default()

    # ================= HEADER =================

    draw.text(
        (250, 120),
        "SCAN FOR PAYMENT",
        fill=(255, 255, 255),
        font=title_font
    )

    draw.text(
        (360, 195),
        "ANY UPI APP",
        fill=(0, 255, 255),
        font=subtitle_font
    )

    # ================= QR BOX =================

    draw.rounded_rectangle(
        [(220, 320), (980, 1080)],
        radius=50,
        fill=(255, 255, 255)
    )

    qr_resized = img.resize((620, 620))

    card.paste(
        qr_resized,
        (290, 390)
    )

    # ================= AMOUNT LABEL =================

    draw.text(
        (410, 1155),
        "Amount To Pay",
        fill=(180, 180, 180),
        font=amount_label_font
    )

    # ================= AMOUNT =================

    draw.text(
        (430, 1240),
        f"₹{amount}",
        fill=(170, 85, 255),
        font=amount_font
    )

    # ================= UPI BOX =================

    draw.rounded_rectangle(
        [(150, 1390), (1050, 1495)],
        radius=30,
        fill=(30, 41, 59)
    )

    draw.text(
        (210, 1425),
        final_upi,
        fill=(255, 255, 255),
        font=body_font
    )

    # ================= REMARK BOX =================

    draw.rounded_rectangle(
        [(150, 1530), (1050, 1635)],
        radius=30,
        fill=(30, 41, 59)
    )

    remark_text = (
        remark
        if remark
        else "Secure UPI Payment"
    )

    draw.text(
        (210, 1565),
        remark_text,
        fill=(220, 220, 220),
        font=body_font
    )

    # ================= FOOTER =================

    draw.text(
        (360, 1685),
        "SECURE UPI GATEWAY",
        fill=(0, 255, 200),
        font=footer_font
    )

    # ================= SAVE CARD =================

    card_buffer = BytesIO()

    card.save(
        card_buffer,
        format="PNG"
    )

    card_buffer.seek(0)

    # ================= DOWNLOAD BUTTON =================

    st.download_button(
        label="⬇ Download Premium UPI Card",
        data=card_buffer,
        file_name="premium_upi_card.png",
        mime="image/png"
    )
