import streamlit as st
import pandas as pd
from PIL import Image

# Show logo at the top
logo = Image.open("udc-homes-logo.PNG")
st.image(logo, width=120)

# App title
st.title("📦 UDC STOCK APP")

# Stock update note
st.caption("🕒 *Note: The stock shown here is updated every morning at 11:00 AM*")

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

        # Use columns for clean layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Item")
            st.info(item_name)

        with col2:
            st.subheader("Stock")
            st.metric(label="Quantity", value=f"{qty} {unit}")

        # Warning if stock is low
        if qty <= 15:
            st.warning("🔔 Please check in WhatsApp group. Stock is low!")
    else:
        st.error("❌ Item not found.")
