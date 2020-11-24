# db-seeder
Seeds a MongoDB Database with initial data and a Superuser

For run this locally Docker and docker-compose are required.

For seed the Database with dummy records and an admin:
```bash
sudo docker-compose up -d --build
docker exec seeder-cli python seeder seeddb
docker exec -it seeder-cli python seeder createadmin
```

This cli has no other applications.