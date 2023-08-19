FROM  python

WORKDIR app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

#docker pull dpage/pgadmin4
#docker run -p 80:80 \
#    -e 'PGADMIN_DEFAULT_EMAIL=user@domain.com' \
#    -e 'PGADMIN_DEFAULT_PASSWORD=postgres' \
#    -d dpage/pgadmin4

#docker run --name db -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres