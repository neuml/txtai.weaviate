# txtai -> weaviate integration example

This repository contains an example Weaviate integration with txtai. 

## Installation

```
pip install -r requirements.txt
```

### Start Weaviate locally

Start a local Weaviate instance with docker-compose.

```
docker-compose up
```

## Example Python application

The following will load a subset of a dataset from a Hugging Face datasets into Weaviate. Once successful, a query prompt will be brought up.

```
python example.py
```

## Example API application

An FastAPI-backed application can also be brought up as follows.

```
CONFIG=app.yml uvicorn "txtai.api:app"
```

This API instance can be used with a txtai client (txtai.go, txtai.java, txtai.js, txtai.rs) or with any generic HTTP client. The following shows how to index and search data using cURL.

```
curl -XPOST "http://localhost:8000/workflow" -H "Content-Type: application/json" -d '{"name": "index", "elements": ["US tops 5 million confirmed virus cases","Canadas last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg","Beijing mobilises invasion craft along coast as Taiwan tensions escalate","The National Park Service warns against sacrificing slower friends in a bear attack","Maine man wins $1M from $25 lottery ticket","Make huge profits without work, earn up to $100,000 a day"]}'
# ["db471ead-5764-4933-a3b0-ba5e7e4039db","2e52177a-ee91-4c00-8f94-594c16ddda55","04e9098d-ac14-4392-9341-6079fefc5cdf","7546a8c4-c10d-49ee-9a76-1d0377d18a9d","bc825fd4-3139-448a-a6e0-85d7b9483e6c","99ffbb1b-5910-40a6-921c-2ce8822166a7"]

curl -XPOST "http://localhost:8000/workflow" -H "Content-Type: application/json" -d '{"name": "search", "elements": ["feel good story"]}'
# [{"data":{"Get":{"Post":[{"_additional":{"certainty":0.5416451},"content":"Maine man wins $1M from $25 lottery ticket"}]}}}][dmezzett@neuml ~]$ 
```

## Architecture

This example uses a txtai workflow to index and search with Weaviate. The following diagram illustrates the architecture.

![architecture](![further](https://raw.githubusercontent.com/neuml/txtai.weaviate/master/architecture.png)
