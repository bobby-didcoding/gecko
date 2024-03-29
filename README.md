# <span style="color:orange">Tech Test - CoinGecko Demo App</span>


***
***
## <span style="color:orange">Prerequisites<span>
* [Docker & Docker Compose](https://docs.docker.com/desktop/) (<span style="color:orange">Local Development with Docker</span> only)
* [Make](https://www.gnu.org/software/make/)

***
***

## Prep repo
There is a small amount of configuration required to start this app. Work through the following commands to ensure you have all the necessary directories.
```
cd app
mkdir static
mkdir media
mkdir logs
cd logs && echo This is our celery log > celery.log
cd ..
cp .env.template .env
```

***
***

## Start Docker
you can now go ahead and build the project
```
make build
```

***
***

### Finished

* Our app UI is accessible at [http://localhost:8000/admin/](http://localhost:8000/admin/)
* The GraphQL UI is available on [http://localhost:8000/graphql/](http://localhost:8000/graphql/)
* Flower is accessible at [http://localhost:5555](http://localhost:5555)

***
*** 


### Example GraphQL queries
Open a browser on [http://localhost:8000/graphql/](http://localhost:8000/graphql/) and use the following query to view all token pairs in the database
```
query{
    tokenPairs{
        basetoken{
            external_id
        }
        quoteToken{
            external_id
        }
    }
}
```
The following will display the pools and their relations.
```
query{
    tokenPairs{
        basetoken{
            external_id
        }
        quoteToken{
            external_id
        }
    }
}
```

### Technical decisions
My decision to utilize Django as the backend framework for this demo app offers numerous advantages. Django provides a robust and scalable environment for building web applications, offering built-in security features, authentication mechanisms, and an extensive ecosystem of third-party packages. Leveraging Django's ORM (Object-Relational Mapping) simplifies database operations, enabling seamless integration with various database systems. Additionally, Django's support for GraphQL through packages like django-graphene facilitates efficient data querying and manipulation, aligning perfectly with your requirement to query token and pool data via GraphQL.

Incorporating Celery, Celery Beat, Redis, and Flower into your architecture enhances the app's performance, scalability, and reliability. Celery, a distributed task queue, enables the execution of asynchronous and periodic tasks, ensuring that data fetching from the Gecko terminal occurs regularly and independently of other app features. Celery Beat complements Celery by providing a scheduler for task scheduling, guaranteeing timely execution of scheduled tasks. Redis serves as Celery's message broker and backend, facilitating communication between Django and Celery workers efficiently. Meanwhile, Flower provides a user-friendly monitoring interface for Celery, allowing easy management and monitoring of task execution across multiple replicas, aligning with your requirement for a distributed architecture. Overall, this technical stack empowers your demo app with robustness, scalability, and efficiency, ensuring seamless operation and management of token and pool data.