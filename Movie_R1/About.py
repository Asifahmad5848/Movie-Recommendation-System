import streamlit as st
from PIL import Image
st.set_page_config(page_title="About", page_icon="ℹ️",layout="wide",)

#st.header('About Movie Recommendation System')
st.markdown(f'<h1 style="color:#ffffff;font-size:39px;">{"About Movie Recommendation System"}</h1>', unsafe_allow_html=True)
#st.markdown(about,unsafe_allow_html=True)
st.markdown(f'<h3 style="color:#ffffff;font-size:24px;">{"A movie recommendation system, or a movie recommender system, is an ML-based approach to filtering or predicting the users’ film preferences based on their past choices and behavior. It’s an advanced filtration mechanism that predicts the possible movie choices of the concerned user and their preferences towards a domain-specific item, aka movie."}</h3>', unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/movie-film-strip-blue-background_1017-33458.jpg");
             background-attachment: fixed;
             background-position: center;
             background-repeat:no-repeat;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

from streamlit_extras.app_logo import add_logo

#add_logo("C:\\Users\\komal\\Downloads\\MRS1\\logo3.png",height=50)
def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://img.uxwing.com/wp-content/themes/uxwing/download/video-photography-multimedia/movie-theater-icon.svg);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
                background-size: 200px 200px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Recommenders";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

#my_logo = add_logo(logo_path="C:\\Users\\komal\\Downloads\\MRS1\\logo3.png", width=50, height=60)
#st.sidebar.image(my_logo)
add_logo()
#st.write(":milk[👈 Check out the movie icon in the nav-bar!]")
#st.header(':white[Developers:]')
st.write(f'<h1 style="color:#ffffff;font-size:24px;">{"👈 Check out the movie icon in the nav-bar!"}</h1>', unsafe_allow_html=True)
st.write(f'<h1 style="color:#ffffff;font-size:35px;">{"Team: Perfect Drive"}</h1>', unsafe_allow_html=True)

#st.markdown(d,unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Koukuntla Komal Reddy        @Project Manager "}</h2>', unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Chalumuri Harshitha          @Software Engineer"}</h2>', unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Chintada Jagan Mohan Rao     @Quality Assurance Engineer "}</h1>', unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Koppaka Yeswanth             @Data Scientist"}</h2>', unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{" Kalapala Venkata Surya Teja @User Experience Designer"}</h2>', unsafe_allow_html=True)
st.write(f'<h2 style="color:#ffffff;font-size:24px;">{"Asif Ahmad Najar             @Documentation Writer"}</h2>', unsafe_allow_html=True)