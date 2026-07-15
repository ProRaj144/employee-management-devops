from fastapi import APIRouter, UploadFile, File, HTTPException
from app.s3 import upload_file, list_files, delete_file

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        file_url = upload_file(file.file, file.filename)

        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "url": file_url
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/files")
def get_files():
    try:
        return list_files()

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/files/{filename}")
def remove_file(filename: str):
    try:
        delete_file(filename)

        return {
            "message": f"{filename} deleted successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
