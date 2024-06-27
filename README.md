# Please read this file first before running API!

#### 1. Install DjVuLibre library on your PC

    DjVuLibre-3.5.28_DjView-4.12_Setup.exe

#### 2. Add your DjVuLibre path to Environment Path and restart your PC

    run "ddjvu" command on your command prompt window and ensure that there's no error

#### 3. On your VS Code terminal, install necessary python linraries

    run "pip install Pillow img2pdf fastapi uvicorn"

#### 4. Run your FAST API app to receive requests!

    run "uvicorn app:app --reload"

#### 5. Send apis on your postman to convert djvu to pdf

    Method: POST

    API: http://localhost:8000/convert/

    Select "Body" tab, choose "form-data" option and add following parameters!

##### 
    Mandantory

    input_path: YOUR_DJVU_FILE_FULL_PATH (E:\Python\CD5523005522 - CD5523005522-231104-YOUSUF MACHINES & STRUCTURALS1 (1).djvu)

    output_path: YOUR_PDF_FILE_FULL_PATH (E:\Python\output.pdf)

##### 
    Optional

    jpeg_quality: IMAGE_QUALITY (Must be a number between 1 ~ 100, default 90)

    scale: SCALE_RATIO (Must be a number between 1 ~ 999, default 120)
