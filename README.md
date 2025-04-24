# Jahan News Blog

A modern news blog built with Django, featuring user authentication, article management, and a responsive design.

# Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository
```bash
git clone https://github.com/balaara-teck/jahan_news_blog.git
cd jahan_news_blog
mkdir media
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration

1. Database Setup
```bash
python manage.py migrate
```

2. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

3. Collect static files
```bash
python manage.py collectstatic
```

## Running the Development Server

1. Start the Django development server
```bash
python manage.py runserver
```

2. Access the application:
   - Main site: http://localhost:8000
   - Admin panel: http://localhost:8000/admin

## Features

- User authentication and registration
- Article creation and management
- Admin dashboard using Django Jazzmin
- Responsive design
- Image upload support
- Social sharing functionality

## Project Structure

- `news/` - Main Django application
- `static/` - Static files (CSS, JavaScript, images)
- `templates/` - HTML templates
- `media/` - User-uploaded files
- `requirements.txt` - Project dependencies

## Dependencies

Key packages used in this project:
- Django 5.1.2
- django-allauth 65.1.0
- django-jazzmin 3.0.1
- Pillow 11.0.0
- And more (see requirements.txt)

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the terms included in the LICENSE file.
