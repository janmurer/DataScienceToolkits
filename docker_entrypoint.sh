#!/bin/bash

# Load environment variables from the .env file
if [ -f .env ]; then
    export $(cat .env | xargs)
fi

# Login to W&B
wandb login $WANDB_TOKEN

# Execute the container's command
exec "$@"
