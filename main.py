import uvicorn
from fastapi import FastAPI, status

from router.user import user

app = FastAPI()
app.include_router(user)


###Home
@app.get(
    path='/',
    status_code=status.HTTP_200_OK,
    tags=['Home'],
    summary='Home')
def root():
    return


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
