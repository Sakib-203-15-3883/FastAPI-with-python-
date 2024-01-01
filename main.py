from fastapi import FastAPI
app = FastAPI()

@app.get("/")

async def root():
  return [1,2]


# define an api route 

@app.get("/post") 

# Define Route Handler Function

async def get_posts():
  return {"image","it,s an image "}