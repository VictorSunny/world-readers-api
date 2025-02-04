
# WORLD-READERS-API

The world readers api obtains and maintains book recommendations from readers all over the world. Open to all would love to share their favourite pieces of peotry, as well as those looking for their next read based on criterias such as genres and publication dates.


## API Reference

#### SIGN UP

```http
  USER SIGNUP ENDPOINT: world-readers/v1/signup/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `email: str, username: str, first_name: str, last_name: str, password: str` | Creates a new account for user token application.|

#
#
#### USER AUTHENTICATION  TOKENS

```http
  AUTH TOKEN CREATION ENDPOINT: world-readers/v1/auth/jwt/create/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `email: str, password: str` | Generates auth token [validity: 5 days], and refresh token [validity: 7 days]. |

```http
  AUTH TOKEN REFRESH ENDPOINT: world-readers/v1/auth/jwt/refresh/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `refresh: str` | Generates a new auth token [validity: 5 days]. |


```http
  AUTH TOKEN VERIFICATION ENDPOINT: world-readers/v1/auth/jwt/create/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `POST` | `token` | Confirms token validity. Advisable to be done before addition to request header|

#
#
#### BOOKS RETRIEVAL AND SUBMISSION

```http
  BOOK DATA READ/WRITE ENDPOINT: world-readers/v1/books/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | | Retrieves all book entries from database.|
| `POST` | `name: str, author: str, year: int, category_id: str(genre name)` | Creates a new book entry in database.|


```http
  SINGLE BOOK READ/WRITE ENDPOINT: world-readers/v1/books/{book_id}/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | | Retrieves single book entry with matching book_id from database.|
| `PUT` | `name: str, author: str, year: int` | Updates single book entry with matching book_id in database.|


```http
  BOOKS DATA READ ENDPOINT: world-readers/v1/books/categories/{name}/
```

| METHOD | PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | | Retrieves all book under specified category 'name' from database.|


```http
  BOOK GENRES READ ENDPOINT: world-readers/v1/books/categories/
```

| METHOD | JSON PARAMETERS     | Description                |
| :-------- | :------- | :------------------------- |
| `GET` | | Retrieves all available book categories from database.|

#
#

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SECRET_KEY`

`DEBUG`
#
#


## Installation

- #Install python#

- #Open terminal#

- Create a folder and activate a vitual environment within it.

- Clone this repository into said folder using git.

- Navigate to cloned repo and run "`pip install -r requirements.txt`"

- In your preferred IDE, set the required environment variables in your .env file

- Run "`python manage.py makemigrations`" and then "`python manage.py migrate`"

- Lastly...


```powershell
  python manage.py runserver
```
#
#
## Technologies
**Server:**  Python, Django, Django rest framework, Djoser, Whitenoise, gUnicorn.

#

## Authors

- [Github@VictorSunny](https://www.github.com/victorsunny)
- [LinkedIn@VictorSunny](https://www.github.com/victor-sunny-6b06ba220)



## 🚀 About Me
Hello there, Victor here.

I'm a backend web developer, and i believe every problem that can be fixed, will be fixed if given enough effort, dedication, and critical thinking, skills all of which are in possession.

I am highly proficient in backend/logical web/app developement using Python and it's related technologies, readily adopting and adapting to new and required technologies.


