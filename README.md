![image](https://github.com/user-attachments/assets/e012c32d-4bcb-4c9c-87d3-bf60ce8f3c0d)
 SafeVolt - File Protection Tool
Welcome to SafeGuard Backup, a sleek and elegant solution to automate and monitor your file backups with ease! This project combines a powerful Flask backend with a React-based frontend to ensure your data is safe and sound. 🌟

🚀 Overview
SafeGuard Backup is designed to help you:

📤 Upload and schedule backups for your important files.
📊 Monitor backup statuses in real-time with a stunning dashboard.
🔄 Automatically retry failed backups up to 3 times for reliability.


Built with modern web technologies, this tool is perfect for personal use, developers, or small businesses looking to safeguard their data effortlessly.

🎨 Features

File Upload: Easily upload files with a simple and elegant interface.
Real-Time Dashboard: View task details (ID, File Path, Backup Name, Status, Retries, Created At) with auto-refresh.
Retry Mechanism: Ensures robustness with up to 3 retry attempts on failures.
Motivational Quotes: Get inspired with random quotes on each visit.
Responsive Design: A visually appealing UI that works on any device.


🛠️ Tech Stack

Backend: Flask, SQLAlchemy (SQLite), Python
Frontend: React, Tailwind CSS
Database: SQLite for task management
Other: HTML, JavaScript, Babel


📦 Installation
Prerequisites

Python 3.x
Node.js (optional, for static serving)

Steps

Clone the Repository
git clone <your-repo-url>
cd safeguard-backup


Set Up Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux


Install Dependencies
pip install flask sqlalchemy flask-cors


Prepare Folders

Create uploads and backups folders in the project root:mkdir uploads backups




Run the Application

Start the Flask backend:python app.py


Start the worker in a separate terminal:python worker.py


Open your browser and go to http://127.0.0.1:5000.




🎮 Usage

Upload a File:

Visit http://127.0.0.1:5000.
Enter a file and a backup name, then click "Upload".


Monitor Status:

The dashboard will display all tasks with their current status (Pending, Completed, Failed).


Enjoy the Experience:

Watch for a new inspirational quote each time you load the page!




🌟 Contributing
We welcome contributions! Feel free to:

Report bugs or suggest features via issues.
Submit pull requests with improvements.

Please follow the Contributor Guidelines (create one if needed).

⚠️ License
This project is licensed under the MIT License. See the LICENSE file for details (create one if needed).

🙌 Acknowledgments

Inspired by the need for simple yet effective backup solutions.
Built with love using open-source tools and libraries.


Happy safeguarding your data with SafeGuard Backup! 🚀 Let’s keep your files secure and your mind at peace! 🌈
