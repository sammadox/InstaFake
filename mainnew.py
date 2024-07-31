import streamlit as st
import time
import pandas as pd
import altair as alt
from scraper import run_actor_with_cookies
import json

# Load JSON data from file
with open('aabbdd139_results.json', 'r') as file:
    json_data = json.load(file)


# Initialize the transformed data dictionary
data = {
    'ID': [],
    'name': [],
    'followers': [],
    'following': [],
    'post_count': []
}

# Transform the JSON data
for entry in json_data:
    data['ID'].append(entry['ID'])
    data['name'].append(entry['name'])
    data['followers'].append(int(entry['followers'].split('\n')[0].replace(',', '')))
    data['following'].append(int(entry['following'].split('\n')[0].replace(',', '')))
    data['post_count'].append(int(entry['post_count'].split('\n')[0].replace(',', '')))



df = pd.DataFrame(data)

# Calculate followers-to-following ratio
df['followers_to_following_ratio'] = df['followers'] / df['following']

# Title of the app
st.title("Instagram Fake Followers Detection")

# Text box input
input_text = st.text_input("Enter some text:")

# Button
if st.button("Submit"):
    # Show loading message for 10 seconds
    with st.spinner('Loading...'):
        #run_actor_with_cookies(input_text)
        time.sleep(10)
    
    # Display the CSV table
    st.write("Here is the CSV table:")
    st.dataframe(df)
    
    # Visualize the followers
    st.write("Followers")
    followers_chart = alt.Chart(df).mark_bar().encode(
        x='ID',
        y='followers'
    ).properties(width=600, height=300)
    st.altair_chart(followers_chart, use_container_width=True)
    
    # Visualize the following
    st.write("Following")
    following_chart = alt.Chart(df).mark_bar().encode(
        x='ID',
        y='following'
    ).properties(width=600, height=300)
    st.altair_chart(following_chart, use_container_width=True)
    
    # Visualize the post count
    st.write("Post Count")
    post_count_chart = alt.Chart(df).mark_bar().encode(
        x='ID',
        y='post_count'
    ).properties(width=600, height=300)
    st.altair_chart(post_count_chart, use_container_width=True)

    # Visualize followers-to-following ratio
    st.write("Followers-to-Following Ratio")
    ratio_chart = alt.Chart(df).mark_bar().encode(
        x='ID',
        y='followers_to_following_ratio'
    ).properties(width=600, height=300)
    st.altair_chart(ratio_chart, use_container_width=True)
