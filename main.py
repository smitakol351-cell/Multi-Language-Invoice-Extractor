import streamlit as st
from PIL import Image
import google.generativeai as genai


GOOGLE_API_KEY = "AIza"
#Set API Key for Gemini model
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini Model
model = genai.GenerativeModel('gemini-2.5-flash')

def get_gemini_response(input,image,prompt):
    response = model.generate_content([input,image[0],prompt])
    return  response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        #Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type, #Give the mime type of the uploaded file
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded')

# initialize our streamlit application

st.set_page_config(page_title="Multi-Language Invoice Extractor")

st.header('Multi-Language Invoice Extractor')



# File uploader
uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"])
image=""
# Check if the user has uploaded a file
if uploaded_file is not None:
    # Open the uploaded image file as a PIL image
    image = Image.open(uploaded_file)

    #resized_image = image.resize((200, 250))  # (width, height)

# Display the resized image
    #st.image(resized_image, caption="Uploaded Image", use_container_width=False)
    # Display the image with a smaller width (e.g., 300px)
    st.image(image, caption="Uploaded Image", use_container_width=False, width=300 )

    # Optional: Process or save the image here
    st.write("Image uploaded successfully!")
else:
    st.write("Please upload an image file.")

#Submit Button


input = st.text_input('Input Prompt: ' , key="input")

submit = st.button('Tell me about the invoice')

input_prompt="""
You are an expert in understanding invoices. We will upload an image as
invoice, and you will have to answer any questions based on the uploaded
invoice image.
"""

#If Submit Button is clicked
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)