import streamlit as st
import io
import time
from pikepdf import Pdf, PasswordError

# Page Configuration - Premium Look ke liye
st.set_page_config(
    page_title="Vikas Mishra | Pro PDF Tools",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Professional Design & Visibility
st.markdown("""
    <style>
    /* Main Background and Text Visibility */
    .stApp {
        background-color: #0e1117;
        color: #e0e0e0;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    
    /* Headers Styling */
    h1, h2, h3 {
        color: #58a6ff !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Footer/Credit Styling */
    .footer-text {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 14px;
        color: #8b949e;
    }
    
    .credit-link {
        color: #58a6ff !important;
        text-decoration: underline !important;
        font-weight: bold;
        font-size: 16px;
    }

    /* Professional Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #238636;
        color: white;
        border: none;
        padding: 10px;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #2ea043;
        border: none;
        color: white;
    }

    /* Input Box Visibility */
    .stTextInput>div>div>input {
        background-color: #0d1117;
        color: white;
        border: 1px solid #30363d;
    }
    
    /* Status Box */
    .success-box {
        padding: 20px;
        background-color: rgba(35, 134, 54, 0.15);
        border: 1px solid #238636;
        border-radius: 10px;
        color: #3fb950;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR DESIGN ---
with st.sidebar:
    st.markdown("## 🛠️ Dashboard Settings")
    st.divider()
    
    st.info("Yeh tool protected PDF files se password hatane ke liye banaya gaya hai.")
    
    # Custom Sidebar Credit (As per request)
    st.markdown("<br><br>" * 5, unsafe_allow_html=True)
    st.markdown("""
        <div style='text-align: center;'>
            <p style='margin-bottom: 0; color: #8b949e;'>Designed & Crafted by</p>
            <p class='credit-link'><u>Vikas Mishra</u></p>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.title("🔐 Premium PDF Pass-Crack Dashboard")
st.write("Ab aap apni password-protected PDF files ko bina kisi rukawat ke unlock kar sakte hain.")

# Layout Columns
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📤 Upload Protected PDF")
    uploaded_file = st.file_uploader("Apni file yahan drag karein ya browse karein", type=["pdf"])
    
    password = st.text_input("File ka Password darj karein:", type="password", help="Agar aapko password pata hai to yahan likhein.")

with col2:
    st.markdown("### 📝 Instruction Box")
    st.info("""
    1. Protected PDF file upload karein.
    2. Sahi password enter karein.
    3. 'Remove Security' button par click karein.
    4. Unlocked file turant download karein.
    """)

st.divider()

if uploaded_file is not None:
    if st.button("🚀 Process & Remove Security"):
        if not password:
            st.error("Kripya password enter karein!")
        else:
            with st.spinner("Processing... Security layers hataai ja rahi hain..."):
                try:
                    # Reading the PDF
                    file_bytes = uploaded_file.read()
                    
                    # Unlocking logic using pikepdf
                    with Pdf.open(io.BytesIO(file_bytes), password=password) as pdf:
                        # Save the decrypted PDF
                        output = io.BytesIO()
                        pdf.save(output)
                        output.seek(0)
                        
                        time.sleep(1.5) # For professional feel/loading
                        
                        st.markdown("""
                            <div class='success-box'>
                                ✅ <b>Success!</b> Aapki PDF file unlock ho gayi hai. Neeche diye gaye button se download karein.
                            </div>
                        """, unsafe_allow_html=True)
                        
                        st.download_button(
                            label="📥 Download Unlocked PDF",
                            data=output,
                            file_name=f"Unlocked_{uploaded_file.name}",
                            mime="application/pdf"
                        )
                
                except PasswordError:
                    st.error("❌ Galat Password! Kripya sahi password try karein.")
                except Exception as e:
                    st.error(f"❌ Kuch gadbad hui: {str(e)}")

# Fallback UI for Visibility check
if not uploaded_file:
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.image("https://www.freeiconspng.com/uploads/pdf-icon-png-pdf-extension-file-format-icon-24.png", width=100)
    st.caption("Waiting for file upload...")

# Professional Footer Line
st.markdown("---")
st.markdown("<p style='text-align: center; color: #484f58;'>© 2024 Vikas Mishra Pro Dashboard | Secure & Private</p>", unsafe_allow_html=True)
