# Pokemon API

This is a Flask-based API for retrieving Pokemon information.

## Docker Setup

This project is containerized using Docker and Docker Compose. The setup includes:

- A Flask application container
- A PostgreSQL database container

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Running the Application

1. Clone the repository:
   ```
   git clone <repository-url>
   cd pokeAPI
   ```

2. Build and start the containers:
   ```
   docker-compose up --build
   ```

3. The API will be available at http://localhost:5000

### API Endpoints

- `GET /pokemon/<pokemon_name>`: Get information about a specific Pokemon

### Database Setup

The database is automatically set up when the containers start. However, you need to run migrations to create the tables:

1. Access the application container:
   ```
   docker exec -it pokeapi-app bash
   ```

2. Run the migrations:
   ```
   cd backend
   alembic upgrade head
   ```

### Development

For development, the backend directory is mounted as a volume in the container, so changes to the code will be reflected immediately without rebuilding the container.

## Project Structure

- `backend/`: Contains the Flask application code
  - `main.py`: Entry point for the application
  - `src/`: Source code
    - `models/`: Database models
    - `services/`: Business logic
    - `db/`: Database migrations
- `Dockerfile`: Defines the application container
- `docker-compose.yml`: Defines the multi-container setup
- `requirements.txt`: Python dependencies

## Environment Variables

The following environment variables can be set in the `.env` file:

- `ENV_FOR_DYNACONF`: The environment for Dynaconf (default: development)
- `DB_HOST`: The database host (default: pgsql when using Docker)

## Troubleshooting

If you encounter issues with the database, you can try the following:

1. Remove the volumes and start fresh:
   ```
   docker-compose down -v
   docker-compose up --build
   ```

2. Check the logs:
   ```
   docker-compose logs
   ```

3. Make sure the migrations have been applied:
   ```
   docker exec -it pokeapi-app bash
   cd backend
   alembic current
   ```