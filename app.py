import streamlit as st

st.title('Hello')                                       # title

st.header('Welcome')                                    # Header

st.subheader('Objective:')                              # Subheader
st.text('streamlit usage')                              # Text

st.markdown('Features')                                 # Markdown

st.success('Success!')                                  # Success
st.info('Information!')                                 # Info
st.warning('Warning!')                                  # Warning
st.error('Error!')                                      # Error
st.exception(ZeroDivisionError('Div not possible'))     # Exception

st.subheader('Help')
st.help(ZeroDivisionError)                              # Help

st.subheader('Write')
st.write("range(1,10)")                                 # Write
st.write(range(1,10))
st.write(1*2*3)


st.subheader('Code')
st.code('x = 10\n'                                      # Code
        'for i in range(x):\n'
        '\tprint(i)')

#checkbox
st.subheader('Gender')

# Create checkboxes and store their states
male = st.checkbox('Male')
female = st.checkbox('Female')
others = st.checkbox('Others')

# Display message based on the selected checkboxes
if male:
    st.write('You are: male')
if female:
    st.write('You are: female')
if others:
    st.write('You opted others')


#radio button
st.subheader('Radio Button')                           
radioButton = st.radio('Select : ', ('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write("You're a Male")
elif(radioButton == 'Female'):
    st.write("You're a Female")
elif(radioButton == 'Other'):
    st.write("You're an Other Gender")

#select box
st.subheader('Select Box')                        
selectBox =  st.selectbox("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected : ", selectBox)

#multi select box
st.subheader('Select Box')                        
multiselectBox =  st.multiselect("Data Science : ", [  'Data Analsis', 'Web Scraping','Machine Learning',
                                                'Deep Learning','Natural Language Processing',
                                                'Computer Vision','Image Processing'])
st.write("You've selected : ", len(multiselectBox),'courses')

#button
button =  st.button('click me')
if button:
    st.write('thanks for clicking me')


#slider
vol= st.slider('select your Volume',0,100,step = 1)
st.write('Volume is : ',vol)

#text_input
st.subheader("Text Input")                             
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')

#text_area
st.subheader('Text area')
st.text_area('describe about yourself')

#number input
st.subheader('Number input')
st.number_input('select your age',18,35)

# Input-Date
st.subheader("Input Date")                            
st.date_input('Date')

# Input-Time
st.subheader("Input Time")                              
st.time_input('Time')




