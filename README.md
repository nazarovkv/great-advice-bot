# great-advice-bot
This project will run docker container with Telegram bot inside of it.

## Build image
`docker build -t great-advice-bot:latest`
## Start container
`docker run -d --rm -p 8000:8000 great-advice-bot:latest`