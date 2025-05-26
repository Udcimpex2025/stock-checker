import streamlit as st
import pandas as pd

# Load CSV from same folder
data = pd.read_csv("stock.csv")

# App title
st.title("📦 UDC STOCK CHECK APP")

# Input from user
item_code = st.text_input("Enter Item Details")

if item_code:
    result = data[data['Item Details'].astype(str).str.contains(item_code, case=False, na=False)]

    if not result.empty:
        qty = result.iloc[0]['Qty.']
        unit = result.iloc[0]['Unit']
        st.success(f"Stock: {qty} {unit}")

        # Check for low stock
        try:
            if float(qty) <= 15:
                st.warning("🔔 Please check in WhatsApp group. Stock is low!")
        except:
            st.warning("⚠️ Unable to evaluate stock quantity.")
    else:
        st.error("Item not found")
