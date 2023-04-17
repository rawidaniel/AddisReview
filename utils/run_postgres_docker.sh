# Build postgres database server
docker build -t my-postgres .

# Run the postgres database
docker run -p 5432:5432 --name my-postgres-container -d my-postgres
