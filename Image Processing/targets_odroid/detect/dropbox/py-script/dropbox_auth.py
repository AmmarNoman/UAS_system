import os, time
 
# Include the Dropbox SDK libraries
from dropbox import client, rest, session
 
# going to store the access info in this file
TOKENS = 'dropbox_token.txt'
 
# Get your app key and secret from the Dropbox developer website
APP_KEY = 'hhid9alxtnee5on'
APP_SECRET = 'crxlj3sautuoo4d'
ACCESS_TYPE = 'app_folder'
 
sess = session.DropboxSession(APP_KEY, APP_SECRET, ACCESS_TYPE)
 
request_token = sess.obtain_request_token()
 
url = sess.build_authorize_url(request_token)
 
# Make the user sign in and authorize this token
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
 
raw_input()
 
# This will fail if the user didn't visit the above URL and hit 'Allow'
access_token = sess.obtain_access_token(request_token)
 
# save the key to the file so you don't need to do this again
token_file = open(TOKENS,'w')
 
token_file.write("%s|%s" % (access_token.key,access_token.secret) )
 
token_file.close()
 
# just for reference, print out the account info that you are accessing with
print "linked account:", client.account_info()
