import os, time, subprocess, sys
from dropbox import client, rest, session

file_source_path = "/home/odroid/detect/opencv-version/frame_with_target/"

## get list of files to upload
file_num = len(sys.argv)-1
if file_num > 0:
 
  TOKENS = '/home/odroid/detect/dropbox/py-script/dropbox_token.txt'
 
  # Get your app key and secret from the Dropbox developer website
  APP_KEY = 'hhid9alxtnee5on'
  APP_SECRET = 'crxlj3sautuoo4d' 
  ACCESS_TYPE = 'app_folder'
 
  # get the stored key from step one and use it
  token_file = open(TOKENS, 'r')
  token_key,token_secret = token_file.read().split('|')
  token_file.close()
 
  # init the session and the client
  sess = session.DropboxSession(APP_KEY,APP_SECRET, ACCESS_TYPE )
  sess.set_token(token_key,token_secret)

#  APP_ACCESS_TOKEN = 'k4QvXviokXAAAAAAAAABAPBADOBTKgo2d5Wvib_QJWNC2lwakMXNL7kcZoorYUkN' 
  client = client.DropboxClient(sess)


  if file_num == 1:
    f = open(file_source_path+sys.argv[1], 'r')
    res = client.put_file("/data/"+sys.argv[1], f)
    f.close() 
  else:
    os.chdir(file_source_path) 
    #subprocess.call(["rm", "data_batch.tar"])
    subprocess.call(["tar", "czf", "data_batch.tar"]+sys.argv[1:])
    f = open("data_batch.tar", 'r')
    res = client.put_file("/data/data_batch.tar", f)
    f.close()

  print res
