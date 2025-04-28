# AimLab Task

A Python-based backend service with modular architecture for managing configurations, libraries, and user operations. Fully containerized with Docker and easily deployable either with Docker Compose or directly on your local machine.

## Features

- **Modular Architecture**: Clear separation between configs, libraries, and user management
- **Containerization**: Complete Docker support for consistent development and deployment
- **Flexible Deployment**: Run with Docker Compose or directly on your local machine
- **Environment Management**: Simple configuration via `.env` files
- **Scalable Design**: Built to accommodate future expansion and feature additions
- **Comprehensive Testing**: Extensive test coverage using pytest and Django test framework

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- pytest
- Docker & Docker Compose

## Project Structure

```
aimlab_task/
├── configs/                  # Configuration files and settings
├── library/                  # Core libraries and utilities
├── user/                     # User management
├── tests/                    # Test files and fixtures
│   ├── __init__.py           # (Optional, can be removed if not needed)
│   ├── conftest.py           # Global pytest fixtures
│   ├── library/              # Library-specific tests
│   │   └── __init__.py       # (Optional, can be removed if not needed)
│   │   └── tests.py          # Library-specific tests
│   └── user/                 # User-specific tests
│       └── __init__.py       # (Optional, can be removed if not needed)
│       └── tests.py          # User-specific tests
├── .dockerignore             # Docker ignore rules
├── .env.example              # Example environment config
├── .gitignore                # Git ignore rules
├── Dockerfile                # Docker image setup
├── docker-compose.yml        # Docker Compose setup
├── manage.py                 # Management script
├── requirements.txt          # Python dependencies
├── start.sh                  # Startup script

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

## Testing

The project uses pytest for comprehensive testing of all components. Tests are organized in a modular structure similar to the main application.

### Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Global fixtures shared across all tests
├── library/             # Library-specific tests
│   ├── __init__.py
│   └── tests.py         # Tests for library models and APIs
└── user/                # User-specific tests
│   ├── __init__.py
│   └── tests.py         # Tests for user functionality
```

### Running Tests

#### With Docker:

```bash
# Run all tests
docker-compose run --rm web pytest

# Run specific tests
docker-compose run --rm web pytest tests/library/tests.py

# Run tests with coverage
docker-compose run --rm web pytest --cov=.
```

#### Without Docker:

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/library/tests.py

# Run tests with coverage
pytest --cov=.
```

### Key Test Features

- **Fixtures**: Common test fixtures are defined in `conftest.py` for reuse across tests
- **Database Tests**: Using `@pytest.mark.django_db` decorator for database-dependent tests
- **API Testing**: Complete testing of all API endpoints using Django REST Framework test client
- **Model Testing**: Comprehensive testing of model functionality and constraints
- **Authentication**: Testing of user authentication and permission systems

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

### Adding New Tests

1. Create test files in the appropriate directory under `tests/`
2. Follow the pytest naming conventions: files should start with `test_` or end with `_test.py`
3. Run the tests to ensure they pass before committing

## License

This project is licensed under the MIT License - see the LICENSE file for details.