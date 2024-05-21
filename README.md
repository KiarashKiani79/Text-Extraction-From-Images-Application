# Optical Character Recognition (OCR)
This project focuses on extracting structured text from images and enhancing it using OpenCV for more accurate results. The process involves downloading and installing Tesseract and other dependencies, loading the desired image, and using Tesseract to extract the text. The extracted text is then processed, especially for complex images, using OpenCV. Image processing operations include noise removal, threshold transformation, erosion, and drawing rectangles around specific patterns or characters. This automated Optical Character Recognition (OCR) method can be used by organizations to extract useful information from images and by individuals to save time and effort in typing. It eases the burden of document analysis and understanding. Let's get started with the project.

### Step to run application locally:
Step 1:	Create the copy of the project.
Step 2: Open command prompt and change your current path
to folder where you can find 'app.py' file.
Step 3: Create environment by command given below-
conda create --name <environment name>
Step 4: Activate environment by command as follows-
conda activate <environment name>
Step 5: Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki
Step 6: Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\ProgramFiles\Tesseract-OCR. It may change so please check the installation path.
Step 7: pytesseract.pytesseract.tesseract_cmd = r'C:\ProgramFiles\Tesseract-OCR\tesseract.exe'
Step 8: Use command below to install required dependencies-
python -m pip install -r requirements.txt
Step 9: Run application by command-
python app.py
You will get url copy it and paste in browser.

## Output of project
<img src="https://github.com/KiarashKiani79/Text-Extraction-From-Images-Application/blob/main/result_screenshots/Screenshot%202024-05-21%20205938.png"/>
<img src="https://github.com/KiarashKiani79/Text-Extraction-From-Images-Application/blob/main/result_screenshots/Screenshot%202024-05-21%20210015.png"/>
