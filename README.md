# HEIC-To-JPG

A small Python program to convert all `.heic` files in a selected folder into `.jpg` images.  
This tool was created because online converters often limit the number of files you can convert at once.

Before running the script, you need to install the following library to handle HEIC files:

```bash
pip install pillow-heif
``` 

You can then execute the program this way : 

```bash
python "HEIC to JPG.py"
``` 

A file explorer window will open simply select the folder containing your .heic images.

The script will:
-  Automatically detect and convert all .heic files in the folder.

-  Create a subfolder called converted_jpg inside the selected folder.

-  Save all converted .jpg images into that subfolder with the same filenames.
