import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self,file_to,file_from,local_path):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)

        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path,mode = dropbox.file.WriteMode.overwrite)

def main():
    access_token = "sl.BAZbUPWR_VG2onA-HZcPK0F4YkyM2La5P9uvD4Q7rEobSPkBCQ3IALru_9xLDzseKxxlwx4IKzJuGbirD6v1G7ER6LusuRP9C6TAPUh60HzChlwj9Ftvbm1SK6vPLUBB_Z4ni4Q"  
    transferData = TransferData(access_token)
    file_from = input("Enter the name of file to upload:-")
    file_to = input("Enter the full path of the file:-")

    transferData.upload_file(file_from,file_to)

main()    
