---
layout: post
title:  "Tree of Codes"
author: sal
categories: [ Jekyll, tutorial ]
image: assets/images/2.jpg
---

Vector Databases
RAG

Vector Database is one of the backbone of advncesment in  LLM and several AI technologies.
With traditional databases such as relational databases, object databases, and graph datases

Vector databases brings the advntages of quick search with less computational cost. With vector databases, the data is hashed into complex matrices and stored into the database. 
This technology is heavily used in LLM and generative AI models. Working with these vectors are faster that strings.
In the context of generative AI, these vectors are easier to compare. Hence meaning can be drawn from these vectors based in its proximity.


Retrieval Augmented Generation (RAG)
This is buillt on top of vector databases. Generative AI models are expensive to train. Generative AI models are train on huge amount of data hence they are expensive to train. But firms using this AI models are interested in applying it in theer domain specific context.
Hence the need to fine-tune these models in order to work with their company data.

For instance, ChatGPT can give you summary of any wikipedi page you can ask.

Assuming you have tones of product documentation within you campany and you want to use AI to help answer some questions in 
from this documentation. ChatGPT was not trained with these data so it can not help. Do you need to retrain an AI model for this use case?
Technically this is posible but not viable because training AI models like GPT is very expensinve.

This is where RAG comes in. With RAG, you can hash your data into complex vectors that and make it accesible to the GPT model.
The AI model can then make predictions based on the information from the vector database.

pgvector is a postgres extention that can convert create a vector dabases from your postgres database.
You can then use your AI model to search for data from this vector datase.


Prerequisit
1. Docker installed.
2. Basic knowledge of docer
3. Optional pgAdmin


Install postgres
We will install posgres17 using docker

```
docker pull postgres:17.4
```

Install pgvector
```
docker pull pgvector/pgvector:pg17
```

NB: The default password for postgres is `postgres` and the default password is `postgres`. It is strongly adviced that you change these credentails but we will stick to these in this tutorial.


Run postgre from docker.
```
docker run -e POSTGRES_USER=postgres \
           -e POSTGRES_PASSWORD=postgres \
           -e POSTGRES_DB=vector_db \
           --name postgres17 \
           -p 5432:5432 \
           -d pgvector/pgvector:pg17
```

Connect to postgres and enable pgvector extention.


Crate pgvector extention
```
CREATE EXTENSION IF NOT EXISTS vector;
```


Verify extension is created
```
SELECT * FROM pg_extension;
```
