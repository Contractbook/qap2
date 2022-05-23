import uvicorn
from buffer import Buffer

from os import environ

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
from starlette.middleware.cors import CORSMiddleware

from models import LoadRequest, CheckRequest, CheckResponse
from utils import send_greeting_on_slack


MAX_LENGTH = 200

app = FastAPI()
app.add_middleware(
    CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*']
)

api_key_header = APIKeyHeader(name='api-key')


def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key != environ['API_KEY']:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )


@app.post(f"/load")
def check(payload: LoadRequest, _: None = Depends(verify_api_key)):
    if len(payload.chunk) > MAX_LENGTH:
        raise HTTPException(400, {"reason": f"Chunk cannot be longer than {MAX_LENGTH}"})
    if len(Buffer.data) + len(payload.chunk) > 1024 * 1024:
        raise HTTPException(400, {"reason": "Chunk would overload the buffer"})
    Buffer.load(payload.chunk)


@app.post(f"/check", response_model=CheckResponse)
def load(payload: CheckRequest, _: None = Depends(verify_api_key)):
    if len(Buffer.data) == 0:
        raise HTTPException(400, {"reason": "Buffer is empty"})
    if len(payload.pattern) == 0:
        raise HTTPException(400, {"reason": "Pattern cannot be empty"})
    if len(payload.pattern) > MAX_LENGTH:
        raise HTTPException(413, {"reason": f"Pattern cannot be longer than {MAX_LENGTH}"})
    pattern_index = 0
    exists = False
    for number in Buffer.data:
        if number == payload.pattern[pattern_index] or payload.pattern[pattern_index] is None:
            pattern_index += 1
            if pattern_index == len(payload.pattern):
                exists = True
                break
        else:
            pattern_index = 0
    # Buffer.clear()
    return CheckResponse(exists=exists)


@app.get(f"/debug/buffer")
def show(_: None = Depends(verify_api_key)):
    return Buffer.data


@app.delete(f"/debug/buffer")
def show(_: None = Depends(verify_api_key)):
    Buffer.clear()
    return Buffer.data


send_greeting_on_slack()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9990)
