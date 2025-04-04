import streamlit as st
import streamlit_option_menu as option_menu
import streamlit_lottie as st_lottie
import requests


#page 1
st.set_page_config(layout="wide")
st.subheader("Hey there 👾")
st.title("My Portfolio Website")
st.write("""
Hey there! I'm a CS major student with a passion for using data to solve real-world problems, and I'm excited to share my work with you.
I love to learn new things and I'm always looking for ways to improve my skills. 
I hope you enjoy exploring my projects as much as I enjoyed creating them.
""")

st.write("[More >>](https://www.linkedin.com/in/amir-esam-elsamahy-85b82b347/)")
st.write("---")

#### animations ####

def get_url(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

x=get_url("https://lottie.host/45f6e56b-9bf1-44c3-95d2-315b7d9401f7/BQpz7p1SgQ.json")
y=get_url("https://lottie.host/aafeb0ed-0c21-43d1-8ab9-5cb9f9b04357/NZlYbZ69vU.json")
z=get_url("https://lottie.host/74be738a-c765-473c-9c8e-d3a5222e4783/mD0oKcKcqF.json")
w=get_url("https://lottie.host/b98a7c21-391b-45d2-8fa0-ff7db2cf9a42/ORmF4qWE7Z.json")








### bar###
selected =option_menu.option_menu(
    menu_title=None,
    options=["About", "Projects", "Contact"],
    icons=["person", "code-slash", "envelope"],
    # menu_icon="cast",
    orientation="horizontal",
)

# in about 
if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("Hey there I'm Amir")
            st.title("Undergraduate at ZC")
            st.write("""
            Hey there i'm Amir, a computer science major with a passion for data science and machine learning.
                     hope u enjoy exploring my projects as much as I enjoyed creating them.
                     dont hasitate to reach out if you have any questions or just want to chat about tech!
                     I'm always looking to learn and grow, so feel free to connect with me on LinkedIn or GitHub.
            
                     
                     """)
            st.write("##")
            st.write("Contact me :")
            st.markdown("[visit Github](https://github.com/amir-elsamahy)")
            st.markdown("[visit LinkedIn](https://www.linkedin.com/in/amir-esam-elsamahy-85b82b347/)")
            st.markdown("[About ZC University ](https://www.zewailcity.edu.eg/academics/undergraduate-studies/schools/program/40)")

        with col2:
            st_lottie.st_lottie(x, height=400, width=400, key="coding")

    st.write("---")

    with st.container():
        col3, col4 =st.columns(2)
        with col3:
            st.write("##")
            st.subheader("""
            Education
            - ZC University
                 - Bachelor of Engineering- Computer Science
                 - school of computer science and engineering
                 - Data Science Major
                    - 2025-2028               
                         
      """)
            
        with col4:
            st.write("##")
            st.subheader("""
            Skills
            - Python
            - SQL
            - C++             
            - computer vision
            - web scraping                             
            
      """)
       
# page 2
# in projects
if selected == "Projects":
    with st.container():
        st.write("##")
        st.subheader("My Projects")


        col5,col6=st.columns(2)
        with col5:
            st_lottie.st_lottie(z, height=400, width=400, key="analyzing")

        with col6:
            st.badge("new")
            st.subheader("Data Science Projects")
            st.write("""
            
            - web scraping and analysis of data from e-commerce website
                 - scraping data from e-commerce website
                 - data cleaning and analysis
                 - data visualization
                    -Spring 2025
                     """)  
            st.markdown("[visit Github Repo](https://github.com/amir-elsamahy?tab=projects)")



    st.write("---") 


    with st.container():
  
        col7,col8=st.columns(2)

        with col7:
            st_lottie.st_lottie(y, height=300, width=300, key="cv")
        with col8:
            st.subheader("Computer Vision Projects")
            st.write("""
         
            - simple face recognition system.
                - using opencv and deep learning 
                -Spring 2025
                """)
            st.markdown("[visit Github Repo](https://github.com/amir-elsamahy?tab=projects)")


    st.write("---")


    with st.container():
        col9,col10=st.columns(2)

        with col9:
            st.subheader("Networking Projects")
            st.write("""
  
        
                    - using cisco packet tracer
                    - network design and configuration
                    - network security and monitoring
                    -Fall 2024
                """)
            st.markdown("[visit Github Repo](https://github.com/amir-elsamahy?tab=projects)")

        with col10:

            st.subheader("c++ Projects")
            st.write("""

            - simple c++ project.
                     -simple OOP project.
                     -SQL database management system
                     -management system for company staff.
                    -spring 2025
                """)
            st.markdown("[visit Github Repo](https://github.com/amir-elsamahy?tab=projects)")
#page 3
# in contact          
if selected == "Contact":
    with st.container():
        st.header("Get in toch 📬")
        st.write("##")
        st.write("my mail :\"amiresamelsamahy@gmail.com\"")
        col11,col12=st.columns(2)
        with col12:
            st_lottie.st_lottie(w, height=400, width=400, key="contact")
        with col11:
            st.write("##")
            st.subheader("Contact me")
############### the form ###############
            contact_form = """
<form action="https://formsubmit.co/amiresamelsamahy@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="your message"></textarea>
     <button type="submit">Send</button>
</form>
            """

            # Render the css file 
            st.markdown(contact_form,unsafe_allow_html=True)
            def local_css(file_name):
                with open(file_name) as f:
                    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
            local_css("style.css")


            
            



        
            
              

      