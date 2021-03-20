# help-nonprofit
*Human Evolution for Landscape Protection (HELP) WebSite*
## Development
    git clone https://github.com/adraxyz/help-nonprofit.git
### Requirements
    Python >= 3.8
    Pip >= 20.1.1
    python3-venv >= 3.8.6
    Postgres >= 12.5
    npm >= 6.14.8
### Database setup
    sudo -u postgres psql
    CREATE DATABASE <your_database_name>;
    CREATE USER <your_database_user> WITH PASSWORD '<your_database_password>';
    ALTER ROLE <your_database_user> SET client_encoding TO 'utf8';
    ALTER ROLE <your_database_user> SET default_transaction_isolation TO 'read committed';
    ALTER ROLE <your_database_user> SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE <your_database_name> TO <your_user>;
### Backend setup
#### Virtual environment
    python3 -m venv help_nonprofit
    . help_nonprofit/bin/activate
#### Requirements
    pip install -r help-nonprofit/backend/requirements.txt
#### Environment variables
    help-nonprofit/backend/backend/.env
#### Migrations
    python3 help-nonprofit/backend/manage.py makemigrations
    python3 help-nonprofit/backend/manage.py migrate
#### Backend static files
    python3 help-nonprofit/backend/manage.py collectstatic
#### Run backend server
    python3 manage.py runserver
Visit *localhost:8000* for APIs calls or the Django admin 
### Frontend setup
#### Packages installation
    cd help-nonprofit/frontend
    npm install
#### Environments variables
    help-nonprofit/frontend/.env
#### Run frontend server
    npm run dev
Visit *localhost:3000*

    

