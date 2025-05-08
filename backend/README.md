# Pokemon API Database Setup

This README provides instructions on how to set up and initialize the database for the Pokemon API.

## Prerequisites

- PostgreSQL installed and running
- Python environment set up with all dependencies installed

## Database Configuration

The database connection settings are defined in the following files:
- `configs/db_config.toml`: Contains database host, name, and port
- `configs/.secrets.toml`: Contains database username and password
- `alembic.ini`: Contains the SQLAlchemy URL for migrations

Make sure these files have the correct settings for your environment.

## Creating and Applying Migrations

To create and apply database migrations, follow these steps:

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create the initial migration:
   ```
   alembic revision --autogenerate -m "Initial migration"
   ```
   This will create a new migration file in the `src/db/versions` directory.

3. Apply the migration to the database:
   ```
   alembic upgrade head
   ```
   This will create all the necessary tables in the database.

## Troubleshooting

If you encounter issues with the database, here are some common problems and solutions:

### No Data in Database

If you don't see any data in the database after making API requests, check the following:

1. Make sure migrations have been applied:
   ```
   alembic current
   ```
   This will show the current migration version. If it shows "None", you need to apply migrations.

2. Check database connection:
   ```
   psql -U pokemon -h localhost -d pokeapi
   ```
   This will connect to the database using the credentials from `.secrets.toml`. If this fails, check your database settings.

3. Check for errors in the application logs when making API requests.

### Migration Errors

If you encounter errors when creating or applying migrations, check the following:

1. Make sure the database exists:
   ```
   createdb -U postgres pokeapi
   ```

2. Make sure the database user exists and has the correct permissions:
   ```
   createuser -U postgres -P pokemon
   ```

3. Check the connection string in `alembic.ini` to ensure it's correct.

## Database Schema

The database schema consists of the following tables:

- `pokemon`: Stores basic information about Pokemon (name, type, generation)
- `infoPokemon`: Stores additional information about Pokemon (moves)

These tables are defined in the model files in `src/models/`.