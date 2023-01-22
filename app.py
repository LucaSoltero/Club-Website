import streamlit as st
from streamlit_lottie import st_lottie
import json
from PIL import Image
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from ex_link import st_button, check_creds
from dotenv import load_dotenv
import os

load_dotenv()
not_path = os.getenv("NOT_KEY")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


# -- Google Sheets Setup --

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(not_path, scope)
client = gspread.authorize(creds)
student_sheet = client.open("Student Data").sheet1

# -- Input Data, Page Title, and Images to be displayed --

input_data = ["STUDENT"]
page_title = "FinTech@USC"
logo_img = Image.open("logo.png")

# CONFIGS
st.set_page_config(page_title=page_title, layout="centered")

# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

# --WELCOME--
st.image(logo_img, width=150)
st.markdown("<h1 style='text-align: center; color: white;'>FinTech at USC</h1>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;">Students interested in and excited about the future of Financial Technology '
    '&#x1F64C;'
    '</div>', unsafe_allow_html=True)
st.markdown("#")
anime = load_lottiefile("Animations/fintech.json")
st_lottie(anime, height=250, loop=True)

# --ABOUT--

# -- WHY FinTech
st.markdown("<h1 style='text-align: center; color: white;'>Why FinTech?</h1>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;">Technology has revolutionized the finance industry and has made it more efficient and accessible to a wider'
    " range of people. The use of technology in finance has allowed for faster and more accurate financial transactions, "
    " as well as the ability to analyze and make informed decisions based on data. The rise of the FinTech industry, "
    "which combines finance and technology, has also made financial services more accessible to underserved populations "
    "and has disrupted traditional financial institutions. In the coming decades, it is expected that the FinTech "
    "industry will continue to grow and evolve as more and more people turn to technology for their financial needs."
    " As a result, it is important for financial institutions and individuals to stay up-to-date on the latest "
    "technological advancements in order to remain competitive in the market."
    '</div>', unsafe_allow_html=True)
st.markdown("#")
# -- animation --


# -- Ideals --
st.markdown("<h1 style='text-align: center; color: white;'>Our Ideals</h1>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;">FinTechSC values the exchange of ideas and knowledge between students and '
    'industry professionals. The club offers opportunities for students to connect with founders and experts in the '
    'FinTech industry and learn from their experiences and insights. FinTechSC also strives to stay informed about '
    'the latest trends and developments in the industry and the ways in which it is growing and evolving.'

    '</div>', unsafe_allow_html=True)

st.markdown("#")
# -- animation --
anime = load_lottiefile("Animations/guru copy.json")
st_lottie(anime, height=250, loop=False)


# STUDENT INPUT

st.markdown("<h1 style='text-align: center; color: white;'>Join Us &#10071;</h1>", unsafe_allow_html=True)
st.markdown(
    '<div style="text-align: center;">Interested in Joining &#10067; Fill out the form below &#128518;'
    '</div>', unsafe_allow_html=True)
st.markdown("#")
with st.form(input_data[0], clear_on_submit=True):
    st.text_input("Name :zap:", "", key="STUDENT_NAME")
    st.text_input("USC Email :sunglasses:", "", key="USC_EMAIL")
    st.text_input("Major" + " :crystal_ball:", "", key="MAJOR")
    submitted_student = st.form_submit_button("Submit")
    if submitted_student:
        student_name = str(st.session_state["STUDENT_NAME"]).strip()
        student_email = str(st.session_state["USC_EMAIL"]).strip()
        student_major = str(st.session_state["MAJOR"]).strip()
        if check_creds(student_name, student_email, student_major):
            insert_row = [student_name, student_email, student_major]
            student_sheet.append_row(insert_row)
            st.write("Your info was successfully submitted! Have a great day :smile:")
        else:
            pass

# -- animation --
st.markdown("#")
anime = load_lottiefile("Animations/tech.json")
st_lottie(anime, loop=True, height=200)

st.subheader("Relevant Links")
st.write("Checkout our Team")
st_button('https://fintechuscteam.onrender.com', "team.fintechusc.com", 20)
st.write("Contact Us")
st_button("https://forms.gle/DHeQgXv4qut7Gtpq9", "https://forms.gle/DHeQgXv4qut7Gtpq9", 20)
st.write("About this Website")
st_button('https://github.com/LucaSoltero/Club-Website', "github.com/LucaSoltero/Club-Website", 20)
st.markdown("#")
st.image(logo_img, width=150)
