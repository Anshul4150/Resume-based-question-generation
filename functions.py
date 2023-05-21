import streamlit as st
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import openai
#------- OCR ------------

@st.cache_data
def convert_pdf_to_txt_file(path):
    texts = []
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    # fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    file_pages = PDFPage.get_pages(path)
    nbPages = len(list(file_pages))
    for page in PDFPage.get_pages(path):
      interpreter.process_page(page)
      t = retstr.getvalue()
    # text = retstr.getvalue()

    # fp.close()
    device.close()
    retstr.close()
    return t, nbPages



  
@st.cache_data
def getresponse(text):
  jobs = 'job_roles.txt'
  openai.api_key = "" #insert api key
  prompt = f"You are an expert Computer science job interviewer(FAANG level), I will give 10 most demading jobs list and their requirement dont generate anything  , then I'll give the resume of the candidate to be interviewed .Compare the resume give your reviews about the candidate for the role and also give score of matching out of 10 (in new line) . For the most relevant job for the candidate . And generate 10 interview technical questons according to the role and the resume , also include 2 DSA coding question , medium dificulty question"

  with open(jobs,'r') as text_file :
    job_roles = text_file.read()
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      temperature = 0.2,
      max_tokens = 1000,
      messages = [
          {"role":"system","content":prompt},
          {"role":"user","content":job_roles},
          {"role":"user","content":text}
      ]

      

  )
  return (response['choices'][0]['message']['content'])
