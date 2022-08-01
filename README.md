# API for Bloggers Social Network
Built on Django Rest Framework

Final version https://github.com/web2cap/api_final_yatube 


## Technology:

- Python and Django
- Rest Framework
- JWTAuthentication and djoser

## Installation
- Clone the repository
- Create and activate virtual environment
- Install all required packages from requirements.txt.
- Apply migrations

## Examples of API requests and responses:
| Resource | Type | Path | Transferred data (JSON) |
| ------ | ------ | ------ | ------ |
| Get an API token | POST | /api/v1/api-token-auth/ | {"username":"","password":""}

#### Answer:
```
{
    "token": "db93aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
}
```

| Resource | Type | Path |
| ------ | ------ | ------ |
| Get List of Posts | GET | /api/v1/posts/ |

#### Answer:
```
[
    {
        "id": 1,
        "text": "In the evening we gathered in the editorial office to talk about the theatre.",
        "pub_date": "2022-04-21T11:22:03.167305Z",
        "author": "test",
        "image": null
        group: 1
    }
]
```

| Resource | Type | Path | Transferred data (JSON) |
| ------ | ------ | ------ | ------ |
| Add post | POST | /api/v1/posts/ | {"text": "","group": ""}

#### Answer:
```
{
    "id": 14,
    "text": "In the evening we gathered at the editorial office to talk about the folk theatre.",
    "author": "anton",
    "image": null
    group: 1
    "pub_date": "2021-06-01T08:47:11.084589Z"
}
```

## Endpoints
| Path | Type | Description |
| ------ | ------ | ------ |
| api/v1/api-token-auth/ | (POST) | pass login and password, get token |
| api/v1/posts/ | (GET, POST) | get a list of all posts or create a new post |
| api/v1/posts/{post_id}/ | (GET, PUT, PATCH, DELETE) | get, edit or delete post by i |
| api/v1/groups/ | (GET) | get a list of all groups |
| api/v1/groups/{group_id}/ | (GET) | get information about the group by id |
| api/v1/posts/{post_id}/comments/ | (GET, POST) | get a list of all post comments with id=post_id or create a new one by specifying the id of the post we want to comment on |
| api/v1/posts/{post_id}/comments/{comment_id}/ | (GET, PUT, PATCH, DELETE) | getting, editing or deleting a comment by id for a post with id=post_id |


### Author:

Pavel Koshelev