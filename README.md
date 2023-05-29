# Description

The idea of this project is to track your daily habits and show it in the heatmap format.

![](./screenshots/home.png)

You can add new habits as you want to. But by default, it will only show starting on the day you created.

![](./screenshots/new_habit.gif)

Then you can check those habits that you have done in the specific day.
![](./screenshots/check_habit.gif)

## Setup

1. Install Docker
2. Install Node
3. Install Yarn
4. Setup .env file base on the [env.example](./.env.example) file
5. Setup .env frontend file bases on the [frontend/.env.example](./frontend/.env.example) file

## Run

### Backend

The backend run as default on port 8000.

```sh
    docker compose up
```

### Frontend

The frontend run as default on port 5173.

```sh
    cd frontend
    yarn
    yarn dev
```

## Seeding

In order to seed the database with some initial data, you can use the seed's file in the [seeds](./backend/seeds) folder.

In order to run the seeds:

1. Start the backend server

```sh
    docker compose up
```

2. Run the loaddata django command inside the container:

```sh
docker exec habit-tracker-api-1 python3 manage.py loaddata ./seeds/habits.json

docker exec habit-tracker-api-1 python3 manage.py loaddata ./seeds/days.json

```
