import streamlit as st
import requests

# Streamlit UI
st.title("Text Extraction App")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Send the image to the backend API
    files = {"files": uploaded_file.getvalue()}
    response = requests.post("http://<backend_url>/extract", files={"files": uploaded_file})
    
    if response.status_code == 200:
        extracted_text = response.json().get('texts', [])
        st.write("Extracted Text:")
        for text in extracted_text:
            st.write(text)
    else:
        st.write("Error in extraction")
