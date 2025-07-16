


## Docker

- `docker build -t paypal-stock -f Dockerfile .`
- `docker run paypal-stock`

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (To remove volumes)
- `docker compose run app /bin/bash` for the command line shell.
