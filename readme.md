# Bungaku API Documentation

## Get All Flowers
```
curl -X GET localhost:3000/flowers?lang={lang}
```
Retrieve information about all available flowers with dual language support (Indonesia and English).

**Example:**
```
curl -X GET localhost:3000/flowers?lang=en
```
```
curl -X GET localhost:3000/flowers?lang=id
```

## Get Flower Data by Name
```
curl -X GET localhost:3000/flower/{flower-name}
```
Retrieve detailed information about a specific flower by providing its name with dual language support (Indonesia and English).

Rules : 
- if you search with indonesia language you need search with indonesia name of flower.
- if you search with english language you need search with english name of flower.
- otherwise if you not use any params language it will default to search on english database

**Example:**
```
curl -X GET localhost:3000/flower/matahari?lang=id
```
```
curl -X GET localhost:3000/flower/suflower?lang=en
```

## User Authentication

### Login
```
curl -X POST localhost:3000/login
```
Authenticate a user with their email and password.

**Example:**
```
{
    "email": "testing@gmail.com",
    "password": "1234567890"
}
```

### Register
```
curl -X POST localhost:3000/register
```
Register a new user with their name, email, and password.

**Example:**
```
{
    "name": "testing",
    "email": "testing@gmail.com",
    "password": "1234567890",
    "confPassword": "1234567890"
}
```

### Logout
```
curl -X DELETE localhost:3000/logout
```
Logout the currently authenticated user.

## User Profile Management

### Get User Detail
```
curl -X GET localhost:3000/user/me
```
Retrieve details of the currently authenticated user.

### Update User Profile
```bash
curl -X PUT localhost:3000/user/update
```
Update user profile information. Use one of the following examples based on the field you want to update:

- **Update Name:**
  ```
  {
      "name": "New Name"
  }
  ```

- **Update Email:**
  ```
  {
      "email": "newemail@example.com",
      "currentPassword": "current_password"
  }
  ```

- **Update Password:**
  ```
  {
      "newPassword": "new_password",
      "currentPassword": "current_password"
  }
  ```
