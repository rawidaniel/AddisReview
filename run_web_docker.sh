# Build postgres database server
docker build -t my-web .

# Run the postgres database
docker run -p 80:80 --name my-web-container -d my-web
