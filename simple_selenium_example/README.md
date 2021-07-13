# Simple selenium example

## What I've done in this directory

In this folder I'm following this example:
<https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp>

## Shell code to deploy

The commands in the tutorial must be out of date as they don't run smoothly.
Instead do this to deploy:

```shell
# Check the current project, make sure its the correct one
gcloud config get-value project

# TODO: Set the project id, image name, region
PROJECT_ID=project_name
SERVICE_NAME=my-screenshot-service
IMAGE_NAME=my_screenshot_service
REGION=europe-west1

# To build the image
gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME

# To deploy the image
gcloud beta run deploy $SERVICE_NAME --image gcr.io/$PROJECT_ID/$IMAGE_NAME --region $REGION --platform managed
```

## Current Error

This example is not running successfully yet. The current error is:

```
selenium.common.exceptions.SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version 77
```

I don't think it matters much which version of chrome is used, but the versions
in `requirements.txt` and `Dockerfile` will have to match.

In order to resolve this, read the following looking for answers:

1. <https://unix.stackexchange.com/questions/233185/install-older-versions-of-google-chrome-stable-on-ubuntu-14-10/590412>
2. <https://askubuntu.com/questions/243394/how-to-install-specific-versions-of-google-chrome-chromium>
3. <https://qxf2.com/blog/building-your-own-docker-images-for-different-browser-versions/>

## Clean up

In order to avoid being billed for any of this infrastructure, make sure to:

1. Stop the image in cloud run and
2. Delete the image from the container registry

OR

1. Delete the project
