import streamlit as st
import pandas as pd
from PIL import Image
import os
import io
import glob
import base64

path_file = os.getcwd() + '/Img/Icone.png'
logo = Image.open(path_file)


st.set_page_config(
    page_title='Social Media & Sales | Dataset',
    page_icon=logo,
    layout='wide'
)

st.markdown(f'# <img src="https://raw.githubusercontent.com/MohamedTR01/My_Images/master/E-business/SM.png" alt="logo" width=200/> Dataset',unsafe_allow_html=True)
st.markdown('<style> div.block-container {padding-top: 0.5rem;}</style>',unsafe_allow_html=True)


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Chargement des données depuis le fichier CSV
data = {
    # 'Online Influencer Marketing - Thought Catalog Influencers': pd.read_csv('./Data/Online Influencer Marketing - Thought Catalog Influencers.csv'),
    'Gender Uses Social Media More By Platform': pd.read_csv('./Data SM/Gender Uses Social Media More By Platform.csv'),
    'Gender Uses Social Media More By Region': pd.read_csv('./Data SM/Gender Uses Social Media More By Region.csv'),
    'Social Media Usage By Age': pd.read_csv('./Data SM/Social Media Usage By Age.csv'),
    'Social Media Usage By Country': pd.read_csv('./Data SM/Social Media Usage By Country.csv'),
    'What Are The Most Used Social Media Platforms': pd.read_csv('./Data SM/What Are The Most Used Social Media Platforms.csv'),
    'Average Number of Social Media Accounts By Years': pd.read_csv('./Data SM/Average Number of Social Media Accounts By Years.csv'),
    'Social Media Addiction Statistics Amongst Teenagers': pd.read_csv('./Data SM/Social Media Addiction Statistics Amongst Teenagers.csv'),
    'Social Influence on Shopping': pd.read_csv('./Data/Social Influence on Shopping.csv')
}

def visualDataFrame(df, title):
    with st.expander("🎯 Data Preview :"):
        options = st.multiselect(
            'DataFrame Columns',
            list(df.columns),
            list(df.columns),
            key=f"{title}_multiselect"  # Utilisation d'une clé unique pour chaque widget multiselect
        )

        tab1, tab2, tab3, tab4, tab5 = st.tabs([":card_file_box: Data", "Types", 'NAN', 'Info', 'Unique Values'])
        with tab1:
            st.subheader(":card_file_box: Data")
            st.dataframe(df[options])

        with tab2:
            st.subheader("Column types:")
            st.text(df[options].dtypes)

        with tab3:
            st.subheader("Null values:")
            st.text(df[options].isna().sum())

        with tab4:
            st.subheader('DataFrame Info')
            st.text(df[options].info())

        with tab5:
            st.subheader('Unique Values')
            st.text(df[options].nunique())

        # Bouton pour télécharger les données visualisées
        if st.button(f"Télécharger les données de {title}", key=f"{title}_download_button"):
            csv = df[options].to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Encodage des données au format CSV en base64
            href = f'<a href="data:file/csv;base64,{b64}" download="{title}_data.csv">Télécharger le fichier CSV</a>'
            st.markdown(href, unsafe_allow_html=True)

# Affichage des DataFrame sélectionnés
data_set = st.multiselect(
    '**Data Frames**',
    list(data.keys()),
    list(data.keys()),
    key="data_frames_multiselect"  # Utilisation d'une clé unique pour le widget multiselect principal
)

for dataset in data_set:
    st.write(f"### {dataset}")
    visualDataFrame(data[dataset], dataset)





# import pandas as pd
# import streamlit as st

# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Chargement des données depuis le fichier CSV
# data = {
#     'Social Influence on Shopping': pd.read_csv('./Data/Social Influence on Shopping.csv'),
#     'Online Influencer Marketing - Thought Catalog Influencers': pd.read_csv('./Data/Online Influencer Marketing - Thought Catalog Influencers.csv')
# }

# def visualDataFrame(df, title):
#     with st.expander("Data Preview"):
#         options = st.multiselect(
#             f'{title} - DataFrame Columns',
#             list(df.columns),
#             list(df.columns),
#             key=f"{title}_multiselect"  # Utilisation d'une clé unique pour chaque widget multiselect
#         )

#         tab1, tab2, tab3, tab4, tab5 = st.tabs([":card_file_box: Data", "Types", "NAN", "Info", "Unique Values"])
#         with tab1:
#             st.subheader(":card_file_box: Data")
#             st.dataframe(df[options])

#         with tab2:
#             st.subheader("Column types:")
#             st.text(df[options].dtypes)

#         with tab3:
#             st.subheader("Null values:")
#             st.text(df[options].isna().sum())

#         with tab4:
#             st.subheader('DataFrame Info')
#             st.text(df[options].info())

#         with tab5:
#             st.subheader('Unique Values')
#             st.text(df[options].nunique())

#         if st.button("Télécharger les données"):
#             csv = df[options].to_csv(index=False)
#             b64 = base64.b64encode(csv.encode()).decode()  # Encodage des données au format CSV en base64
#             href = f'<a href="data:file/csv;base64,{b64}" download="{title}_data.csv">Télécharger le fichier CSV</a>'
#             st.markdown(href, unsafe_allow_html=True)

# # Affichage des DataFrame sélectionnés
# data_set = st.multiselect(
#     '**Data Frames**',
#     list(data.keys()),
#     list(data.keys()),
#     key="data_frames_multiselect"  # Utilisation d'une clé unique pour le widget multiselect principal
# )

# for dataset in data_set:
#     st.write(f"### {dataset}")
#     visualDataFrame(data[dataset], dataset)



''''''''''''''''''''




# import streamlit as st
# import pandas as pd
# import io

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)


# import pandas as pd
# import streamlit as st

# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Chargement des données depuis le fichier CSV
# data = {
#     'Social Influence on Shopping': pd.read_csv('./Data/Social Influence on Shopping.csv'),
#     'Online Influencer Marketing - Thought Catalog Influencers': pd.read_csv('./Data/Online Influencer Marketing - Thought Catalog Influencers.csv')
# }

# def visualDataFrame(df, title):
#     with st.expander(f"{title} - Data Preview"):
#         options = st.multiselect(
#             'DataFrame Columns',
#             list(df.columns),
#             list(df.columns)
#         )

#         tab1, tab2, tab3, tab4, tab5 = st.columns(5)
#         with tab1:
#             st.subheader(":card_file_box: Data")
#             st.dataframe(df[options])

#         with tab2:
#             st.subheader("Column types:")
#             st.text(df[options].dtypes)

#         with tab3:
#             st.subheader("Null values:")
#             st.text(df[options].isna().sum())

#         with tab4:
#             st.subheader('DataFrame Info')
#             st.text(df[options].info())

#         with tab5:
#             st.subheader('Unique Values')
#             st.text(df[options].nunique())

# # Affichage des DataFrame sélectionnés
# data_set = st.multiselect(
#     '**Data Frames**',
#     list(data.keys()),
#     list(data.keys()))

# for dataset in data_set:
#     st.write(f"### {dataset}")
#     visualDataFrame(data[dataset], dataset)




# import pandas as pd
# import streamlit as st
# import io

# hide_st_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# header {visibility: hidden;}
# </style>
# """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# # Chargement des données depuis le fichier CSV
# SM = pd.read_csv('./Data/Social Influence on Shopping.csv')
# SMA = pd.read_csv('./Data/Online Influencer Marketing - Thought Catalog Influencers.csv')

# list_ = [('Social Influence on Shopping', 'Social Influence on Shopping'),('Online Influencer Marketing - Thought Catalog Influencers','Online Influencer Marketing - Thought Catalog Influencers')]  # Liste avec un tuple contenant le nom du DataFrame et son titre

# data = {}
# for item in list_:
#     df, title = item
#     data[title] = df

# def visualDataFrame(df, title):
#     with st.expander("Data Preview"):
#         options = st.multiselect(
#             'DataFrame Columns',
#             list(df.columns),
#             list(df.columns)
#             )

#         tab1, tab2, tab3, tab4, tab5 = st.tabs([":card_file_box: Data", "Types", "NAN", "Info", "Unique Values"])
#         with tab1:
#             st.subheader("A tab with data")
#             st.dataframe(df[options])

#         with tab2:
#             st.subheader("Column types:")
#             st.text(df[options].dtypes)

#         with tab3:
#             st.subheader("Null values:")
#             st.text(df[options].isna().sum())

#         with tab4:
#             st.subheader('DataFrame Info')
#             st.text(df[options].info())

#         with tab5:
#             st.subheader('Unique Values')
#             st.text(df[options].nunique())

# # Affichage des DataFrame sélectionnés
# data_set = st.multiselect(
#     '**Data Frames**',
#     list(data.keys()),
#     list(data.keys()))

# for dataset in data_set:
#     st.write(f"### {dataset}")
#     visualDataFrame(SM,dataset)
