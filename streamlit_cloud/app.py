"""Streamlit Community Cloud portfolio adapter for oop-ecommerce-cart.

This does not replace the original implementation.
"""
from pathlib import Path

import streamlit as st

TITLE = "E-Commerce Cart"
ICON = "🛒"
DESC = "A shopping-cart implementation using object composition and discount strategies."
CATEGORY = "Python OOP exercise"
NOTICE = "Browser shopping cart is a learning demo with no real checkout or payment."
GITHUB = "https://github.com/mohsinattasial/oop-ecommerce-cart"
VERCEL = "https://mohsin-ecommerce-cart.vercel.app"
LOCAL_COMMAND = "cd oop-ecommerce-cart && python cli.py"
FEATURES = ["Cart items and quantities","Strategy pattern discounts","Python unittest checks"]

st.set_page_config(page_title=TITLE + " | Mohsin Atta", page_icon=ICON, layout="wide")
st.caption("Mohsin Atta · GitHub Portfolio · Streamlit Cloud edition")
st.title(ICON + " " + TITLE)
st.write(DESC)
st.caption(CATEGORY)

left, right = st.columns(2)
with left:
    st.link_button("GitHub source code", GITHUB, use_container_width=True)
with right:
    st.link_button("Existing browser version", VERCEL, use_container_width=True)

st.info(NOTICE)
with st.expander("Original project and features", expanded=False):
    for feature in FEATURES:
        st.write("• " + feature)
    st.code(LOCAL_COMMAND, language="bash")

st.subheader("Interactive browser edition")
st.caption("The following interactive view is embedded from the separate Vercel deployment.")
import streamlit.components.v1 as components
components.iframe(VERCEL, height=760, scrolling=True)

st.divider()
st.caption("© 2026 Mohsin Atta · Educational portfolio · MIT-licensed original code where applicable")
