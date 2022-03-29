# OCR_API
An implementation of FastAPI and Pytesseract to build an OCR (Optical Character Recognition) API.

### Features

- Currently the only endpoint receives one or several images per POST call and outputs the text (if any) within each of them

- Only works for the english language

### Installation

First, download and install the Tesseract engine per the official [repo](https://github.com/tesseract-ocr/tesseract)

Then execute the following inside this repository to install all the dependencies for the project using:
```
$ pip install -r requirements.txt
```

Finally, execute the server inside root folder with
```
$ uvicorn app.main:app --reload
```
