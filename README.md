# AimLab Task

A Python-based backend service with modular architecture for managing configurations, libraries, and user operations. Fully containerized with Docker and easily deployable either with Docker Compose or directly on your local machine.

## Features

- **Modular Architecture**: Clear separation between configs, libraries, and user management
- **Containerization**: Complete Docker support for consistent development and deployment
- **Flexible Deployment**: Run with Docker Compose or directly on your local machine
- **Environment Management**: Simple configuration via `.env` files
- **Scalable Design**: Built to accommodate future expansion and feature additions

## Tech Stack

- Python 3.x
- Django
- Docker & Docker Compose

## Project Structure

```
aimlab_task/
├── configs/                 # Configuration files and settings
├── library/                 # Core libraries and utilities
├── user/                    # User management
├── .dockerignore            # Docker ignore rules
├── .env.example             # Example environment config
├── .gitignore               # Git ignore rules
├── Dockerfile               # Docker image setup
├── docker-compose.yml       # Docker Compose setup
├── manage.py                # Management script
├── requirements.txt         # Python dependencies
├── start.sh                 # Startup script
```

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) (3.8+ recommended)
- [Docker](https://www.docker.com/products/docker-desktop) (optional)
- [Docker Compose](https://docs.docker.com/compose/) (optional)

### Option 1: Run with Docker (Recommended)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/murodbro/aimlab_task.git
   cd aimlab_task
   ```

2. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your specific settings
   ```

3. **Build and start Docker containers**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   Open [http://localhost:8000/](http://localhost:8000/) in your browser

### Option 2: Run Without Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/murodbro/aimlab_task.git
   cd aimlab_task
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv venv

   # Activate on Windows
   venv\Scripts\activate

   # Activate on macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env with your specific settings
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   Open [http://localhost:8000/](http://localhost:8000/) in your browser

## Usage

Once the application is running, you can:

- Access the admin panel at `/admin/` (if using Django)
- Use the API endpoints according to the documentation
- Configure settings via the web interface or configuration files

## Development

### Adding New Dependencies

1. Add the dependency to `requirements.txt`
2. Rebuild containers if using Docker:
   ```bash
   docker-compose build
   ```
   Or install directly if running locally:
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
