# Overview

This is a REST API built with FastAPI and PostgreSQL. It allows you to perform **CRUD (Create, Read, Update and Delete)** operations on a **Person** resource. 

API URL: https://hngstagetwo-wpel.onrender.com

You can create a new resource by making a `POST` request to the `/api` endpoint without adding the `user_id` to the URL. 

By providing the `user_id` and making the corresponding `HTTP` requests, you can update, get and delete a resource. The user_id field accepts both the id of the person and the name.

You can also get all the resources available in the database by making a `GET` request to the `/api` endpoint

These **endpoints** are described in more detail below.

## Contents

- [Getting Started]
- [Endpoints]
    - [1. Create a Person]
    - [2. Get All People]
    - [3. Get a Person by ID]
    - [4. Update a Person]
    - [5. Delete a Person]
- [Data Validation]
- [API Limitations]
    

## Getting Started

For instructions on how to setup the application, go to the README file here: https://github.com/Ideeee/hngstagetwo/blob/main/README.MD

## Endpoints

The API provides the following endpoints for managing the persons resource:

### 1\. Create a Person

- **Endpoint**: `POST /api`
- **Description**: Creates a new person resource.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Request Body**: Accepts a JSON object containing name(required), and city(optional).

```javascript
{  
    "name": "Kelechi",
    "city": "Lagos"
}
```

- **Responses**: 

>Status code: 201

```javascript
{  
    "id": 1,
    "name": "Kelechi",
    "city": "Lagos"
    "date_created": current UTC time,
    "last_updated": current UTC time
}
```

    

### 2\. Get All Persons

- **Endpoint**: `GET /api`
- **Description**: Returns all available persons in the database.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Request**: Make a GET request to the `/api` endpoint.
- **Response**: Returns an array of all person resources in the database.

>Status code: 200

```javascript
[
    {  
        "id" : 20,
        "name" : "Kelechi",
        "city": "Lagos"
        "date_created": current UTC time,
        "last_updated": current UTC time
    },
    {  
        "id" : 2,
        "name" : "Adele",
        "city": null
        "date_created": current UTC time,
        "last_updated": current UTC time
    },   // etc....
] 
```
    

### 3\. Get a Person by ID

- **Endpoint**: `GET /api/{user_id}`
- **Parameters** `GET /api/{id}` or `GET /api/{name}`
- **Description**: Returns the details of a single person resource.
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Response**: JSON object of the person with the specified `id` and person `name'. Error message **(404)** if person not found.

>Status code: 200

```javascript
{  
    "id" : 35,
    "name" : "Rema",
    "city": "Lagos",
    "date_created": current UTC time,
    "last_updated": current UTC time
}
```

>Status code: 404

```javascript
{  
    "detail" : "Resource Not Found"
}
```
    

### 4\. Update a Person

- **Endpoint**: `PATCH /api/{user_id}`
- **Parameters** `PATCH /api/{id}` or `PATCH /api/{name}`
- **Description** : Updates/edits the resource
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Request Body**: A JSON object containing the information to be updated, i.e `name` or `city`.

```javascript
{
    "name" : "Obongjayar",
    "city" : "Okobo"
}
```

>Response: 200

```javascript
{
    "id" : 2,
    "name" : "Obongjayar",
    "city": "Okobo"
    "date_created": current UTC time,
    "last_updated": current UTC time
}
```

>Response: 404
    
 ```javascript
{  
    "detail" : "Resource not found",
}
```
    

### 5\. Delete a Person

- **Endpoint**: `DELETE /api/{user_id}`
- **Parameters** `DELETE /api/{id}` or `DELETE /api/{name}`
- **Description** : Deletes a resource
- **Headers**: `Content-Type: application/json Accept: application/json`
- **Response**: Success message confirming the deletion. Error message **(404)** if person not found. 

>Response: 200

```javascript
{
    "message": "Resource has been deleted successfully"
}
```
>Response: 404
    
 ```javascript
{  
    "detail": "Resource not found",
}
```
---

## Data Validation

As demonstrated above, the API includes basic validation rules for request data. Ensure your requests follow the specified data format to avoid validation errors. E.g, in the request body, the name field can only accept a `string` data type.


## API Limitations

This API has certain limitations that may need to be addressed depending on your project requirements:

**User Authentication and Authorization**: The API does not use authentication and authorization mechanisms. All users have can access all endpoints. You would need to implement proper authentication and authorization to restrict access based on user roles and permissions.



