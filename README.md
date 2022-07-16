# library-backend-django
## Contains:
<li>Project starting Guide.</li>
<li>API Documentation</li>

## About Project:
Mini back-end system for library management written in python

## Frameworks Used 🌟
<li>Python</li>
<li>Django</li>
<li>Django_Rest_Framework</li>


## Steps to follow for running backend server:
- ### step 1
Clone the github repository for running the project locally.
```
https://github.com/vikasg57/library-backend-django.git
```
- ### step 2
Install all dependencies of the project with the following command.
```
pip install -r requirements.txt
```
- ### step 4
Enter into the librarymanagment folder.
```
cd librarymanagment
```

- ### step 4
Start thr backend server with following command.
```
python manage.py runserver
```

# REST API DOCUMENTATION


## Sign up into the app

### Request

`POST /books/signup/`

    curl --location --request POST 'http://localhost:8000/books/signup/' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY; sessionid=9jmyl7ed25rtss8qayp8392o6dicndys' \
    --data-raw '{
    "first_name":"vikas",
    "last_name":"gaikwad",
    "email":"vis@ede.com",
    "password":"123123e",
    "is_admin": true
    }'

### Response

if Successful
    
    '{
    "first_name":"vikas",
    "email":"vis@ede.coom
    }'

if User already Present

    {"message": "user already exist"}

## Log in into the app

### Request

`POST /books/login/`

    curl --location --request POST 'http://localhost:8000/books/login/' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY; sessionid=9jmyl7ed25rtss8qayp8392o6dicndys' \
    --data-raw '{
    "email":"vis@ede.com",
    "password":"123123e"
    }'

### Response

if successful

    {"massage": "User logged in Successfully"}

if user not present

    {"massage": "User not present please sign up first"}

## Log out from the app

### Request

`POST /books/logout/`

    curl --location --request POST 'http://localhost:8000/books/logout/' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Cookie: csrftoken=OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY; sessionid=9jmyl7ed25rtss8qayp8392o6dicndys'
### Response

    {"message": "User logged out"}
    

## Get All book from Library

### Request

`GET /books/books`

    curl --location --request GET 'http://localhost:8000/books/books/' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Cookie: csrftoken=WMolgEjumiL4F1yltXhTjsNQNY3kMW6rnSzkjR0Qid5wukZaLdYWHLoSfeng5DJK; sessionid=a99w1ofkik65np8ce0rctzuycqd7qli1'
### Response

    [
     {
        "book_name": "polity",
        "description": "indian polity",
        "year": "2005",
        "book_authors": [
            {
                "author_name": "laxmikant",
                "uuid": "dd3509f0-ac84-48fe-bf80-7f436462568f"
            },
            {
                "author_name": "ramesh singh",
                "uuid": "54edc908-5040-4e5b-b963-7f303880ed66"
            }
        ],
        "uuid": "a744f8a1-d436-467c-af89-0be6fb858343"
    },
    {
        "book_name": "jaipt",
        "description": "jscript demo",
        "year": "2000",
        "book_authors": [],
        "uuid": "8005ef77-d6e9-4e3b-8daa-f18c346ae0d1"
    },
    ]

## Add the book into Library

### Request

`POST /books/books/`

    curl --location --request POST 'http://localhost:8000/books/books/' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY; sessionid=9jmyl7ed25rtss8qayp8392o6dicndys' \
    --data-raw '{
    "book_name": "you dont know js",
    "description": "jscript demo",
    "authors":[{"author":"kyle simpson"},{"author":"simpson"}],
    "year": "2000"
    }'
### Response

if User is Admin

    {
    "book_name": "you dont know js",
    "description": "jscript demo",
    "year": "2000",
    "book_authors": [
        {
            "author_name": "kyle simpson",
            "uuid": "50534ae1-9641-41fb-8c0b-8febe26f31b2"
        },
        {
            "author_name": "simpson",
            "uuid": "f0172307-3df6-4b83-ad2a-de98e32a8238"
        }
    ],
    "uuid": "d63a55f1-46e5-4974-b7f1-7878afd302f2"
    }

if User is not Admin

    {
    "message": "You do not have permission to perform this action"
    }

## Edit request for book

### Request

`PUT /books/books/?book_id=uuid`

    curl --location --request PUT 'http://localhost:8000/books/books/?book_id=8005ef77-d6e9-4e3b-8daa-f18c346ae0d1' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Content-Type: application/json' \
    --header 'Cookie: csrftoken=OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY; sessionid=9jmyl7ed25rtss8qayp8392o6dicndys' \
    --data-raw '{
    "book_name": "javascript",
    "description": "javascript in depth analysis",
    "year": "2000"
    }'
### Response

if User is Admin.

    {
    "book_name": "javascript",
    "description": "javascript in depth analysis",
    "year": "2000",
    "book_authors": [],
    "uuid": "8005ef77-d6e9-4e3b-8daa-f18c346ae0d1"
    }

if User is not Admin.

    {
    "message": "You do not have permission to perform this action"
    }

## Delete book from library

### Request

`DELETE /books/books/?book_id=uuid`

    curl --location --request DELETE 'http://localhost:8000/books/lbooks/?book_id=uuid' \
    --header 'X-CSRFToken: OJ4RDQFHCNfshnGm8FmQhOsZtnH0HnmAutB8VJWGh7j0lYVTPCf9M2D4MSnyh0aY' \
    --header 'Cookie: csrftoken=WMolgEjumiL4F1yltXhTjsNQNY3kMW6rnSzkjR0Qid5wukZaLdYWHLoSfeng5DJK; sessionid=a99w1ofkik65np8ce0rctzuycqd7qli1'

### Response

if User is admin.

    {"message": "book deleted successfully"}

if User is not Admin.

    {
    "message": "You do not have permission to perform this action"
    }

###  Thanks for the reading hope you have nice day.