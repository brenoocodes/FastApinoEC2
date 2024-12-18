from filefastapi import router, s3, BUCKET_NAME, app
from fastapi import HTTPException, Query
from starlette.responses import JSONResponse

@router.get("/get-url")
async def get_file_url(bucket: str = Query(...)):
    object_name = bucket
    if not object_name:
        raise HTTPException(status_code=400, detail="O campo 'name' é obrigatório.")
    
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=object_name)
        public_url = f"https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{object_name}"
        return JSONResponse({"message": "URL pública gerada com sucesso", "url": public_url})
    except s3.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            raise HTTPException(status_code=404, detail="Arquivo não encontrado.")
        raise HTTPException(status_code=500, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro inesperado: " + str(e))

app.include_router(router)
