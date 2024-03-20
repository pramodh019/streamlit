import streamlit as st

#Uploading
st.subheader('uploading a FILE')
file= st.file_uploader('Upload the CSV file:',type=['csv','xlsx'])

#Displaying
st.table(file)

#Another way
if file is not None:
    st.dataframe(file)

#Dealing with Images directly
st.subheader('Dealing with Images')
st.image(r"C:\Users\pramo\Desktop\jupyter project\Streamlit\spiderman.png.jpg") 


#Dealing with Images while uploading
st.subheader('uploading a Image')
img_file= st.file_uploader('Upload the image:',type=['png','jpeg'])
if file is not None:
    st.image(img_file)


#working with videos
st.subheader('Working with Videos')
video_file = st.file_uploader("Upload the Video file : ", type = ['mkv', 'mp4'])
if video_file is not None:
    st.video(video_file, start_time = 0)

#working with audio
st.subheader('Working with Audio')
audio_file = st.file_uploader("Upload the audio file : ", type = ['mp3', 'wav'])
if audio_file is not None:
    st.audio(audio_file.read())