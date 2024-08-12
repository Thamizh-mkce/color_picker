import streamlit as st

# Streamlit app layout
st.title("Color Picker")

# Color picker widget
selected_color = st.color_picker("Pick a color", "#ff0000")

# Display the selected color
st.write(f"Selected color: {selected_color}")

# Display a box with the selected color
st.markdown(
    f"""
    <div style="width:100px; height:100px; background-color:{selected_color};">
    </div>
    """,
    unsafe_allow_html=True,
)
