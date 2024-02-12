import streamlit as st
import pandas as pd
from PIL import Image
import os
import io
import glob
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from streamlit_extras.metric_cards import style_metric_cards




path_file = os.getcwd() + '/Img/Icone.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Social Media & Sales | Dashboard',
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


df1 = pd.read_csv('./Data/Social Influence on Shopping.csv')
df2 = pd.read_csv('./Data SM/Gender Uses Social Media More By Platform.csv')
df3 = pd.read_csv('./Data SM/Gender Uses Social Media More By Region.csv')
df4 = pd.read_csv('./Data SM/Social Media Usage By Age.csv')
df5 = pd.read_csv('./Data SM/Social Media Usage By Country.csv')
df6 = pd.read_csv('./Data SM/What Are The Most Used Social Media Platforms.csv')
df7 = pd.read_csv('./Data SM/Average Number of Social Media Accounts By Years.csv')
df8 = pd.read_csv('./Data SM/Social Media Addiction Statistics Amongst Teenagers.csv')


st.markdown(f'# <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/E-business/SM.png" alt="logo" width=200/>  Analysis & Visualization',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.5rem;}</style>',unsafe_allow_html=True)

with st.container():
    tab_1, tab_2 = st.tabs(['Social Media Worldwide Usage Statistics','Social Influence on Shopping'])
    # tab_0 = st.tabs(['Social Influence on Shopping'])

    with tab_1 : 
        with st.container():
            st.header('1️⃣ Social Media Usage By Gender :')
            st.markdown('---')
            fig1 = px.bar(df2,x='Social Media',y=['Female User (%)','Male User (%)'],labels={'value':'Percentage (%)','Social Media':'Social Media','variable':'Gender'})
            st.plotly_chart(fig1, use_container_width=True)    

            # with col_team11[1] :
                # Reformatter les données pour les utiliser dans Plotly Express
                # fig2 = px.pie(df2, values='Female User (%)', names='Social Media', title='Répartition des utilisateurs par sexe sur les réseaux sociaux')
                # st.plotly_chart(fig2, use_container_width=True)
                # for column in df2.columns[1:]:  # Exclure la première colonne (noms des plateformes)
                # # Créer un diagramme circulaire avec Plotly Express
                #     fig2 = px.pie(df2, values=column, names='Social Media', title=f'Répartition des utilisateurs par genre pour {column}',
                #     labels={'Social Media': 'Plateforme de médias sociaux', column: 'Pourcentage'}, hole=0.3)
                #     st.plotly_chart(fig2, use_container_width=True)

                # fig2 = px.pie(df2, values='Female User (%)', names='Social Media', title='Répartition des utilisateurs par sexe sur les réseaux sociaux')
                # fig2.update_traces(textposition='inside', textinfo='percent+label')
                # st.plotly_chart(fig2, use_container_width=True)
            title = ['Female','Male']
            col_team22 = st.columns([1,1])
            with col_team22[0] :
                fig2 = px.pie(df2, values='Female User (%)', names='Social Media', title=f'Distribution Of Users By Gender For {title[0]}')
                fig2.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig2, use_container_width=True)
            
            with col_team22[1] :
                fig2 = px.pie(df2, values='Male User (%)', names='Social Media', title=f'Distribution Of Users By Gender For {title[1]}')
                fig2.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig2, use_container_width=True)


            with st.expander('1️⃣ Result'):
                st.markdown('''
                <h5>🌟 Social media sites that have significantly more female users are : </h5>
                <ul>
                <li>Snapchat</li>
                <li>Pinterest</li>
                <li>Instagram</li>
                <li>Tiktok</li>
                </ul>
                <h5>
                <br>
                <h5>🌟 Men tend to use : </h5>
                <ul>
                <li>Twitter</li>
                <li>LinkedIn</li>
                <li>YouTube</li>
                </ul>
                <h5>    
                <h4>More than women do. It’s clear that some social media sites tend to be more attractive to different genders.</h4>
                ''',unsafe_allow_html=True)
            
            st.markdown('---')
            st.header('2️⃣ Social Media Usage by Regions : ')
            st.markdown('---')
            fig3 = px.bar(df3,x='Region',y=['Female','Male'],labels={'value':'Percentage (%)','Social Media':'Social Media','variable':'Gender'})
            st.plotly_chart(fig3, use_container_width=True)   
            

            # selected_region = st.radio('Select Region', df3['Region'].unique())
            selected_region = st.selectbox('Select Region', df3['Region'].unique())
            filtered_df = df3[df3['Region'] == selected_region]
            fig4 = px.pie(filtered_df, values=[filtered_df['Female'].sum(), filtered_df['Male'].sum()], 
            names=['Female', 'Male'],
            color= ['Female', 'Male'],
            title=f'Social Media Use By Gender - {selected_region}',
            hole=0.3,
            width=1200,
            height=600,
            color_discrete_map = {'Female': '#73122e','Male': '#1f3e70'})
            # color_discrete_map={'Female':'darkblue','Male':'cyan'})
            fig4.update_traces(marker = dict(line = dict(color = 'white', width = 2)))
            st.plotly_chart(fig4, use_container_width=True)

            with st.expander('2️⃣ Result'):
                st.markdown('''
                + <font face='Microsoft Tai Le'>Southern Asia has the most significant difference between male and female users. Almost 3 out of 4 social media accounts are for men in this region.</font>

                + <font face='Microsoft Tai Le'>In all other regions, females are the biggest users with the exception of Western Europe, where it is even.</font>

                + <font face='Microsoft Tai Le'>Worldwide women tend to use social media more than men. When you break it down by region women dominate all but one of the major regions in the world.</font>

                + <font face='Microsoft Tai Le'>Women also spend more time on social media than men do.</font>
                ''',unsafe_allow_html=True)
            
            st.markdown('---')
            st.header('3️⃣ Social Media Usage By Age :')
            st.markdown('---')
            fig5 = px.bar(df4,x='Percentage (%)',y='Age Group',labels={'Age Group':'Age','Social Media':'Social Media'},text='Percentage (%)')
            # fig5.update_traces(marker_color='darkred')
            fig5.update_traces(marker_color='#3480eb')
            st.plotly_chart(fig5, use_container_width=True)    
            with st.expander('3️⃣ Result'):
                st.markdown('''
                + <font face='Microsoft Tai Le'>The drop from the 50-64 age group to 65+ is significant. This may be because people over 65+ never adapted to social media compared to other age groups.</font>
                ''',unsafe_allow_html=True)
            
            st.markdown('---')
            st.header('4️⃣ Social Media Usage By Country :')
            st.markdown('---')
            fig6 = px.bar(df5,x=df5['Percentage (%)'],y=df5['Country'],text='Percentage (%)')
            # fig5.update_traces(marker_color='darkred')
            fig6.update_traces(marker_color='#3480eb')
            st.plotly_chart(fig6, use_container_width=True) 
            with st.expander('4️⃣ Result'):
                st.markdown('''
                + <font face='Microsoft Tai Le'>These statistics show the share of internet users in selected countries visiting social networking sites as of 2023.</font>
                + <font face='Microsoft Tai Le'>The UAE has a huge number of social media users compared to the rest of the world. 105.5% of all internet users in the UAE actively use and visit at least one social media website.</font>
                + <font face='Microsoft Tai Le'>South Korea, Hong Kong and the Netherlands are also big social media users.</font>
                + <font face='Microsoft Tai Le'>The big English speaking countries such as the US and England don't feature in the top 15 countries in the world. Surprising!</font>
                ''',unsafe_allow_html=True)
            # col_team33 = st.columns([1,1])
            # with col_team33[0]:  
            st.markdown('---')
            st.header('5️⃣ Social Media Usage By Users :')      
            st.markdown('---')     
            fig7 = px.bar(df6,x='Users (in millions)',y='Social Media Network',text='Users (in millions)',width=1200,height=600)
            # fig5.update_traces(marker_color='darkred')
            fig7.update_traces(marker_color='#3480eb')
            st.plotly_chart(fig7, use_container_width=True) 

            fig8 = px.pie(df6, values='Users (in millions)', names='Social Media Network', title='Distribution Of Users By Social Media :',width=1200,height=600)
            fig8.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig8, use_container_width=True)

            with st.expander('5️⃣ Result'):
                 st.markdown('''
                + <font face='Microsoft Tai Le'>Facebook has 2.85 billion active users while YouTube has 2.29 billion active users.</font>
                + <font face='Microsoft Tai Le'>Facebook was the first social media platform to ever pass the 1 billion active user mark.</font>
                + <font face='Microsoft Tai Le'>Ever since its launch, Facebook has been the biggest social media platform when ranked by active user base.</font>
                ''',unsafe_allow_html=True)

            st.markdown('---')
            st.header('6️⃣ Average Number of Social Media Accounts By Years :')
            st.markdown('---')
            fig9 = px.line(df7, x="Years", y="Average Number of Social Media Accounts",labels={"Average Number of Social Media Accounts":"Average Number of Social Media"},)
            st.plotly_chart(fig9, use_container_width=True)

            fig10 = px.bar(df7,x='Years',y='Average Number of Social Media Accounts',color_discrete_sequence=px.colors.qualitative.Set2_r)
            st.plotly_chart(fig10, use_container_width=True)

            with st.expander('6️⃣ Result'):
                st.markdown('''
                + <font face='Microsoft Tai Le'>There are thousands of social media apps and platforms all over the world. They are all constantly fighting for your attention.</font>
                + <font face='Microsoft Tai Le'>The average person has 8-9 social media accounts. This has doubled since 2013, when the average person just had 4-5 accounts.</font>
                + <font face='Microsoft Tai Le'>It’s important to know that messaging platforms such as WhatsApp and Facebook Messenger are included in this statistic. The number also varies significantly depending on the country.</font>
                ''',unsafe_allow_html=True)

            st.markdown('---')
            st.header('7️⃣ Social Media Addiction Statistics Amongst Teenagers :')
            st.markdown('---')
            fig11 = px.bar(df8,x=['Low Emotional Well-Being (%)','High Emotional Well-Being (%)'],y='Negative Social Media Affect',labels={'value':'Percentage (%)','variable':''})
            st.plotly_chart(fig11, use_container_width=True) 

            with st.expander('7️⃣ Result'):
                st.markdown('''
                + <font face='Microsoft Tai Le'>43% of young people feel very bad if no one likes their social media posts.</font>
                + <font face='Microsoft Tai Le'>This is a big driver for teens to be using social media constantly and posting things that get engagement.</font>
                + <font face='Microsoft Tai Le'>It also seems that negative experiences on social media don’t stop teens from using it.</font>
                ''',unsafe_allow_html=True)

            









    with tab_2: 
        with st.container():
            #st.subheader('Select Answers')
            selected_answers = st.multiselect('Select Answers',df1['Answer'].unique(),default=df1['Answer'].unique())
            filtered_df = df1[df1['Answer'].isin(selected_answers)]
            st.write('---')
            st.subheader('The greatest and least impact of social media on sales')
            st.markdown(f'<hr style="border-top: 0.2rem solid #147bba ; margin-top: -10px; margin-bottom: 10px;">', unsafe_allow_html=True)
            col12 = st.columns([1,1])
            df11 = df1[df1['Answer']=='Instagram']
            with st.expander("1️⃣ Description"):
                st.markdown('''
                + <font face='Microsoft Tai Le'>Analytical dashboard containing two indicators concerning the impact of two social networking platforms. On the left, Instagram is shown as having the "Maximum Impact" and on the right, Snapchat is shown as having the "Worst Impact".</font>
                ''',unsafe_allow_html=True)
            st.subheader('Comparative analysis of social networks on sales')
            st.markdown(f'<hr style="border-top: 0.2rem solid #147bba ; margin-top: -10px; margin-bottom: 10px;">', unsafe_allow_html=True)
            col12[0].metric("🔺Top Impact","Instagram")
            df11 = df1[df1['Answer']=='Snapchat']
            col12[1].metric("🔻Worst Impact","Snapchat")
            style_metric_cards(background_color="#b8c3e3",border_left_color="#147bba",border_color="#1f66bd",box_shadow="#F71938")



            st.subheader("Histogram and Pie Chart of Answer and Count")
            col_team1, col_team2 = st.columns([1,1])
            with col_team1 :
                fig12 = px.bar(filtered_df,x='Answer',y='Count',barmode='group')
                st.plotly_chart(fig12, use_container_width=True)
            with col_team2 : 
                fig13 = px.pie(filtered_df, values='Count', names='Answer')
                st.plotly_chart(fig13, use_container_width=True)

            with st.expander("2️⃣ Description"):
                st.markdown('''
                + <font face='Microsoft Tai Le'>Two graphs analyzing the impact of different social networks on sales. The first is a bar chart showing that Instagram has the greatest influence, followed by Facebook, while Snapchat and Twitter have a lesser impact. The second is a pie chart showing that a large proportion of sales come from other, unspecified sources, with Instagram and Facebook as significant contributors, and Twitter and Snapchat less influential.</font>
                ''',unsafe_allow_html=True)

            st.subheader("Histogram and Pie Chart of Segment Type and Count")

            col_team33 = st.columns([1,1])
            with col_team33[1] :
                fig14 = px.pie(filtered_df, values='Count', names='Segment Type')
                st.plotly_chart(fig14, use_container_width=True)

            with col_team33[0]:
                fig15 = px.bar(filtered_df,x='Count',y='Segment Type',barmode='group')
                st.plotly_chart(fig15, use_container_width=True)

            with st.expander("3️⃣ Description"):
                st.markdown('''
                + <font face='Microsoft Tai Le'>Two graphs relating to user or customer segmentation. A bar chart shows that the "Custom" category is the largest, while a pie chart illustrates that "Custom" represents the majority, with other categories such as "Mobile", "Gender", "University" and "Web" forming a small fraction of the whole.</font>
                ''',unsafe_allow_html=True)

            st.subheader("Histogram of Segment Description and Count")
            # Création de l'histogramme avec Plotly
            def plot_histogram(data):
                fig16 = px.bar(data, x='Segment Description', y='Count', color='Segment Description', barmode='group',
                            labels={'Segment Description': 'Segment Description', 'Count': 'Count'},
                            )
                
                fig16.update_layout(
                    width=800,  # Largeur en pixels
                    height=800,  # Hauteur en pixels
                )
                return fig16

            # Filtrer les données pour ne garder que celles qui ont Count > 0
            filtered_data = df1[df1['Count'] > 0]

            # Afficher l'histogramme
            st.plotly_chart(plot_histogram(filtered_data), use_container_width=True)

            with st.expander("4️⃣ Description"):
                st.markdown('''
                + <font face='Microsoft Tai Le'>a histogram listing different segments, probably users or customers, by type and number. There is a wide variety of segments displayed, with an uneven distribution of accounts among them. Several categories such as "Mobile", "Web", "Gender", "University" and "Custom" are distinguished by colors, indicating a variety of segments with different numbers associated with each.</font>
                ''',unsafe_allow_html=True)












    
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots



# # Create subplots: use 'domain' type for Pie subplot
# fig11 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
# fig11.add_trace(go.Pie(labels=df3['Region'], values=df3['Female'], name="GHG Emissions",label0='Gender'),
#               1, 1,)
# fig11.add_trace(go.Pie(labels=df3['Region'], values=df3['Male'], name="CO2 Emissions",
#               1, 2)

# # Use `hole` to create a donut-like pie chart
# fig11.update_traces(hole=.4, hoverinfo="label+percent+name")

# st.plotly_chart(fig11, use_container_width=True)


# import streamlit as st
# import plotly.graph_objects as go
# import pandas as pd

# # Créer un DataFrame avec vos données
# data = {
#     'Social Media': ['Snapchat', 'Pinterest', 'Instagram', 'Facebook', 'Twitter', 'LinkedIn', 'TikTok', 'YouTube'],
#     'Female User (%)': [60, 78, 57, 44, 32, 49, 59, 45],
#     'Male User (%)': [40, 22, 43, 56, 68, 51, 41, 55]
# }
# df = pd.DataFrame(data)

# # Créer un diagramme circulaire avec Plotly Express
# fig = go.Figure()

# # Ajouter les données pour chaque réseau social
# for index, row in df.iterrows():
#     fig.add_trace(go.Pie(labels=['Female', 'Male'],
#                          values=[row['Female User (%)'], row['Male User (%)']],
#                          name=row['Social Media'],
#                          textinfo='label+percent',
#                          hole=0.3))

# # Mise en forme du titre
# fig.update_layout(title='Répartition des utilisateurs par sexe sur les réseaux sociaux')

# # Afficher le diagramme dans Streamlit
# st.plotly_chart(fig)