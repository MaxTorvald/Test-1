# Real-Time chat application
import os
import sys
import streamlit as st
import json
from PIL import Image
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="Real-Time chat application", page_icon=":speech_balloon:", layout="wide")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/7401522f-2d8b-4049-ad18-eb0edb6af224/CE9lFrNlEH.json")
# header section
st.subheader("Hi, I'm Max :wave:")
st.title("A Modern and Quantum physics specialist from the US")
st.write("I'm passionate about learning more about coding and modeling robots")
st.write("Here you can see my first actual website!")
st.write("Welcome to my real time chat application V. 0.0.1")
st.write("[Learn More >](https://www.upwork.com/freelancers/~01cf15b6fe4ac674c8)")

#What I do
with st.container():
    st.write("-----")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Tell me more about this channel")
        st.write("##")
        st.write(
            """
            On my website you can talk to people around the world, create your emotes, get banners, profile accessories andmuch more
            be sure to:
            -Write your email address
            -Write down your password, must be at least 8 characters, with upper and lower letters, as well as numbers and symbols
            -Enter your verification number which consists of 6 numbers generated via your gmail, can only be used once.
            -Select your country, your nation's code and if possible, your ID.
            -If you'd love for a much better experience, plus AI features and more, be sure to subscribe to my premium version (5.99$/month).
            -You can donate for more support for my new real time chat.
            -Your infos are always in a safe hand, but for insurement, don't give your infos to strangers nor to anyone at that matter.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300,key="coding")

        # Projects
        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with text_column:
                st.subheader("Integrate Lottie Animations inside your streamlit app")
                st.write(
                    """
                    Learn how to use Lottie files in Streamlit!
                    Animations make our web app more engaging and fun, and lottie files are the easiest way to do it
                    In this tutorial, I'll show you exactly how to do it
                    """
                       )
                st.markdown("[Check this video from...](https://www.youtube.com/watch?v=5XyzyMqY7Cw&t=57s)")
# footer section
st.write("---")
st.write("Made with ❤️ by [Max]")
with st.container():
    st.write("-----")
    st.write("##")
    st.write("Connect with me on:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.write("##")
        st.write("_")