import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(
    page_title="Premium UPI QR Generator",
    page_icon="💎",
    layout="centered"
)

# ---------- PREMIUM CSS ----------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg,#050816,#0f172a,#111827);
    color: white;
}

.main-title {
    text-align:center;
    font-size:42px;
    font-weight:800;
    background: linear-gradient(to right,#a855f7,#06b6d4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    margin-bottom:10px;
}

.subtitle {
    text-align:center;
    color:#94a3b8;
    margin-bottom:40px;
}

.glass-card {
    background: rgba(255,255,255,0.06);
    padding:30px;
    border-radius:30px;
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(20px);
    box-shadow:0 0 40px rgba(168,85,247,0.2);
}

.payment-card {
    background: rgba(255,255,255,0.08);
    padding:35px;
    border-radius:35px;
    border:1px solid rgba(255,255,255,0.12);
    backdrop-filter: blur(25px);
    box-shadow:0 0 60px rgba(6,182,212,0.2);
    text-align:center;
    margin-top:30px;
}

.amount-text {
    font-size:18px;
    color:#cbd5e1;
    margin-top:20px;
}

.price {
    font-size:54px;
    font-weight:800;
    background: linear-gradient(to right,#a855f7,#06b6d4);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.footer-text {
    margin-top:25px;
    color:#94a3b8;
    font-size:14px;
}

.qr-box {
    background:white;
    padding:20px;
    border-radius:30px;
    display:inline-block;
    margin-top:20px;
}

.stButton>button {
    width:100%;
    border:none;
    border-radius:18px;
    background: linear-gradient(to right,#9333ea,#06b6d4);
    color:white;
    font-size:18px;
    font-weight:700;
    padding:14px;
    transition:0.3s;
}

.stButton>button:hover {
    transform:scale(1.02);
    box-shadow:0 0 25px rgba(168,85,247,0.5);
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.markdown("<div class='main-title'>Premium UPI QR Generator</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>Luxury Secure Payment Gateway</div>", unsafe_allow_html=True)

# ---------- FORM ----------

upi_options = [
    "9696159863-2@ibl",
    "9696159863-3@ybl",
    "9696159863@phonepe"
]

st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

selected_upi = st.selectbox("Select UPI ID", upi_options)

custom_upi = st.text_input("Custom UPI ID")

amount = st.text_input("Amount")

remark = st.text_input("Note / Remark")

generate = st.button("Generate Premium QR")

st.markdown("</div>", unsafe_allow_html=True)

# ---------- QR GENERATION ----------

if generate:

    final_upi = custom_upi if custom_upi else selected_upi

    upi_link = f"upi://pay?pa={final_upi}&pn=Vinay&am={amount}&tn={remark}&cu=INR"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=2
    )

    qr.add_data(upi_link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffered = BytesIO()
    img.save(buffered, format="PNG")

    st.markdown("<div class='payment-card'>", unsafe_allow_html=True)

    st.markdown("### ✨ Scan For Payment Any UPI App")

    st.markdown("<div class='qr-box'>", unsafe_allow_html=True)

    st.image(img, width=280)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='amount-text'>Amount To Pay</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='price'>₹{amount}</div>", unsafe_allow_html=True)

    st.markdown(f"#### {final_upi}")

    if remark:
        st.markdown(f"📝 {remark}")

    st.markdown("<div class='footer-text'>🔒 Secure UPI Gateway</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.download_button(
        label="⬇ Download QR Code",
        data=buffered.getvalue(),
        file_name="premium_upi_qr.png",
        mime="image/png"
    )
