Features

1. User Registration: Allows new users to register with email and password.
2. User Login: Provides an authentication token for user login.
3. Ride Management:
    1. Create ride requests.
    2. viewing ride details
    3. listing all rides
    4. Update the status of rides.
    5. Assign drivers to rides.
    6. Update the current location of rides.

Endpoints

1. POST /api/register/  ----user registration
Request Body: { "username": "string", "email": "string", "password": "string", "is_driver": "boolean" }
Response: { "user": { "username": "string", "email": "string" }, "message": "User created successfully" }

eg:     {
    "user": {
        "id": 16,
        "username": "test",
        "email": "test@gmail.com",
        "is_driver": false
    },
    "message": "User created successfully"
}


2. POST /api/login/     ----Login User
Request Body: { "email": "string", "password": "string" }
Response: { "token": "string", "user_id": "integer", "email": "string" }

eg: {
    "token": "string",
    "user_id": 16,
    "email": "test@gmail.com"
}


3. POST /api/rides/  ----Create Ride Request
Request Body: { "pickup_location": "string", "dropoff_location": "string" }
Response: { "id": "integer", "rider": "integer", "driver": "null", "pickup_location": "string", "dropoff_location": "string", "status": "PENDING", "created_at": "datetime", "updated_at": "datetime" }

eg: {
    "id": 5,
    "rider": 16,
    "driver": null,
    "pickup_location": "thrikkakara",
    "dropoff_location": "palarivattom",
    "current_location": null,
    "status": "PENDING",
    "created_at": "2024-09-19T04:33:36.698272Z",
    "updated_at": "2024-09-19T04:33:36.698272Z"
}

4. PATCH /api/rides/{id}/update_status/ -----Update Ride Status
Request Body: { "status": "string" } (Status options: PENDING, IN_PROGRESS, COMPLETED)
Response: { "status": "string" }

eg: {
    "status": "COMPLETED"
}

5. POST /api/rides/{id}/match_driver/   -----Assign Driver to Ride
Response: { "driver": "string" }

eg:   {"driver":"sruthi"}

6. PATCH /api/rides/{id}/  ------Update Ride Location
Request Body: { "current_location": "string" }
Response: { "current_location": "string" }

eg: {
    "current_location": "palarivattom"
}

7. GET api/rides/{ride_id}/ ------ viewing ride details

eg: {
    "id": 5,
    "rider": 16,
    "driver": 7,
    "pickup_location": "thrikkakara",
    "dropoff_location": "palarivattom",
    "current_location": "palarivattom",
    "status": "COMPLETED",
    "created_at": "2024-09-19T04:33:36.698272Z",
    "updated_at": "2024-09-19T04:39:32.434651Z"
}

8. GET api/rides/ ---- viewing all rides
