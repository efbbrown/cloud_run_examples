# Quickstart example

## What I've done in this directory

In this folder I'm following the official quickstart guide on cloud run found here:
<https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python>

Next thing to follow is this:
<https://cloud.google.com/run/docs/developing>

## Shell code to deploy

```shell
# Check the current project, make sure its the correct one
gcloud config get-value project

# TODO: Set the project id
PROJECT_ID=project_name

# To build the image
gcloud builds submit --tag gcr.io/$PROJECT_ID/helloworld

# To deploy the image
gcloud run deploy --image gcr.io/$PROJECT_ID/helloworld
```

## Clean up

In order to avoid being billed for any of this infrastructure, make sure to:

1. Stop the image in cloud run and
2. Delete the image from the container registry

OR

1. Delete the project
