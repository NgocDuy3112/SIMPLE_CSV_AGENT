from helpers import *
    

def main():
    st.set_page_config(page_title="Hỏi đáp file CSV")
    st.header("Hỏi đáp file CSV 📈")
    csv_file = st.file_uploader("Tải một file CSV lên để trã lời câu hỏi", type="csv")
    if csv_file is not None:
        df = pd.read_csv(csv_file)
        llm = create_llm_from_ollama()
        PREFIX = """
        Answer the following question based only on the provided context. The answer must be written in Vietnamese:
        Question: {input}
        """
        agent = create_pandas_dataframe_agent(
            llm, 
            df, 
            verbose=True, 
            allow_dangerous_code=True, 
            prefix=PREFIX,
            handle_parsing_errors=True
        )

        user_question = st.text_input("Ask a question about your CSV: ")

        if user_question is not None and user_question != "":
            with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))


if __name__ == "__main__":
    main()