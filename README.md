# InstaDataCom - File Sharing Web App

## 🧩 Problem Statement

In educational environments, especially classrooms, teachers often face difficulty sharing files like assignments, notes, or resources with students in a quick and organized way. Traditionally, this is done via email or messaging apps like WhatsApp, which can be inefficient, lead to missed files, or lack centralized access.

**InstaDataCom** addresses this by offering a simple, centralized file sharing platform. Teachers can upload any type of document, and all students who are logged in (either via email/password or Google) can view, download, and access those files from anywhere, on any device — be it a PC, Android phone, or iOS device. It eliminates the need for repeated messages or individual file sharing and ensures every student gets access at the same time with minimal effort.

This solution is ideal for:
- Teachers sharing lecture materials, notes, and assignments
- Students accessing study resources from a single dashboard
- File access and download without needing to use third-party apps

InstaDataCom is a Django-based web application for uploading, viewing, downloading, and deleting files using Supabase Storage. Users can sign up or log in via email/password or Google OAuth. All uploaded files are accessible to every logged-in user, making it ideal for collaborative environments.

🚀 Features
📤 Upload files (CSV, PDF, TXT, Excel, and more)

🔓 Files stored in a public Supabase bucket with accessible download URLs

👤 User authentication via:

Email & password

Google OAuth 2.0

📥 Download files in their original format

🗑️ Delete files from both Supabase and Django DB

🔍 Search files by title from the dashboard

📊 Responsive dashboard with a file list

🌐 Fully deployed on Vercel (https://instadatacom.vercel.app/)

📱 Mobile-compatible: Android and iOS supported via browser

## 🧱 Tech Stack

- Backend: Django (Python)
- Authentication: Google OAuth 2.0
- Database: Supabase (PostgreSQL + Storage)
- Frontend: HTML5, CSS3, Bootstrap
- Hosting: Vercel

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/Sujalmansuri/InstaDataCom---File-Sharing-Web-App
cd instadatacom

2. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Set Up Environment Variables
Create a .env file in the root directory and add:

SUPABASE_URL=your-supabase-url
SUPABASE_API_KEY=your-supabase-api-key
SUPABASE_PROJECT_ID=your-project-id
Add your Google OAuth client credentials to settings.py:

GOOGLE_CREDENTIALS = {
  "web": {
    "client_id": "...",
    "project_id": "...",
    ...
  }
}
4. Run Migrations and Start Server
python manage.py migrate
python manage.py runserver

🚀 Deployment
Connect your GitHub repo to Vercel

Set environment variables in the Vercel dashboard

Deploy and go live!

📝 Models
User_Data
email

full_name

password (hashed)

is_google_user

UploadedFile
title

public_url

path_in_bucket

user_email

uploaded_at

🤝 Contributing
PRs are welcome. Feel free to fork and submit improvements or bug fixes.
Devloped By:- Sujal Mansuri

Next time you want to share any file make sure you use this web app.
