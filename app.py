    # ---------- PREMIUM DOWNLOADABLE CARD ----------

    card_width = 900
    card_height = 1400

    # Base background
    card = Image.new("RGB", (card_width, card_height), "#050816")

    draw = ImageDraw.Draw(card)

    # Premium gradient layers
    for i in range(800):
        color = (
            int(20 + i * 0.08),
            int(10 + i * 0.03),
            int(40 + i * 0.09)
        )

        draw.rectangle(
            [(0, i), (card_width, i + 2)],
            fill=color
        )

    # Main Glass Card
    draw.rounded_rectangle(
        [(40, 40), (860, 1360)],
        radius=45,
        fill=(17, 24, 39),
        outline=(120, 80, 255),
        width=4
    )

    # Glow effect
    glow = Image.new("RGBA", (card_width, card_height), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow)

    glow_draw.rounded_rectangle(
        [(40, 40), (860, 1360)],
        radius=45,
        outline=(0, 255, 255, 180),
        width=8
    )

    glow = glow.filter(ImageFilter.GaussianBlur(18))

    card.paste(glow, (0, 0), glow)

    draw = ImageDraw.Draw(card)

    # Fonts
    title_font = ImageFont.load_default()
    normal_font = ImageFont.load_default()
    amount_font = ImageFont.load_default()

    # Header
    draw.text(
        (250, 90),
        "SCAN FOR PAYMENT",
        fill=(255, 255, 255),
        font=title_font
    )

    draw.text(
        (300, 130),
        "ANY UPI APP",
        fill=(0, 255, 255),
        font=title_font
    )

    # QR Background Box
    draw.rounded_rectangle(
        [(170, 250), (730, 810)],
        radius=40,
        fill=(255, 255, 255)
    )

    # QR resize
    qr_resized = img.resize((470, 470))

    card.paste(qr_resized, (215, 295))

    # Amount Label
    draw.text(
        (330, 860),
        "Amount To Pay",
        fill=(180, 180, 180),
        font=normal_font
    )

    # Amount
    draw.text(
        (360, 920),
        f"₹{amount}",
        fill=(170, 85, 255),
        font=amount_font
    )

    # UPI Box
    draw.rounded_rectangle(
        [(120, 1030), (780, 1110)],
        radius=25,
        fill=(25, 35, 55)
    )

    draw.text(
        (170, 1060),
        final_upi,
        fill=(255, 255, 255),
        font=normal_font
    )

    # Remark Box
    draw.rounded_rectangle(
        [(120, 1150), (780, 1230)],
        radius=25,
        fill=(25, 35, 55)
    )

    remark_text = remark if remark else "Secure UPI Payment"

    draw.text(
        (170, 1180),
        remark_text,
        fill=(210, 210, 210),
        font=normal_font
    )

    # Footer
    draw.text(
        (320, 1290),
        "SECURE UPI GATEWAY",
        fill=(0, 255, 200),
        font=normal_font
    )

    # Save card
    card_buffer = BytesIO()

    card.save(card_buffer, format="PNG")

    card_buffer.seek(0)
