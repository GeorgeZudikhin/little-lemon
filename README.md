# Little Lemon 

## About the Project

Little Lemon is a Django-based web application for restaurant management. It includes features like booking tables and viewing the restaurant menu.

## Getting Started

### Prerequisites
- Python 3
- pip
- MySQL

### Setting Up the Environment

1. **Clone the Repository**
   - Clone the project using:
     ```bash
     git clone https://github.com/GeorgeZudikhin/little-lemon
     ```

2. **Set Up a Virtual Environment**
   - Create and activate a virtual environment:
     ```bash
     python3 -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**
   - Install the required packages:
     ```bash
     pip3 install -r requirements.txt
     ```

4. **Set Up MySQL**
   - Ensure MySQL is installed and running.
   - Create a new database for the project.

5. **Run Migrations**
   - Apply database migrations:
     ```bash
     python manage.py migrate
     ```

6. **Create a Superuser (optional)**
   - Create a Django superuser:
     ```bash
     python manage.py createsuperuser
     ```

7. **Start the Server on Port 8000**
   - Run the Django development server:
     ```bash
     python manage.py runserver
     ```

   
## API Routes

### Admin Routes
- `admin/` - Django admin interface.

### Restaurant Menu Routes
- `restaurant/menu/items/` - Get a list of menu items.
- `restaurant/menu/items/"id"` - Get, update, or delete a specific menu item.

### Restaurant Booking Routes
- `restaurant/booking/tables/` - View and manage table bookings.

### Authentication Routes
- `auth/` - Djoser authentication routes for user management.
- `auth/api-token-auth/` - Obtain an authentication token.
- `restaurant/menu/api-token-auth/` - Obtain an authentication token specifically for menu related operations.

