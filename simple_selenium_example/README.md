# Simple selenium example

## What I've done in this directory

In this folder I'm following this example:
<https://dev.to/googlecloud/using-headless-chrome-with-cloud-run-3fdp>

That example was a bit out of date and wouldn't run succesfully so I used some
techniques inspired by this article as well:
<https://qxf2.com/blog/building-your-own-docker-images-for-different-browser-versions/>

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

## Redeployment

If you make changes to your image that you want to deploy rerun
the `gcloud builds submit ...` and `gcloud beta run deploy ...` commands.

```shell
# To build the image
gcloud builds submit --tag gcr.io/$PROJECT_ID/$IMAGE_NAME

# To deploy the image
gcloud beta run deploy $SERVICE_NAME --image gcr.io/$PROJECT_ID/$IMAGE_NAME --region $REGION --platform managed
```

## Clean up

In order to avoid being billed for any of this infrastructure, make sure to:

1. Stop the image in cloud run and
2. Delete the image from the container registry

OR

1. Delete the project
