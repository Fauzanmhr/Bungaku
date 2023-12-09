```
# get all flowers
curl -X GET localhost:3000/flowers

# get flower data by name 
curl -X GET localhost:3000/flower/:flower-name

example:
localhost:3000/flower/matahari

# post login
curl -X POST localhost:3000/login

example:

{
    "email": "testing@gmail.com",
    "password": "1234567890"
}

# post register
curl -X POST localhost:3000/register

example:
{
    "name": "testing",
    "email": "testing@gmail.com",
    "password": "1234567890",
    "confPassword": "1234567890",
}

# delete user logout
curl -X DELETE localhost:3000/logout

# Get User Detail
curl -X GET localhost:3000/user/me

# put user update
curl -X PUT localhost:3000/user/update

example:
{
    "name": "testing",
    "email": "testing@gmail.com",
    "password": "superman",
    "confPassword": "superman",
}

```



