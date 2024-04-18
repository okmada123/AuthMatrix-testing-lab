# About

The purpose of this app was to test the [AuthMatrix](https://portswigger.net/bappstore/30d8ee9f40c041b0bfec67441aad158e) Burp Suite extension.

The app uses 4 roles (roles are assigned to 4 users). It provides a few endpoints that are accessible based on the user's role. For example, the `/admin_data` endpoint is accessible only to a user with the `admin` role.

Session management is not implemented. Roles are indicated in a dedicated HTTP header `X-Role`. For example:

`X-Role: user1`

# Quick start

Just run `docker compose up` and the app will be available on `http://localhost:8000/`.

You can use `authmatrix.txt` to load the AuthMatrix configuration in Burp Suite.