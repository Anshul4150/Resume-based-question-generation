import streamlit as st
from PIL import Image

from functions import convert_pdf_to_txt_file,getresponse


st.set_page_config(page_title="Resume based queston generation")


html_temp = """
            <div style="background-color:{};padding:1px">
            
            </div>
            """

# st.markdown("""
#     ## :outbox_tray: Text data extractor: PDF to Text
    
# """)
# st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
st.markdown("""
    ## RESUME BASED QUESTION GENERATION
""")


pdf_file = st.file_uploader("Load your PDF", type=['pdf'])
hide="""
<style>
footer{
	visibility: hidden;
    	position: relative;
}
.viewerBadge_container__1QSob{
  	visibility: hidden;
}
#MainMenu{
	visibility: hidden;
}
<style>
"""
st.markdown(hide, unsafe_allow_html=True)
if pdf_file:
    path = pdf_file.read()
    file_extension = pdf_file.name.split(".")[-1]
    if file_extension == "pdf":
        text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
        st.text(getresponse(text_data_f))
    


  
