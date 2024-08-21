import streamlit as st
import pickle
import string

# Ensure correct file paths
vectorizer_path = r"A:\datascience\withMLmodel\Emailproj\vectorizerV5.pkl"
model_path = r"A:\datascience\withMLmodel\Emailproj\modelV5.pkl"
background_image_path = "A:/datascience/withMLmodel/Emailproj/Hacker-Wallpaper-03-4000x2158-1-scaled.jpg"

# Set background image using HTML and CSS
background_image_code = f"""
<style>
    body {{
        background-image: url('{background_image_path}');
        background-size: cover;
    }}
</style>
"""

st.markdown(background_image_code, unsafe_allow_html=True)

# Define the text transformation function
def transform_text(text):
    text = text.lower()
    text = text.split()
    
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in string.punctuation:
            y.append(i)

    return " ".join(y)

# Load the vectorizer and model
with open(vectorizer_path, 'rb') as f:
    c_vic = pickle.load(f)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.title("Email Spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('Classify'):
    transformed_sms = transform_text(input_sms)
    vec = c_vic.transform([transformed_sms])
    result = model.predict(vec)[0]
    
    if result == 1:
        st.header("Spam")
    else:
        st.header("Ham")
