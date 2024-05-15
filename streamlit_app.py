import streamlit as st


st.image('image1.jpeg')
st.title('Job Postings in :green[Saudi Arabia]')

st.markdown("""
In recent years, Saudi Arabia has seen significant growth in job opportunities across various sectors.
This analysis aims to provide insights into job postings in Saudi Arabia, highlighting key trends and patterns in the job market.
""")





st.header("Riyadh has most job postings", level=2)

st.markdown("""
The chart illustrates the distribution of job postings across various regions within Saudi Arabia.
It is evident that Riyadh leads significantly, accounting for the highest number of job postings compared to other regions.
""")
st.image('q2.png', caption='Riyadh has most job postings', use_column_width=True)





st.header("Job Postings in Saudi Arabia", level=2)
st.markdown("<h2 style='text-align: center; color: green;'>Job Postings in Saudi Arabia</h2>", unsafe_allow_html=True)
st.image('https://example.com/your-image.jpg', caption='Your Image Caption', use_column_width=True)


st.title('Job Postings in :green[Saudi Arabia]')
st.text('This is some text.')
st.image('https://example.com/your-image.jpg', caption='Your Image Caption', use_column_width=True)
