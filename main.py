from fastapi import FastAPI
from fastapi import Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form

app = FastAPI()
templates = Jinja2Templates(directory='templates')
from db import get_all_todos, add_todo, delete_todo, get_todo, update_todo_task, update_todo_status

@app.on_event("startup")
async def startup_event():
    if(len(get_all_todos()) == 0):
        add_todo("Learn Python")
        add_todo("Learn FastAPI")
    
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    context = {
        "request":request,
        "title":"home",
        "todolist": get_all_todos()
    }
    
    print(get_all_todos())
    
    response = templates.TemplateResponse("home.html", context)
    return response

@app.get("/todos", response_class=HTMLResponse)
def home(request: Request):
    context = {
        "request":request  
    }
    response = templates.TemplateResponse("todolist.html", context)
    return response


@app.post("/add", response_class=HTMLResponse)
def add(request: Request, task: str = Form(...)):
    print("here...")
    print(task)
    newtodo = add_todo(task)
    context = {
        "request": request,
        "todo": newtodo
    }
    return templates.TemplateResponse("todoitem.html", context=context)

@app.delete('/delete/{item_id}', response_class=Response)
def delete(item_id: int):
    delete_todo(item_id)
    return Response(content="", media_type="text/html")


@app.get("/edit/{item_id}", response_class=HTMLResponse)
def get_edit(request: Request, item_id: int):
    todo = get_todo(item_id)
    context = {"request": request, "todo": todo}
    return templates.TemplateResponse("edititem.html", context)


@app.put("/edit/{item_id}", response_class=HTMLResponse)
def put_edit(request: Request, item_id: int, task: str = Form(...)):
    todo = update_todo_task(item_id, task)
    context = {"request": request, "todo": todo}
    return templates.TemplateResponse("todoitem.html", context)


@app.patch("/status/{item_id}/{status}", response_class=HTMLResponse)
def put_status(request: Request, item_id: int, status: str):
    todo = update_todo_status(item_id, status)
    context = {"request": request, "todo": todo}
    return templates.TemplateResponse("todoitem.html", context)

