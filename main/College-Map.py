import streamlit as st
import pandas as pd
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

image = Image.open('assets/academic.jpg')

st.image(image, caption='Image by rawpixel.com on Freepik')

# main code goes here

with streamlit_analytics.track():

    def main():

        st.title("Programas Acadêmicos nos EUA")
        st.subheader('Dados originais:')
        df = pd.read_excel("data/College_Map_Results2023_05_23_23.46.18.xls")
        st.write(df)
        st.write('\n')
        st.write('\n')

        st.subheader('Dados filtrados:')
        # Load the Excel file containing the college data
        st.write('\n')
        df = pd.read_excel("data/College_Map_Results2023_05_23_23.46.18.xls", sheet_name="Colleges")

        # Get a list of unique states from the DataFrame
        cities = df["City"].unique().tolist()

        # Select a state using the st.selectbox
        selected_city = st.multiselect("Selecione uma cidade:", cities)
        

        if selected_city:
            for i in range(len(selected_city)):
                selected_colleges = df[df["City"] == selected_city[i]]
        

            college_names = selected_colleges["College Name"].tolist()
            degrees_offered = selected_colleges["Degrees Offered"].tolist()
            
            tuition = selected_colleges["Published Out-of-state Tuition and Fees ($)"].tolist()
            link  = selected_colleges["Profile Link to College Navigator"].tolist()

            st.subheader("Instituições em  {}".format(selected_city))
            st.write('\n')
            st.write('\n')
            # Display college names and degrees offered
            for i in range(len(college_names)):

                col1, col2, col3, col4 = st.columns(4)
                with col1:
                  st.write("Nome da instituição:", college_names[i])
                with col2:
                  st.write("Graus oferecidos:", degrees_offered[i])
                with col3:
                    st.write("Valor de Bolsas:", tuition[i])
                with col4:
                    st.write("Link do Perfil da Instituição:", link[i])
                    st.write("-----------")

                    
    if __name__ == "__main__":
        main()
