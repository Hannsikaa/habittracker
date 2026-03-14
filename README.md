# Habit Tracker REST API

A backend REST API for tracking daily habits built using Python and FastAPI.
This project allows users to create, manage, and track habits while maintaining streaks and viewing habit statistics.

## Overview

The Habit Tracker API provides endpoints to manage habits including creation, completion tracking, renaming, deletion, search, and leaderboard ranking based on streak performance.

This project demonstrates backend API development, database interaction, and input validation using modern Python frameworks.

## Features

* Create new habits
* Mark habits as completed
* Rename existing habits
* Delete habits
* Search habits by name
* View leaderboard based on streak performance
* Habit statistics
* Input validation using Pydantic
* Error handling with HTTP exceptions

## Tech Stack

* Python
* FastAPI
* Pydantic
* SQLite
* REST API Architecture

## Project Structure

app/
main.py – API routes and application entry point
operations.py – business logic for habit operations
schemas.py – request and response models
habits.db – SQLite database

## API Endpoints

### Get all habits

GET /habits

### Add a new habit

POST /habits

### Mark habit as completed

PUT /habits/done

### Rename a habit

PUT /habits/change_name

### Delete a habit

DELETE /habits/{name}

### Search habit

GET /habits/search?name=habitname

### Habit leaderboard

GET /habits/leaderboard

### Habit statistics

GET /habits/stats

## Example Habit Response

{
"id": 1,
"name": "exercise",
"status": false,
"streak": 3
}

## Key Concepts Demonstrated

* REST API design
* Backend architecture separation (routes, schemas, operations)
* Data validation using Pydantic
* Database CRUD operations
* Exception handling in APIs

## Future Improvements

* User authentication system
* Multi-user habit tracking
* PostgreSQL database support
* Deployment to cloud
* Frontend dashboard

## Author

Hannsikaa Podishetti
