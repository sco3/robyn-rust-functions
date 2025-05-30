#!/usr/bin/env -S uv run 
import time
from robyn import Robyn

from fib import fibonacci as fib2

from hello_world import say_hello

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


app = Robyn(__file__)

@app.get("/hello")
async def hello(request):
    return "hello"

@app.get("/hello2")
async def hello(request):
    sh = say_hello()
    print ("> ", sh)
    return sh

@app.get("/fib/:n")
async def fib_endpoint(request, path_params):
    start  = time.monotonic()
    n = int(path_params["n"])
    print (n)
    r = fib(n)
    took  = time.monotonic()-start
    return {"result":r,"took":took}

@app.get("/fib2/:n")
async def fib_endpoint2(request, path_params):
    start  = time.monotonic()
    n = int(path_params["n"])
    print (n)
    r = fib2(n)
    took  = time.monotonic()-start
    return {"result":r,"took":took}

app.start(port=8080)
