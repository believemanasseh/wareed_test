
# Wareed Test




## Run Locally

Clone the project

```bash
  git clone git@github.com:believemanasseh/wareed_test.git
```

Go to the project directory

```bash
  cd wareed_test
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Create superuser account

```bash
  python3 manage.py createsuperuser
```

Run migrations

```bash
  python3 manage.py migrate
```

Start django server

```bash
  python3 manage.py runserver
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

`DEFAULT_FROM_EMAIL`

`EMAIL_HOST_USER`

`EMAIL_HOST_PASSWORD`


## API Reference
All requests to any endpoint should include an authorization header containing the access token. e.g. "Authorization: Bearer <access_token>"


#### Get tokens

```http
  POST /api/token
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `username`      | `string` | **Required**. Valid username |
| `password`      | `string` | **Required**. Valid password |

#### Refresh token

```http
  POST /api/token/refresh
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `refresh`      | `string` | **Required**. Valid refresh token |

#### Get all students

```http
  GET /api/students
```

#### Get student

```http
  GET /api/students/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Get students less than age

```http
  GET /api/students/search?age=${age}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `age`      | `str` | **Required**. Age to search students |

#### Send emails to students

```http
  POST /api/students/send-email
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `to_email`      | `list` | **Required**. Valid email addresses |
| `subject`      | `str` | **Required**. Valid subject/header |
| `text`      | `str` | **Required**. Valid text/message |



