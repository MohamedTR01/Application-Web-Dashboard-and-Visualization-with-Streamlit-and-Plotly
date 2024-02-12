import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
import os
import io
from io import BytesIO
import warnings
import qrcode


warnings.filterwarnings('ignore')



path_file = os.getcwd() + '/Img/Icone.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Social Media & Sales | Home',
    page_icon=logo,
    layout='wide'
)



qr_datasource1 = qrcode.make("https://www.kaggle.com/datasets/thedevastator/uncovering-millennials-shopping-habits-and-socia")
qr_datasource2 = qrcode.make("https://www.searchlogistics.com/learn/statistics/social-media-addiction-statistics")

col_logos_1,col_logos_2,col_logos_3 = st.columns([1,8,1])
with st.container():
    with col_logos_2:
        st.markdown("""
                <style>
                    .logos {
                        background-color: white;
                        height: 170px;
                        display: flex;
                        justify-content: space-between;
                        align-items: center;
                        border-radius: 0 0 5px 5px;
                    }
                    
                </style>
                <div class="logos">
                <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/Fsjest.jpg" title="Fsjest" alt="Fsjest" width="150" height="150" />
                <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/Master%20DSEF.png" title="DSEF" alt="DSEF" width="400" height="150"/>
                <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/Faculty%20Official/UAE.png" title="UAE" **alt="UAE" width="150" height="150" /> 
                </div>
        """,unsafe_allow_html=True)

st.markdown("""---""")
st.markdown("""
<h1><center>Project : Interactive analysis of social networks and their impact on online sales</center></h1>
""",unsafe_allow_html=True)
st.markdown("""---""")
# st.image('./Img/Online Influencer Marketing.jpg')
# <center><img src='https://inkbotdesign.com/wp-content/uploads/2019/04/social-media-marketing-target-audience-1536x1022.jpg' width = 900px height = 599px/></center>
with st.container():
    st.markdown("""
    <center><img src='https://media.licdn.com/dms/image/C4D12AQFGV3tgn2m2JA/article-cover_image-shrink_720_1280/0/1604667263365?e=1709164800&v=beta&t=rkoq7ela4RuX-_KGD1cY28MR7NbP41DyBCvSOl10k3M' width="1000" height="500"/></center>
    """,unsafe_allow_html=True)
st.markdown("""
<br><br>
""",unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.1rem;}</style>',unsafe_allow_html=True)


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



with st.container():
    
    col_team0, col_team1, col_team2, col_team3 = st.columns([1,4,4,1])
    with col_team1:
        st.markdown("""
                <style>
                    .centered-header {
                        text-align: center;
                    }
                </style>
            """, unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Realized by :</h2>', unsafe_allow_html=True)
        team = pd.DataFrame({'Names':['ACHARGUI AFKIR AYMANE','TRIBAK MOHAMMED','ZAID ILYASS']})
        fig = ff.create_table(team, height_constant=30, colorscale=[[0, '#02365e'],[.5, '#b3cce3'],[1, '#b3cce3']])
        fig.update_layout(font=dict(size=20))
        st.plotly_chart(fig, use_container_width=True)  

    with col_team2:
        st.markdown("""
                <style>
                    .centered-header {
                        text-align: center;
                    }
                </style>
            """, unsafe_allow_html=True)
        st.markdown('<h2 class="centered-header">Proposed by</h2>', unsafe_allow_html=True)
        team = pd.DataFrame({'Prof':['Mohamed DRISSI BAKHKHAT']})
        fig = ff.create_table(team, height_constant=30, colorscale=[[0, '#02365e'],[.5, '#b3cce3'],[1, '#b3cce3']])
        fig.update_layout(font=dict(size=30))
        st.plotly_chart(fig, use_container_width=True)


st.markdown("""---""")
with st.container():
    st.markdown("""
    <h2>Data Source :</h2>
    """,unsafe_allow_html=True)
    # Convert PilImage to bytes
    img_bytes_1 = BytesIO()
    img_bytes_2 = BytesIO()
    qr_datasource1.save(img_bytes_1, format='PNG')  # Assuming PNG format, change accordingly
    qr_datasource2.save(img_bytes_2, format='PNG')
    # datasource_col0,datasource_col1,datasource_col2 = st.columns([1,8,1])
    datasource_col = st.columns([1,1,1,1])
    with datasource_col[0]:
        # Display the QR code in Streamlit
        st.image(img_bytes_1, caption='Data Source QR Code')
    with datasource_col[2]:
        st.image(img_bytes_2, caption='Data Source QR Code')

st.markdown("""---""")
st.subheader('Tools :')
tool1,tool2,tool3,tool4,tool5,tool6,tool7,tool8,tool9= st.columns(9)
st.markdown("""
        <style>
            .image {
                background-color: transparent;
                border: none;  /* Remove the button border */
                background-color: white;
                width: 100px;
                height: 100px;
                border-radius: 5px;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .image img {
                position:relative
                padding:5px;
            }
            .image:hover {
                background-color: #999999;
            }
            .github_actions {
                padding: 15px 5px 0px 5px;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
            }
            
            .github_actions p {
                color: black;
                font-size: 14px;
            }
   
        </style>
    """, unsafe_allow_html=True)
with tool1:
        st.markdown("""
                    <div class="image">
                    <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/python/python-original-wordmark.svg" alt="" with=80 height=80>
                    </div>
                    
                    """, unsafe_allow_html=True)
with tool2:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/vscode/vscode-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool3:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/git/git-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool4:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/docker/docker-plain-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool5:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/numpy/numpy-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)
with tool6:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/pandas/pandas-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)

with tool7:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/elghallali/my-images/aff6e3ea2f3f31483187856b7c9d412852c9205c/streamlit-logo-primary-colormark-darktext.svg" alt="" with=80 height=60>
                 </div>
                 """, unsafe_allow_html=True)
with tool8:
        st.markdown("""
                 <div class="image">
                 <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/plotly/plotly-original.svg" />
                 </div>
                 """, unsafe_allow_html=True)
with tool9:
        st.markdown("""
                 <div class="image">
                 <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/github/github-original-wordmark.svg" alt="" with=80 height=80>
                 </div>
                 """, unsafe_allow_html=True)

        

st.markdown(
    f"""
    <style>
    table {{
        transform: scale(1.5); /* Zoom de 1.5 fois la taille normale */
    }}
    </style>
    """,
    unsafe_allow_html=True
)