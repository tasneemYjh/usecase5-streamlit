import streamlit as st

st.title('Job Postings in :green[Saudi Arabia]')


st.text('This is some text.')
st.image('https://example.com/your-image.jpg', caption='Your Image Caption', use_column_width=True)



def set_background(color):
    hex_color = f"#{color}"
    html_code = f"""
    <style>
    body {{
        background-color: {hex_color};
    }}
    </style>
    """
    st.markdown(html_code, unsafe_allow_html=True)

# Set background color
set_background("f0f0f0")

# Display content
st.title("Job Postings in Saudi Arabia")


#st.markdown("<h2 style='text-align: center; color: green;'>Job Postings in Saudi Arabia</h2>", unsafe_allow_html=True)

#st.title('Job Postings in :green[Saudi Arabia]')
st.text('This is some text.')
st.image('https://example.com/your-image.jpg', caption='Your Image Caption', use_column_width=True)


st.title('Job Postings in :green[Saudi Arabia]')
st.text('This is some text.')
st.image('https://example.com/your-image.jpg', caption='Your Image Caption', use_column_width=True)
