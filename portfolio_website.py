import streamlit as st
import google.generativeai as genai
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


# Change background color in the website by CSS
# page_bg_color = """
# <style>
# [data-test_id="stAppViewContainer"] {
#     background-color: #ADD8E6;  /* Replace this with your desired background color */
# }
# </style>
# """
#
# # Inject the CSS style into the Streamlit app
# st.markdown(page_bg_color, unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Phuong Thu")
with col2:
    st.image("images/me.jpg")

st.title(" ")
persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """

st.title("Phuong Thu's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user ask:" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title("")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
with col2:
    st.video("https://www.youtube.com/watch?v=_2UqdX8dcsU&t=4608s")

st.title(" ")
st.title("My Setup")
st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)    # 0 is min value, 100 is max value, 70 is the value u have
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

# st.file_uploader("Upload a file")
# to upload file from computer

st.write(" ")
st.title("Gallery")
images = [
    "images/g1.jpg", "images/g2.jpg", "images/g3.jpg",
    "images/g4.jpg", "images/g5.jpg", "images/g6.jpg",
    "images/g7.jpg", "images/g8.jpg", "images/g9.jpg"
]
col1, col2, col3 = st.columns(3)

for x, image in enumerate(images):
    if x < 3:
        with col1:
            st.image(image)
    elif 3 <= x < 6:
        with col2:
            st.image(image)
    else:
        with col3:
            st.image(image)

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("contact@murtazahassan.com")
