import streamlit as st
import tensorflow_datasets as tfds
import streamlit_analytics

st.set_page_config(
    page_icon=":atom:",
    page_title="Atomic Universe",)

    # Insert custom CSS sidebar and background
st.markdown("""
    <style>
    section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 30px !important;
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
    section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 30px !important;
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
    div [data-testid="stAppViewContainer"]{
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
    [data-testid="stHeader"]{
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
    div [data-testid="stImage"]{
    width: 800px !important
    }

        </style>""", unsafe_allow_html=True)

from PIL import Image

image = Image.open('assets/fingerprint.jpg')

st.image(image, caption='Image by pikisuperstar on Freepik')


with streamlit_analytics.track():

    st.title('Projetos de Machine Learning')
    st.write('\n')
    st.write('\n')
    # List all available dataset collections
    dataset_list = tfds.list_builders()

    # Iterate through each dataset collection and display information about them
    for dataset_name in dataset_list:
        dataset = tfds.builder(dataset_name)

        col1, col2 = st.columns(2)
        with col1:
            st.write("Dataset Name:", dataset_name)
        with col2:
            st.write("Dataset Homepage:", dataset.info.homepage)
        
        st.write('\n')
        st.subheader('Dataset Summary')
        st.write(dataset.info.description)
        st.write('\n')
        st.subheader('Dataset Citation')
        st.write(dataset.info.citation)
        
        st.write("--------")
