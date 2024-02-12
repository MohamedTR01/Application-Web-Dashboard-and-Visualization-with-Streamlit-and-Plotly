import streamlit as st
import pandas as pd
from PIL import Image
import os
import io
import glob
from streamlit_extras.metric_cards import style_metric_cards


path_file = os.getcwd() + '/Img/Icone.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Social Media & Sales | About',
    page_icon=logo,
    layout='wide'
)

hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# st.snow()
st.markdown(f'# <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/E-business/SM.png" alt="logo" width=200/> About',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.5rem;}</style>',unsafe_allow_html=True)

with st.container():
    st.write('''
    <div style="border: 1px solid white; padding: 10px; background-color: #2d5166;">
    <center><h2 style="color: white;">Interactive analysis of social networks and their impact on online sales</h2></center>
    </div>
    ''', unsafe_allow_html=True)

    st.write('---')
    st.header('✅ Interactive Social Network Analysis for Data Diversification')
    st.markdown('''
    <b><font size="5">Description :  </font></b>

    <font>The Interactive Social Network Analysis project focuses on using up-to-date data, collected until December 2023, to explore various aspects of online behavior, with particular emphasis on demographics, platform, account averaging, and teen addiction statistics.</font>
    
    <b><font size="5" >Key features of the Project :  </font></b>

    + <b><font>Data diversification : </font></b><font>The data collected includes varied information such as gender, region, age, country, social networking platforms, and average accounts per user. This diversification offers a comprehensive perspective of online users.</font>
    + <b><font>Demographic analysis : </font></b><font>The project examines the distribution of users by gender, region, age and country, providing crucial information on the demographic make-up of social network users.</font>
    + <b><font>Social Network Platforms :  </font></b><font>The analysis focuses on different social network platforms, assessing relative popularity, preferences and trends among users.</font>
    + <b><font>Average Accounts : </font></b><font>The study calculates the average number of accounts held by each user, providing insights into the level of online engagement and interaction.</font>
    + <b><font>Teen Addiction Statistics : </font></b><font>An in-depth analysis of social network addiction statistics among teenagers is carried out, highlighting trends, contributing factors, and offering recommendations for healthy use.</font>

    <b><font size="5">Project objectives :  </font></b>
    + <b><font>Understand the diversity of social network users according to several parameters.</font>
    + <b><font>Identify emerging trends on different platforms.</font>
    + <b><font>Assess the impact of demographics on social network use.</font>
    + <b><font>Propose recommendations to promote responsible use of social networks, particularly among teenagers.</font>
    + <b><font>Understand the diversity of social network users according to several parameters.</font>

    <b><font size="5">Deliverables :</font></b>
    + <b><font>A detailed report on the results of the interactive analysis.</font>
    + <b><font>Interactive visualizations for easy understanding.</font>
    + <b><font>Recommendations based on the findings of the analysis.</font>
    ''',unsafe_allow_html=True)

    st.header('✅ Impact of Social Networks on Online Sales')
    st.markdown('''
    <b><font size="5">Description :  </font></b>

    <font>The project aims to analyze in depth the influence of social networks on online sales performance. To this end, an impressive database of 150 million questionnaires has been collected, providing significant scope for exhaustive analysis.</font>
    
    <b><font size="5" >Main components of the database :</font></b>

    + <b><font>Question : </font></b><font>Each questionnaire includes a series of specific questions relating to people's interactions with social networks and their online purchasing behavior.</font>
    + <b><font>Segment : </font></b><font>Data is segmented to enable more targeted analysis, potentially based on criteria such as demographics, geographic location, or online behavior.</font>
    + <b><font>Type : </font></b><font>This category specifies the type of question asked, enabling data to be grouped according to relevant themes, such as engagement on social networks, influence of online reviews, etc.</font>
    + <b><font>Description : </font></b><font>Each question is accompanied by a description, providing additional contextual information for accurate interpretation of the results.</font>
    + <b><font>Response : </font></b><font>Individuals' answers to the questions asked, providing crucial qualitative data for assessing opinions, attitudes and behaviors.</font>
    + <b><font>Number of Individual Responses per Question : </font></b><font>Indicates the number of individuals who responded to each question, making it possible to assess the representativeness of the data.</font>
    + <b><font>Number of Individual Responses per Question : </font></b><font>Provides a percentage measure of responses to each question, facilitating comparison and prioritization of results.</font>

      <b><font size="5">Project objectives :  </font></b>

    + <b><font>Analyze Engagement on Social Networks : </font></b><font>Examine how individuals interact with social media platforms and whether this influences their online purchasing decisions.</font>
    + <b><font>Assess the Impact of Online Reviews : </font></b><font>Investigate how reviews and comments on social networks affect consumer confidence and propensity to make online purchases.</font>
    + <b><font>Identify Trends in Purchasing Behavior : </font></b><font>Use data to identify significant trends in online purchasing behavior in relation to the use of social networks.</font>
    + <b><font>Propose Strategic Recommendations : </font></b><font>Based on the results, formulate recommendations for companies to improve their presence on social networks and optimize online sales strategies.</font>






    ''',unsafe_allow_html=True)
