# Back-end API for WorkTeams


## Setup

- Clone the repository

  ```bash
  git clone https://github.com/Build-WorkTeams/Backend-API.git
  cd Backend-API
  ```

- Create a new environment and activate it.
  
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

- Install all package requirements

  ```bash
  pip install -r requirements.txt
  ```

- Move into the source code directory
  ```bash
  cd src
  ```

- Run migrations and database setups
  ```bash
  python manage.py migrate
  ```

- Run the server locally

  ```bash
  python manage.py runserver
  ```
  
