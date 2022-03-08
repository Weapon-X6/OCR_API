import pytesseract
import asyncio


async def read_image(img_path, lang='eng'):
    try:
        text = pytesseract.image_to_string(img_path, lang=lang)
        await asyncio.sleep(2)
        return text
    except:
        return "File {0} couldn't be processed".format(img_path)
