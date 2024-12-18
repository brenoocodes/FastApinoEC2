import boto3

def upload_file_to_s3(bucket_name, file_path, object_name=None):
    """
    Envia um arquivo para um bucket S3.

    :param bucket_name: Nome do bucket no S3.
    :param file_path: Caminho local do arquivo a ser enviado.
    :param object_name: Nome do objeto no S3 (se None, será o mesmo do arquivo local).
    :return: URL pública do arquivo.
    """
    # Inicializa o cliente S3
    s3 = boto3.client('s3')

    # Define o nome do objeto se não for especificado
    if object_name is None:
        object_name = file_path.split('/')[-1]

    try:
        # Realiza o upload do arquivo
        s3.upload_file(file_path, bucket_name, object_name)

        # Gera a URL pública do arquivo
        url = f"https://{bucket_name}.s3.amazonaws.com/{object_name}"
        print(f"Arquivo enviado com sucesso: {url}")
        return url
    except Exception as e:
        print(f"Erro ao enviar arquivo: {e}")
        raise


bucket_name = "brenocodesaprendizado"
file_path = "source/functions/licitanet.pdf"
upload_file_to_s3(bucket_name, file_path, object_name='brenocodes/documento.pdf')
