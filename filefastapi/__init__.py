from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
import boto3


app = FastAPI()


# Configurando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens. Troque "*" por uma lista de domínios confiáveis, se necessário.
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(router)


s3 = boto3.client('s3')
BUCKET_NAME = "brenocodesaprendizado"