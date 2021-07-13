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
