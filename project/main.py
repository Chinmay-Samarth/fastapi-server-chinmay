
import uvicorn

if __name__ == '__main__':
    uvicorn.run("hello:app", host="0.0.0.0", port=0000, reload=True)