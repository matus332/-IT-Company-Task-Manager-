# IT Company Task Manager

Django web application for managing workers, positions, task types and tasks inside an IT company.

## Features

- User authentication: login and logout
- Custom user model: Worker
- CRUD for workers
- CRUD for tasks
- CRUD for positions
- CRUD for task types
- Task assignment to workers
- Task priority management
- Task deadline validation
- Overdue task detection
- Search functionality
- Pagination
- Django admin panel
- Form validation
- Automated tests

## Technologies

- Python
- Django
- SQLite
- HTML
- CSS
- Bootstrap
- Crispy Forms

## Database structure

Main models:

- Position
- Worker
- TaskType
- Task

Relations:

- One Position can have many Workers
- One TaskType can have many Tasks
- One Task can have many Workers
- One Worker can have many Tasks

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd IT_Company_Task_Manager
