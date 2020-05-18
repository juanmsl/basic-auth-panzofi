#!/usr/bin/env bash

IMAGE_NAME='basic-auth'
docker build --tag $IMAGE_NAME:latest -f Dockerfile .
