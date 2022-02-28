import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import tweepy
from tweepy import OAuthHandler
import json
import re
import configparser
import detector


#To Hide Warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

STYLE = """
<style>
img {
    max-width: 100%;
}
</style> """


def main():

    html_temp = """
    <link href='https://fonts.googleapis.com/css2?family=Open+Sans:wght@800&display=swap' rel='stylesheet'>
	    <div style="background-color:#8C1515;">
            <p style="color:white;font-size:50px;padding:9px;text-transform:uppercase;font-family:Open Sans,sans-serif;;letter-spacing: 3px">
                <b>Phizon</b>
            </p>
        </div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)
    st.subheader("Don't be the victim!")
 
    from PIL import Image
    image = Image.open('phish.png')
    st.image(image,use_column_width=True)

    ################# Twitter API Connection #######################
    
    consumer_key = "kvSRXawYtSh32pknAZh7NRAFv"
    consumer_secret = "yEWEEnR5wqWUxUUUDT03N3uIpfDbdN5kgNOqXXQinWrqo2os2o"
    access_token = "3104698248-9cv98abLhM1GTSQFZNGTdpYDgjqpra8JY7XxWca"
    access_token_secret = "6na5TRSSNIck1smYecrygwSZBosbCW6yxkFxmHSyIvrEw"

    # Use the above credentials to authenticate the API.

    auth = tweepy.OAuthHandler( consumer_key , consumer_secret )
    auth.set_access_token( access_token , access_token_secret )
    api = tweepy.API(auth)
    ################################################################


    def prediction(url):
        dt = detector.Detector()
        result = dt.detect(url)
        return result 
    
    def image_check():
        st.subheader("Image")
        image_file = st.file_uploader("Upload Image", type=["png","jpg","jpeg"])
        if image_file is not None:
            file_details = {"filename":image_file.name, "filetype":image_file.type}
            st.write(file_details)
            st.image(image_file)
            my_bar = st.progress(100)


    def check_url():
        # Collect Input from user :
        url = str()
        url = str(st.text_input("Enter the URL you wish to identify (Press Enter once done)"))
        result = prediction(url)
        return result

    
    def get_tweets(Topic,Count):
                i=0
                df = pd.DataFrame(columns=["Date","User","IsVerified","Tweet","Likes","RT",'User_location'])
                my_bar = st.progress(100) # To track progress of Extracted tweets
                for tweet in tweepy.Cursor(api.search_tweets, q=Topic,count=50, lang="en",exclude='retweets').items():
                    #time.sleep(0.1)
                    #my_bar.progress(i)
                    df.loc[i,"Date"] = tweet.created_at
                    df.loc[i,"User"] = tweet.user.name
                    df.loc[i,"IsVerified"] = tweet.user.verified
                    df.loc[i,"Tweet"] = tweet.text
                    df.loc[i,"Likes"] = tweet.favorite_count
                    df.loc[i,"RT"] = tweet.retweet_count
                    df.loc[i,"User_location"] = tweet.user.location
                    i=i+1
                    if i>Count:
                        break
                    else:
                        pass
                return df

    def clean_tweet(tweet):
                regex=r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
                matches = re.findall(regex, tweet)
                while len(matches)>1:
                    matches.pop()
                if len(matches) == 0:
                  return 0
                else:
                    match = "{}".format(",".join(["'{}'".format(char) for char in matches]))
                    return match

    def fetch_tweet(api):
            # Write a Function to extract tweets:
            # Collect Input from user :
            Topic = str()
            Topic = str(st.text_input("(Press Enter once done)"))
            if len(Topic) > 0 :
                # Call the function to extract the data. pass the topic and filename you want the data to be stored in.
                with st.spinner("Please wait, Tweets are being extracted"):
                    df = get_tweets(Topic , Count=10)
                st.success('Tweets have been Extracted !!!!')
                    # Call function to get Clean tweets
                df['url'] = df['Tweet'].apply(lambda x : clean_tweet(x))
                df.drop(df.loc[df['url']==0].index,inplace=True)
                # See the Extracted Data : 
                if st.button("See the Extracted Data"):
                    #st.markdown(html_temp, unsafe_allow_html=True)
                    st.success("Below is the Extracted Data :")
                    st.write(df[['Tweet','url']])
                if st.button("Predict Results"):
                    st.write("Wait while we process..........")
                    df['phishing'] = df['url'].apply(lambda x : prediction(x))
                    st.write(df[['url','phishing']])
                        

    process_name = st.selectbox(
    'Select Operation',
    ('Select','Enter URL','Fetch Tweets','Image Check')
    )

    if process_name == 'Enter URL':
        result = check_url()
        if st.button("Predict Results"):
            st.write(result)
    if process_name == 'Fetch Tweets':
        st.write("Enter any topic to fetch random tweets and verify if they promote any malware activity through hyperlinks")
        fetch_tweet(api)               
    if process_name == 'Image Check':
        st.write("Upload any image of potential phishing website to verify if it is clone or not")
        image_check()

   
    
    #Sidebar
    st.sidebar.header("About App")
    st.sidebar.info("Lookout if you have been a victim of phishing attack or check before you become one.")
    
    st.sidebar.info("[Source Code](https://github.com/vidhigupta9/aws)")
    st.sidebar.header("Made by :")
    st.sidebar.info("[Vidhi Gupta](https://github.com/vidhigupta9)")
    st.sidebar.info("[Deep Rodge](https://github.com/deeprodge)")
    

if st.button("Exit"):
        st.balloons()


if __name__ == '__main__':
    main()
