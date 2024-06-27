from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from pydantic import BaseModel, Field, validator
import shutil
import os
import subprocess
import img2pdf
from PIL import Image

app = FastAPI()

def convert_djvu_to_pdf(input_file, output_file, jpeg_quality=75, scale=50):
    # Create a temporary directory to store images
    temp_dir = "temp_images"
    os.makedirs(temp_dir, exist_ok=True)

    # Use ddjvu to convert DJVU to images
    subprocess.run(["ddjvu", f"--scale={scale}", input_file, f"{temp_dir}/page_%04d.tiff"])

    # Convert each TIFF image to grayscale JPEG to reduce size
    images = []
    for image_file in sorted(os.listdir(temp_dir)):
        if image_file.endswith(".tiff"):
            tiff_path = os.path.join(temp_dir, image_file)
            jpg_path = tiff_path.replace(".tiff", ".jpg")

            # Convert TIFF to grayscale JPEG with the specified quality
            img = Image.open(tiff_path)
            img = img.convert("RGB")  # Convert to RGB for JPEG compatibility
            img.save(jpg_path, "JPEG", quality=jpeg_quality)
            images.append(jpg_path)

    # Convert images to PDF using img2pdf
    with open(output_file, "wb") as f:
        f.write(img2pdf.convert(images))

    # Clean up temporary image files and directory
    shutil.rmtree(temp_dir)

@app.post("/convert/")
async def convert_djvu_to_pdf_api(
    input_path: str = Form(...),
    output_path: str = Form(...),
    jpeg_quality: int = Form(90),
    scale: int = Form(120)
):
    # Perform conversion
    try:
        convert_djvu_to_pdf(input_path, output_path, jpeg_quality, scale)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))  # Return 400 Bad Request with error message

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion failed: {str(e)}")  # Return 500 Internal Server Error for other exceptions

    return {"message": f"Conversion successful. PDF saved at {output_path}"}