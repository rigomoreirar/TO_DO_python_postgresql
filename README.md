# TO_DO_python_postgresql

Welcome to the Ultimate TO-DO App! 📝🚀

Because "I'll do it tomorrow" wasn't cutting it anymore 😅

Basically, this project pretends to be a template that displays how Hexagonal Architechture structure can be applied on different cases. Always following SOLID design.

---

## Features

- **Add Tasks:** Jot down your brilliant ideas... or your grocery list. We don't judge.
- **Delete Tasks:** Wave goodbye to those pesky tasks you never intend to do.
- **Update Tasks:** Change your mind? No problem. Flexibility is our middle name.
- **User Authentication:** Secure your tasks like a boss. Only you can see your to-dos (no snooping!).

---

## Tech Stack

- **Python:** Because who doesn't love a good script?
- **PostgreSQL:** For that reliable, non-judgmental database support.
- **Docker:** Containerize your frustrations away.

---

## Getting Started

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/TO_DO_python_postgresql.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd TO_DO_python_postgresql
    ```

3. **Set Up the Database:**
    ```bash
    docker compose -f docker-compose.postgresql_db.yml up -d
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Initialize the Database:**
    ```bash
    python infrastructure/persistence/init_db.py
    ```

6. **Run the Application:**
    ```bash
    python main.py
    ```

---

## Contributing

Feel free to fork the repo and submit pull requests! 😉

---

## License

This project is licensed under the MIT License. Because sharing is caring ❤️