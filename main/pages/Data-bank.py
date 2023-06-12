import streamlit as st
import requests
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

image = Image.open('assets/analysis.jpg')

st.image(image, caption='Made by Canvas')


with streamlit_analytics.track():
    def search_datasets(query):
        base_url = "https://api.osf.io/v2/"
        endpoint = "nodes/"
        url = f"{base_url}{endpoint}"

        headers = {"Content-Type": "application/vnd.api+json"}
        params = {
            "filter[title]": query,
            "page[size]": 10
        }

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        datasets = data["data"]
        return datasets

def main():
    st.title("Dataset Search")
    st.subheader('Ache dados de diversos setores para ajudar na sua pesquisa')
    query = st.text_input("Enter search query")
    if st.button("Search"):
        if query:
            datasets = search_datasets(query)
            st.success("Search completed.")
            if datasets:
                for dataset in datasets:
                    dataset_id = dataset["id"]
                    attributes = dataset["attributes"]
                    download = dataset["links"]

                    title = attributes["title"]
                    category = attributes.get("category", "")
                    description = attributes.get("description", "")
                    public = attributes.get("public", "")
                    tags = attributes.get("tags", [])
                    date_created = attributes.get("date_created", "")
                    date_modified = attributes.get("date_modified", "")
                    root = dataset["relationships"]["root"]["links"]["related"]["href"]
                    preprint = attributes.get("preprint", "")

                    st.write(f"ID: {dataset_id}")
                    st.write(f"Title: {title}")
                    st.write(f"Category: {category}")
                    st.write(f"Description: {description}")
                    st.write(f"Public: {public}")
                    st.write(f"Tags: {tags}")
                    st.write(f"Date Created: {date_created}")
                    st.write(f"Date Modified: {date_modified}")
                    st.write(f"Root: {root}")
                    st.write(f"Preprint: {preprint}")
                    st.write(f"download: {download}")
                    st.write("----")
            else:
                st.warning("No datasets found.")
        else:
            st.warning("Please enter a search query.")

if __name__ == "__main__":
    main()


keyword = st_tags_sidebar(
        value=['Análise de dados', 'Ciência de dados', 'Database'],
        suggestions=['College', 'University', 'Tuition', 
                    'International'],
        maxtags = 4,
        key='2')
