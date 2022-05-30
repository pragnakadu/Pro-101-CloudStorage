import os
import dropbox
from dropbox.files import WriteMode

class TransferData :

        def __init__(self , access_token) :
                self.access_token = access_token

        def upload_files(self , file_from , file_to) :

                 dbx=dropbox.Dropbox(self.access_token)
                 for root, dirs , files in os.walk(file_from):

                                for filename in files:
                                        local_path = os.path.join(root , filename)
                                        relative_path = os.path.relpath(local_path , file_from)
                                        dropbox_path = os.path.join(file_to , relative_path)
                                        with open (local_path , 'rb') as f :
                                                dbx.files_upload(f.read() ,dropbox_path , mode = WriteMode('overwrite'))

def main():
                access_token = 'sl.BImMA0DCG9Z19L53_c3sGNyKSf0iCElrBLYWWlMi71-QqCWwFSqPRkY3euE3jfHOhd5rM4Wa4qHAvbq5MwLyHE6LqENCSl8FdZQUWsC750P5-ztoS9cXs8MQ8hU592yWpznyfCw'
                transferData = TransferData(access_token)
                file_from = str(input("Enter the file path to be uploaded to the dropBox: "))
                file_to = input("Enter the full path for the dropBox")

                transferData.upload_file(file_from, file_to)
                print("the file has been moved!!")

main()
