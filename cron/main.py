from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=30, wait_first=True)
def periodic():
    print("hi")