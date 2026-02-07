import streamlit as st
import time


from tools.laptop_tools import (
    search_by_budget,
    filter_by_ram,
    best_value_laptops,
    gaming_laptops   # ⭐ ADDED
)


# st.sidebar.markdown(
#     "<div style='text-align: center;'>"
#     "<img src='image.png' width='140'>"
#     "</div>",
#     unsafe_allow_html=True
# )
st.sidebar.markdown("## Laptop Recommender")

# ---------------------------------
# Page Config
# ---------------------------------

st.set_page_config(
    page_title="AI Laptop Recommender",
    page_icon="logo.png",
    layout="wide"
)

st.title("💻 AI Laptop Recommendation System")
st.write("Find the best laptop based on your needs instantly.")

st.divider()


# ---------------------------------
# Sidebar Controls
# ---------------------------------

st.sidebar.header("🔎 Filters")

option = st.sidebar.selectbox(
    "Choose Recommendation Type",
    [
        "Search by Budget",
        "Filter by RAM",
        "Best Value Laptops",
        "Gaming Laptops 🎮"   # ⭐ ADDED
    ]
)


# ---------------------------------
# MAIN UI
# ---------------------------------

if option == "Search by Budget":

    max_price = st.sidebar.slider(
        "Maximum Budget (₹)",
        20000,
        200000,
        70000,
        step=5000
    )

    if st.sidebar.button("Recommend 💻"):

        with st.spinner("🧠 AI analyzing 5000+ laptops..."):
            time.sleep(1.5)
            result = search_by_budget(max_price)

        st.success("Here are the best options:")
        st.text(result)




elif option == "Filter by RAM":

    min_ram = st.sidebar.selectbox(
        "Minimum RAM",
        [8, 16, 32]
    )

    if st.sidebar.button("Recommend 💻"):

        with st.spinner("⚡ Scanning high-performance machines..."):
            time.sleep(1.5)
            result = filter_by_ram(min_ram)

        st.success("Top performance machines:")
        st.text(result)




elif option == "Best Value Laptops":

    max_price = st.sidebar.slider(
        "Budget",
        30000,
        200000,
        80000,
        step=5000
    )

    if st.sidebar.button("Recommend 💻"):

        with st.spinner("📊 Calculating performance-per-rupee..."):
            time.sleep(1.5)
            result = best_value_laptops(max_price)

        st.success("Maximum performance per rupee:")
        st.text(result)




# ---------------------------------
# ⭐ GAMING FEATURE (NEW)
# ---------------------------------

elif option == "Gaming Laptops 🎮":

    max_price = st.sidebar.slider(
        "Gaming Budget",
        40000,
        300000,
        100000,
        step=5000
    )

    if st.sidebar.button("Recommend 💻"):

        with st.spinner("🎮 Finding RTX-powered beasts..."):
            time.sleep(1.5)
            result = gaming_laptops(max_price)

        st.success("Top Gaming Machines:")
        st.text(result)



# st.sidebar.divider()


st.sidebar.markdown(
"""
---
<small>
© 2025 Harsha Project <br>
All rights reserved.
</small>
""",
unsafe_allow_html=True
)
