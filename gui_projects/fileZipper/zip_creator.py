import zipfile
import pathlib



def make_archive(filepaths, des_dir):
    des_dir = pathlib.Path(des_dir, "compressed.zip")
    with zipfile.ZipFile(des_dir ,'w') as myzip:        
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            myzip.write(filepath, arcname=filepath.name)
            
            
if __name__ == "__main__":
    make_archive()