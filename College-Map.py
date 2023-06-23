import pandas as pd
import streamlit as st


st.set_page_config(
    page_icon=":atom:",
    page_title="Atomic Universe",)

    # Insert custom CSS sidebar and background
st.markdown("""
    <style>
    div [data-testid="stAppViewContainer"]{
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
    [data-testid="stHeader"]{
        background: linear-gradient(135deg, #072b79 0%, #02090a 100%)  !important;
        }
  
        </style>""", unsafe_allow_html=True)

st.header("Programas Acadêmicos nos EUA")
# Create a DataFrame from the processed data
df = pd.read_excel('data/college.xlsx', sheet_name="Colleges")

col1, col2 = st.columns(2)

with col1:
    chart_data = df['Student Population']     
    st.bar_chart(chart_data)

with col2:
    chart_data = df['Undergraduate Students']     
    st.bar_chart(chart_data)


chart_data = df['Public/Private']
st.bar_chart(chart_data)


  # Get a list of unique states from the DataFrame

cities = df["City"].unique().tolist()

        # Select a state using the st.selectbox
selected_city = st.multiselect("Selecione uma cidade:", cities)
        

if selected_city:
     for i in range(len(selected_city)):
        selected_colleges = df[df["City"] == selected_city[i]]
        

        college_names = selected_colleges["College Name"].tolist()
        degrees_offered = selected_colleges["Degrees Offered"].tolist()
            
        link  = selected_colleges["Profile Link to College Navigator"].tolist()
      

        st.subheader("Instituições em  {}".format(selected_city))
        st.write('\n')
        st.write('\n')
            # Display college names and degrees offered
        for i in range(len(college_names)):

                col1, col2, col3 = st.columns(3)
                with col1:
                  st.write("Nome da instituição:", college_names[i])
                with col2:
                  st.write("Graus oferecidos:", degrees_offered[i])
                with col3: 
                 st.write("Link:", link[i] )
                 st.write("----------------")
