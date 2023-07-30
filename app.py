import streamlit as st



def main():
    """
    The main function of the ChatPDF Explorer app. Sets up the Streamlit page configuration, displays the app header
    and a text input for the user to ask questions about their documents, and provides a sidebar for the user to upload
    their PDF files and process them.
    """
    st.set_page_config(page_title="ChatPDF Explorer", page_icon=":books:")

    st.header("ChatPDF Explorer :books:")
    st.text_input("Ask a question about your documents:")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your PDF files", type=["pdf"])
        st.button("Process")


if __name__ == '__main__':
    main()
