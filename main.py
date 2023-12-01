import PyPDF2
import openai
import streamlit as st
from io import BytesIO
# Change this line
import PyPDF2

# To this line
import fitz  # This is the PyMuPDF library


openai.api_key = "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"
TEMPLATE = """
Patient Information Template

1. Brief Patient Information
- Name: [Patient's Full Name]
- Date of Birth: [DOB]
- Gender: [Male/Female/Other]
- Address: [Patient's Address]
- Contact Number: [Patient's Phone Number]
- Emergency Contact: [Emergency Contact Name and Number]

2. History of Previous Illnesses
- Medical History:
  - [Previous illnesses, surgeries, or significant medical events]
  - [Dates and details of each event]

3. Diagnoses
- Chronic Conditions:
  - [List of chronic conditions diagnosed]
- Major Diagnoses:
  - [List of major diagnoses]
- Allergies:
  - [Known allergies and reactions]

4. Current Condition
- Presenting Complaint:
  - [Reason for the current visit]
- Symptoms:
  - [Detailed description of current symptoms]
- Medications:
  - [Current medications and dosages]
- Vitals:
  - Blood Pressure: [BP]
  - Heart Rate: [HR]
  - Respiratory Rate: [RR]
  - Temperature: [Temp]

5. Information About Relatives
- Next of Kin:
  - [Name and relationship of the patient's next of kin]
- Family Medical History:
  - [Any significant medical history among close family members]
"""


def chatgpt(text):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "YOUR NAME BETTER HEALTHCARE BOT",
            },
            {
                "role": "user",
                "content": text + "give me a medical summary. I diagnose accordingly." + TEMPLATE,
            },
        ],
    )
    return completion['choices'][0]['message']['content']

def read_pdf(pdf_file):
    text = ""
    # Change this line
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

# To this line
    pdf_document = fitz.open(pdf_file)



    return pdf_document

def main():
    st.title("PDF Reader App")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        # Read the PDF file
        pdf_text = read_pdf(uploaded_file)



        # Use GPT-3.5 to generate a response based on the extracted text



        response = chatgpt(pdf_text)
        st.markdown("# Summarization")
        st.text_area("Response:", value=response, height=300)


if __name__ == "__main__":
    main()
