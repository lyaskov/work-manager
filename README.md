# WorkManager - Task Management System

WorkManager is a Django-based task management application designed for IT teams.  
It helps developers, designers, project managers, and QA specialists **create, assign, track, and manage tasks efficiently**.

## Features
- ✅ **User Authentication**: Secure login and profile management.
- ✅ **Task Management**: Create, edit, and delete tasks.
- ✅ **Task Assignment**: Assign tasks to specific team members.
- ✅ **Task Status Tracking**: Mark tasks as completed or active.
- ✅ **Task Prioritization**: Set task priority levels (Urgent, High, Medium, Low).
- ✅ **Pagination & Filtering**: Easily navigate and filter tasks.
- ✅ **Dashboard**: View statistics on completed and active tasks.
- ✅ **Profile Editing** – Users can edit their personal information.

## Technologies Used

| Technology      | Description |
|----------------|-------------|
| **Django**     | A high-level Python web framework for rapid development and clean, pragmatic design. |
| **SQLite**     | Default database used for development (can be switched to PostgreSQL or MySQL for production). |
| **Bootstrap**  | Optional frontend styling framework for responsive and modern UI components. |
| **Django Auth**| Built-in Django authentication system for user login, registration, and session management. |


## 🔧 Installation Guide  

Python3 must be already installed

```shell
git clone https://github.com/lyaskov/work-manager.git
cd work-manager
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Rename .env-sample to .env and fill in the required settings.

### **Apply Migrations & Create Superuser**

```shell
python manage.py migrate
python manage.py createsuperuser
```

### **Run the Development Server**

```shell
python manage.py runserver
```

### **Open the Application in Browser**

🔗 **Local Development Server:**

```
http://localhost:8000/
```

---

## Live Demo

 **Try the live demo:** [WorkManager on Render](https://work-manager-mtev.onrender.com/)

### **Demo Screenshot**
![Website Interface](Demo.png)



### **Demo Credentials**

#### **Regular User**

- **Username:** `worker`
- **Password:** `user34Ffd`

#### **Admin User**

- **Username:** `admin`
- **Password:** `sup197Pass`

## License

This project is licensed under the **MIT License**.