import streamlit as st
from PyPDF2 import PdfMerger
import os

st.set_page_config(layout="wide", page_icon="📑", page_title="MesclaPDFs")

def merge_pdfs(pdf_list, output_path):
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output_path)
    merger.close()

def main():
    st.title("Mesclar PDFs")

    uploaded_files = st.file_uploader("Selecione os arquivos PDF, ou arraste e solte aqui", type="pdf", accept_multiple_files=True)

    if uploaded_files:
        if st.button("Combinar PDFs"):
            with st.spinner("Combinando PDFs..."):
                output_path = "merged_output.pdf"
                merge_pdfs(uploaded_files, output_path)
                st.success("PDFs combinados com sucesso!")

                with open(output_path, "rb") as f:
                    st.download_button(
                        label="Baixar PDF combinado",
                        data=f,
                        file_name="merged_output.pdf",
                        mime="application/pdf"
                    )

                # Remover o arquivo temporário após o download
                os.remove(output_path)

if __name__ == "__main__":
    main()
