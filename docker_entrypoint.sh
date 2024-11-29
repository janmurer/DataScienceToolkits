#!/bin/bash

# Export W&B token from .env file
source .env
export WANDB_API_KEY=$WANDB_TOKEN

# Log into W&B
wandb login $WANDB_API_KEY

# Execute the container's command
exec "$@"
