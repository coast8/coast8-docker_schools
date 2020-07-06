


# Import and Export Docker images for windows container


https://www.assistanz.com/import-and-export-docker-images/

docker save -o C:\Users\asmythy\docker-files\images\wl-10.3.6_v1.2.tar 66817ef9e6b7
docker load –i c:\temp\nanoserver.tar
docker images
docker run