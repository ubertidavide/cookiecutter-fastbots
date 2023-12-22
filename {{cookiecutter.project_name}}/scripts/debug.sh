#!/bin/sh

# start the bot from the entrypoint
poetry run python -m debugpy --listen 5678 main.py