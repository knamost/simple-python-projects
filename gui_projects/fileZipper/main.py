from zip_creator import make_archive
import FreeSimpleGUI as sg 

label1 = sg.Text("Select file to compress: ")
input1 = sg.Input()
button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select Destination folder")
input2 = sg.Input(key="folderpath")
button2 = sg.FolderBrowse("Choose", key="folderpath")

compress_button = sg.Button('Compress')
output_label = sg.Text(key="result_message", text_color="Blue")


window = sg.Window("File Compressor", 
                   layout=[
                       [label1, input1, button1],
                       [label2, input2, button2],
                       [compress_button, output_label]])

while True:
    event, values = window.read()
    
    filepath = values['files'].split(";")
    folder = values['folderpath']    
    
    if not filepath or not folder:
        sg.popup_error("Please select both a file and a destination folder.")
        continue
    
    make_archive(filepath, folder)
    window["result_message"].update(value="Compression completed!")
    
    if event in (sg.WIN_CLOSED, None):
        break

window.close()