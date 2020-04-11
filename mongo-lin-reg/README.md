# Linear Regression on Housing Prices w/ MongoDB

This is an application which stores house data in a MongoDB database, retrieves it, and performs linear
 regression on it to predict house prices.
 
src/storeHouseData.py takes the data from data/housing.txt and stores it in a MongoDB database called `housing_ml` in
 a collection called `houses`.

src/main.py retrieves all the documents from the `houses` collection, performs linear regression on the data, and
 predicts the price of a house. The normal equation method is used if there are fewer than 10,000 training examples (as
  recommended by Andrew Ng), and gradient descent is used otherwise.
  
## Development

```shell script
docker-compose up
```

## Deployment

```shell script
docker-compose push
```

```shell script
docker-machine create --driver amazonec2 --amazonec2-open-port 8080 --amazonec2-region ca-central-1 mongo-lin-reg
```

```shell script
docker-machine env mongo-lin-reg
```

```shell script
eval $(docker-machine env mongo-lin-reg)
```

```shell script
docker-machine active
```

```shell script
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

```shell script
docker-compose logs
```

```shell script
eval $(docker-machine env -u)
```

```shell script
docker-machine rm mongo-lin-reg
```

## Useful Links

### DockerHub
- [DockerHub repo](https://hub.docker.com/repository/docker/calumsieppert/mongo-lin-reg/general)

### Docker Compose
- [Compose file reference](https://docs.docker.com/compose/compose-file/)
- [Compose networking](https://docs.docker.com/compose/networking/)
- [Compose file composition](https://docs.docker.com/compose/extends/)
- [Compose in production](https://docs.docker.com/compose/production/)
- [Compose install](https://docs.docker.com/compose/install/)

### Docker Machine
- [Docker Machine AWS Tutorial](https://docs.docker.com/machine/examples/aws/)
- [Docker Machine install](https://docs.docker.com/machine/install-machine/)

### AWS
- [AWS Educate tutorials](https://www.awseducate.com/student/s/pathways)
- [AWS Console](https://ca-central-1.console.aws.amazon.com/console/home?region=ca-central-1#)
