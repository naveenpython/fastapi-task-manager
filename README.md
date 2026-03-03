# FastAPI Task Manager API 🚀

A robust, fully functional CRUD (Create, Read, Update, Delete) Backend API built with **FastAPI** and **SQLite**. This project allows users to manage their daily tasks efficiently.

## 🛠️ Tech Stack
* **Language:** Python
* **Framework:** FastAPI
* **Database:** SQLite3
* **Server:** Uvicorn

## ✨ Features
* **Add Task:** Create a new task and save it to the database.
* **View Tasks:** Fetch a list of all current tasks.
* **Update Task:** Mark a specific task as "Completed".
* **Delete Task:** Permanently remove a task from the database.
* **Interactive Docs:** Auto-generated Swagger UI for easy API testing.

## 🚀 API Endpoints

| HTTP Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/add-task` | Add a new task (Default status: Pending) |
| **GET** | `/tasks` | Retrieve all tasks from the database |
| **PUT** | `/update-task/{task_id}` | Mark a specific task as "Completed" |
| **DELETE** | `/delete-task/{task_id}`| Delete a specific task by its ID |

## ⚙️ How to Run Locally

Follow these steps to run this project on your local machine:

**1. Clone the repository:**
```bash
git clone https://github.com/naveenpython/fastapi-task-manager.git
