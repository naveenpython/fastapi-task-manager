from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

#create fastapi
app = FastAPI()
#access path our website
@app.get('/')

def welcome():
    return {'messagre':'welcome to my website'}

@app.get('/about')
def about():
    return {"name":"naveen kumar","role":"backend engineer "}

@app.get('/project')
def project():
    return {"name":"task_management"}


@app.get('/student/{student_id}')
def get_student(student_id: int):
    return{
        "message":"student data mil gya !",
        "student_id_is":student_id,
        "name":"raj mehta" }

@app.get('/search')

def search_student(name:str,city:str="Gurugram",study:int=9):
    return{
        "message":"ye raha aapka search result",
        "search_name":name,
        "search city":city,
        "class":study

    }

#informed the fastapi
class Task(BaseModel):
    task_name:str
    status:str="Pending" #it is default value
# @app.post('/add-task')
# def create_task(new_task:Task):
#     return{
#         "message":"your task is successfully added ",
#         "received_data":new_task
#     }
def init_db():
    conn=sqlite3.connect("task_manager.db")
    cursor=conn.cursor()
    cursor.execute("""
            create table if not exists fastapi_tasks(
                id integer primary key autoincrement,
                task_name text,
                status text
                
                )

    """)
    conn.commit()
    conn.close()

init_db()#check the table

@app.post('/add_task')

def create_task(new_task:Task):
    conn = sqlite3.connect("task_manager.db")
    cursor=conn.cursor()

    #insert the data
    cursor.execute("insert into fastapi_tasks(task_name,status) values(?,?)",(new_task.task_name,new_task.status))
    conn.commit()
    conn.close()

    return{
        "message": f"{new_task.task_name} successfully add database"
    }
@app.get('/tasks')
def get_all_tasks():
    #connect the database
    conn=sqlite3.connect("task_manager.db")
    #convert the data in json file 
    conn.row_factory=sqlite3.Row
    cursor=conn.cursor()

    #select all data
    cursor.execute("select * from fastapi_tasks")
    all_task=cursor.fetchall()#fetch all data 

    conn.close()#close the database

    return{
        "all task":len(all_task),"list of task":all_task

    }

#put request using 
@app.put('/update-task/{task_id}')
def mark_task_done(task_id:int):
    conn=sqlite3.connect('task_manager.db')
    cursor=conn.cursor()
    cursor.execute("update fastapi_tasks set status = 'complate' where id= ?" ,(task_id,))
    conn.commit()
    conn.close()
    return {
        'message':f"your task is {task_id} successfully complate"
    }
# delete request 
@app.delete('/delete_task/{task_id}')
def delete_task(task_id:int):
    conn = sqlite3.connect('task_manager.db')
    cursor = conn.cursor()

    cursor.execute("delete from fastapi_tasks where id = ?",(task_id,))
    conn.commit()
    conn.close()
    return{"message":f"{task_id} is deleted from your databae"}