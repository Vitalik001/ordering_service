FROM postgres

WORKDIR /code/db

COPY create_tables.sql /docker-entrypoint-initdb.d/

EXPOSE 5432

CMD ["service", "postgresql", "start"]
#    sleep 10 && \
#    psql -U postgres -c "SELECT 'CREATE DATABASE postgres' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'postgres');" && \
#    psql -U postgres -d postgres -f /docker-entrypoint-initdb.d/create_tables.sql

