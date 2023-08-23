# Use the official PostgreSQL image as the base image
FROM postgres

WORKDIR /code/db
# Set environment variables for the PostgreSQL container
ENV POSTGRES_PASSWORD=postgres

# Expose the PostgreSQL port
EXPOSE 5432

ADD create_tables.sql /docker-entrypoint-initdb.d/

