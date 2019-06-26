# ponzischeme_webapp

This repository contains the source code the Ponzi Scheme game web app.<br>
You can find the web app here: https://www.ponzischeme-game.com/
It is hosted on pythonanywhere.com

The web app is an async online implementation of the board game Ponzi Scheme.<br>
See https://boardgamegeek.com/boardgame/180899/ponzi-scheme for details on this game.

The main contents of the code:
- frontend (Vue.js)
- backend (Python)


Files needed (in root dir), but not under version control:

`.env     ` (environment variables needed by python) <br>
`site.db  ` (the database with users and games) <br>
`dist     ` (deployed frontend code) <br>

The `.env` file contains the following environment variables:

```
export    SECRET_KEY=
export    SQLALCHEMY_DATABASE_URI='sqlite:///site.db'
export    EMAIL_USER=
export    EMAIL_PASS=
export    BASE_URL='http://localhost:8080'
export    SEND_EMAIL='no'
```

`SECRET_KEY`:  needed for authentication. <br>
`SQLALCHEMY_DATABASE_URI`: the path to the database<br>
`EMAIL_USER` and `EMAIL_PASS`: used for the email address from which notification, confirmation, etc. emails are sent<br>
`BASE_URL`: the base url of the app (localhost:8080 for development, ponzischeme-game.com for the deployed app)<br>
`SEND_EMAIL`: `no` (typically used in development) or `yes` (deployed) <br>

In development mode, to start the backend server, in the root directory:

`FLASK_APP=run.py FLASK_DEBUG=1 flask run`

And the front end, in directory frontend:

`npm run serve`
