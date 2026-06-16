import streamlit as st
import os
import sys

# Add project root to path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from src.extractor import extract_resume
from src.pdf_handler import extract_text_from_pdf
from src.database_handler import store_data_into_database
import json

st.set_page_config(page_title="Resume Extractor", layout="wide")
st.title("📄 Resume Information Extractor")
st.markdown("Upload your resume (PDF or TXT)")

uploaded_file = st.file_uploader("Choose file", type=["pdf", "txt"])

if uploaded_file is not None:
    temp_path = f"temp_{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    if uploaded_file.type == "application/pdf":
        text = extract_text_from_pdf(temp_path)
    else:
        text = uploaded_file.read().decode("utf-8")
    
    st.success("File processed successfully!")
    
    with st.spinner("Extracting data..."):
        result = extract_resume(text, uploaded_file.name)
    
        st.subheader("Contact Info")
        contact = result["contact"]

        st.write(f"**Name:** {contact.get('name') or 'Not found'}")
        st.write(f"**Email:** {contact.get('email') or 'Not found'}")
        st.write(f"**Phone:** {contact.get('phone') or 'Not found'}")
        
        st.subheader("Skills")
        st.write(", ".join(result.get("skills", [])) or "No skills found")
        
        # Education
        st.subheader("🎓 Education")
        for edu in result.get("education", []):
            if isinstance(edu, dict):
                display_text = edu.get('degree') or edu.get('institution') or str(edu)
            else:
                display_text = str(edu)
            st.write(f"• {display_text}")

            # Experience
            st.subheader("💼 Experience")
            for exp in result.get("experience", []):
                if isinstance(exp, dict):
                    display_text = exp.get('description') or exp.get('position') or str(exp)
                else:
                    display_text = str(exp)
                st.write(f"• {display_text}")

            # Certifications
            st.subheader("📜 Certifications")
            certs = result.get("certifications", [])
            if certs:
                for cert in certs:
                    st.write(f"• {cert}")
            else:
                st.write("No certifications found")
            
            json_str = json.dumps(result, indent=2)
           
        #store data into database
        st.download_button("Download JSON", json_str, "result.json", "application/json")
        if os.path.exists(temp_path):
            os.remove(temp_path)