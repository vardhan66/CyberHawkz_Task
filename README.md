# SalesData
## Setup Instructions

### Prerequisites

- Python 3.12.1+
- PostgreSQL
- Redis

### Installation

1. Clone the repository:

    git clone <repository-url>
    cd SalesData


2. Create and activate a virtual environment:

  
    python -m venv venv
    source venv/bin/activate  


3. Install dependencies:


    pip install -r requirements.txt


4. Configure the database in `SalesData/settings.py`.

5. Run the migrations:


    python manage.py makemigrations
    python manage.py migrate


6. Add dummy data:


    python manage.py dummy_data


7. Run Redis server:

    
    redis-server
 If You're using WSL :
    sudo apt-get install redis
    sudo service redis-server start
To check the server is running:
    redis-cli ping
  

8. Start the Django development server:

   
    python manage.py runserver


9. Access the application at `http://127.0.0.1:8000/sales-chart/`.