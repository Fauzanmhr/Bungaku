# get all flowers
curl -X GET localhost:3000/flowers

# get flower data by name 
curl -X GET localhost:3000/flower/:flower-name

# post login
curl -X POST localhost:3000/login

# post register
curl -X POST localhost:3000/register

# delete user logout
curl -X DELETE localhost:3000/logout

# Get User Detail
curl -X GET localhost:3000/user/me

# put user update
curl -X PUT localhost:3000/user/update



