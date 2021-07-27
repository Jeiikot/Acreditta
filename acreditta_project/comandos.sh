#Crear contenedor, montar volumen y acceder con terminal interactiva
sudo docker run -p 8000:8000 -v /path/Acreditta:/acreditta/ --name=acreditta -it --entrypoint=/bin/bash acreditta -i -P

sudo docker run -d -p 8000:8000 -v /path/Acreditta:/acreditta/ --name=acreditta -it --entrypoint=/bin/bash acreditta -i -P

#Para acceder a un contenedor en ejecución
docker exec -i -t acreditta /bin/bash