import streamlit as st
import pandas as pd
from PIL import Image

# Show logo at the top
logo = Image.open("udc-homes-logo.PNG")
st.image(logo, width=120)

# App title
st.title("📦 UDC STOCK APP")

# Load CSV from same folder
data = pd.read_csv("stock.csv")

# Input from user
item_code = st.text_input("Enter Item Details").strip()

if item_code:
    # Case-insensitive partial match
    result = data[data['Item Details'].astype(str).str.contains(item_code, case=False, na=False)]

    if not result.empty:
        item_name = result.iloc[0]['Item Details']
        qty = float(result.iloc[0]['Qty.'])  # Convert to float to allow decimals
        unit = result.iloc[0]['Unit']

        # Show full item and stock
        st.success(f"{item_name}\n\nStock: {qty} {unit}")

        # Warning if stock is low
        if qty <= 15:
            st.warning("🔔 Please check in WhatsApp group. Stock is low!")
    else:
        st.error("❌ Item not found.")
