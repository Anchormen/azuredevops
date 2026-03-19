# FastAPI app for Azure devops exercise
# Style errors have been included
import os
import socket
import uvicorn
from fastapi import FastAPI
def square(n):
    number = float(n)
    return 'Square of {} is {}'.format(number, number*number)
app = FastAPI()
# Use the following url to get the result replacing <IP> with the external IP, for example, http://20.76.191.125:8000
@app.get("/")
def hello_world():
    try:
        # to get the hostname
        host = socket.gethostname()
        # to get the host ip
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        host = "unkown"
        ip = "unknown"
    message = os.getenv("MESSAGE", "FastAPI Demo")
    return f"{message} on host {host} ({ip})"
# Use the following url to get the result replacing <IP> with the external IP, for example, http://20.76.191.125:5000/square_number?number=2
@app.get("/square_number")
def square_number(number: str):
    return square(number)
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        port=os.getenv("PORT", 8000),
        reload=True,
    )
