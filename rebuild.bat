#docker container stop docker-scrapy
#docker container rm docker-scrapy
#docker build -t docker-scrapy .
#docker run -itd --name docker-scrapy docker-scrapy
#docker exec -it docker-scrapy /bin/sh

docker container stop my_scrapy
docker container rm my_scrapy
docker build -t my_scrapy .
docker run -itd --name my_scrapy my_scrapy
docker exec -it my_scrapy /bin/sh
