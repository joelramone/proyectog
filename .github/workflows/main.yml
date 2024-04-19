name: Docker Build and Deployment

on:
  push:
    branches:
      - main

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Login to Docker Hub
      run: echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
      env:
        DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
        DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}

    - name: Build Docker images
      run: |
        cd backend
        docker build -t ${{ secrets.DOCKER_USERNAME }}/django-backend .
        docker push ${{ secrets.DOCKER_USERNAME }}/django-backend
        cd ../gui
        docker build -t ${{ secrets.DOCKER_USERNAME }}/django-gui .
        docker push ${{ secrets.DOCKER_USERNAME }}/django-gui
        cd ../process
        docker build -t ${{ secrets.DOCKER_USERNAME }}/django-process .
        docker push ${{ secrets.DOCKER_USERNAME }}/django-process

    - name: Start Docker Compose services
      run: docker-compose up -d

    - name: Wait for services to start
      run: sleep 30s

    - name: Stop Docker Compose services
      run: docker-compose down

