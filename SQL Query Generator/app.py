import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY="AIzaSyBlTi1Cp-YVAsrGe0Vb6kUaSqTj_DlwPyw"

genai.configure(api_key=GOOGLE_API_KEY)
model=genai.GenerativeModel('gemini-pro')


def main():
   st.set_page_config(page_title="SQL Query Generator 🤖",page_icon=":robot:") 
   st.markdown(
      
      """
            <div style="text-align: center;">
            <h1>SQL Query Generator 🌐🛢🤖</h1>
            <h3>I can generate SQL queries for you!</h3>
            <h4>With Explainations as well!!</h4>
            <p>This is a simple tool that allows you to generate SQL queries based on your prompts.</p>

            </div>

""",
    unsafe_allow_html=True,
     
   )     

   text_input=st.text_area("Enter your Query here :")

  

   submit=st.button("Generate SQL Query")
   if submit:
        with st.spinner("Generating SQL Query..."):
            template="""
                Create a SQL query snippet using the below text:
                
                ...

                   {text_input}

                ...
                I just want a SQL query in appropriate form.

             """
            formatted_template=template.format(text_input=text_input)

            
            response=model.generate_content(formatted_template)
            sql_query=response.text
            sql_query=sql_query.strip().lstrip("```sql").rstrip("```")


            expected_output="""
                What would be the expected response of this SQL query snippet:
                
                   ...

                   {sql_query}

                   ...
                Provide sample tabular response with no explanation:

            """

            expected_output_formatted=expected_output.format(sql_query=sql_query)
            expectedOutput=model.generate_content(expected_output_formatted)
            expectedOutput=expectedOutput.text
            


            explaination="""
                Explain this Sql query:
                
                   ...

                   {sql_query}

                   ...
                Please provide with simplest of explaination in points format:

                 """
            explaination_formatted=explaination.format(sql_query=sql_query)
            explaination=model.generate_content(explaination_formatted)   
            explaination=explaination.text
            

            with st.container():
                st.success("SQL Query Generated Successfully!Here is your Query Below:")
                st.code(sql_query,language="sql")

                st.success("Expected Output of this SQL query will be:")
                st.markdown(expectedOutput)

                st.success("Explaination  of this SQL query :")
                st.markdown(explaination)

main()  