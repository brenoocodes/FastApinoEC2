from filefastapi import router, s3, BUCKET_NAME, app

from fastapi import APIRouter, File, UploadFile, Form, HTTPException
from botocore.exceptions import BotoCoreError
from starlette.responses import JSONResponse



@router.post("/upload")
async def upload_file(file: UploadFile = File(...), object_name: str = Form(None)):
    object_name = object_name or file.filename
    try:
        s3.upload_fileobj(file.file, BUCKET_NAME, object_name, ExtraArgs={"ContentType": "application/pdf"})
        url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{object_name}"
        return JSONResponse({"message": "Upload bem-sucedido", "url": url})
    except BotoCoreError as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)