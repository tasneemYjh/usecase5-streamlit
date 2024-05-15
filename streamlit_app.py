import streamlit as st


st.image('image1.jpeg')
st.title('Job Postings in :green[Saudi Arabia]')

st.markdown("""
In recent years, Saudi Arabia has seen significant growth in job opportunities across various sectors.
This analysis aims to provide insights into job postings in Saudi Arabia, highlighting key trends and patterns in the job market.
""")





st.header("( Riyadh has most job postings )")


st.markdown("""
The chart illustrates the distribution of job postings across various regions within Saudi Arabia.
It is evident that Riyadh leads significantly, accounting for the highest number of job postings compared to other regions.
""")
st.image('q2.png', caption='Riyadh has most job postings', use_column_width=True)





#st.header("Job Postings in Saudi Arabia", level=2)
st.markdown("""this chart shows that gender equality in employment opportunities across the kingdom.
Both male and female candidates have an equal number of job postings, highlighting a balanced approach to hiring.
""")
st.image('q1.png', caption='Equal job postings for all genders.', use_column_width=True)


#st.title('Job Postings in :green[Saudi Arabia]')
st.markdown("""this chart shows that Fresh graduates have a higher number of job postings, indicating a demand for new talent in the job market.
""")
st.image('q3.png', caption='More job postings target fresh graduates.', use_column_width=True)


st.markdown("""this chart shows that Job postings commonly feature a salary range between 4000 and 7000 for fresh graduates, indicating a competitive entry-level pay scale across various industries.""")
st.image('q4.png', caption='salary range for fresh graduates.', use_column_width=True)


st.markdown("""The chart clearly demonstrates a substantial preference for full-time employment contracts over remote work agreements.
""")
st.image('q5.png', caption='Full-time contracts greatly outnumber remote.', use_column_width=True)



