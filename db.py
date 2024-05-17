from tinydb import TinyDB, Query
db = TinyDB('db.json')


def get_all_todos():
    return db.all()

def get_todo(id):
    todo = db.get(doc_id=id)
    return todo

def add_todo(task):
    todo = {
        "task":task,
        "status":"pending"
    }
    new_id = db.insert(todo)
    return {**todo, "id":new_id}

def delete_todo(id):
    db.remove(doc_ids=[id])


def update_todo_status(id, status):
    todo = db.get(doc_id=id)
    todo["status"] = status
    db.update(todo, doc_ids=[id])
    return todo
    
def update_todo_task(id, task):
    todo = db.get(doc_id=id)
    todo["task"] = task
    db.update(todo, doc_ids=[id])
    return todo
    
# if len(getAlltodos() == 0):
#     addTodo("Learn Python")
#     addTodo("Learn FastAPI")
#     addTodo("Learn Django")
    



