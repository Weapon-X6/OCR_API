from fastapi import FastAPI, File, UploadFile
from typing import List
import time
import asyncio
import app.ocr as ocr
import app.utils as utils


app = FastAPI()


@app.post("/api/v1/extract_text")
async def extract_text(Images: List[UploadFile] = File(...)):
    response = {}
    s = time.time()
    tasks = []

    for img in Images:
        img_path = str(utils.get_project_root()) + "/images/"
        print("Images uploaded: ", img.filename)
        temp_file = utils.save_file_to_server(
            img, path=img_path, save_as=img.filename)
        tasks.append(asyncio.create_task(
            ocr.read_image(temp_file)))

    text = await asyncio.gather(*tasks)

    for i in range(len(text)):
        response[Images[i].filename] = text[i]

    response["Time taken"] = round((time.time() - s), 2)

    return response
