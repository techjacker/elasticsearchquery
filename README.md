# AWS Elasticsearch Query

This library will run your static queries against elasticsearch deployments on AWS. Supply the endpoint plus the local filepath to your JSON file containing the query payload.

Good for lambda functions setting up mappings for AWS elasticsearch deployments.

-----------------------------------------------------------

## Example Usage

### Command Line

#### 1. Set required environment variables
```Shell
# .env
ES_ENDPOINT=https://xxx.xxx.es.amazonaws.com
ES_REGION=eu-west-1
```

#### 2. Create JSON file with your Elasticsearch query to be run
```Shell
# my_es_query.json
{
	"query": {
	  "match": {
	  }
	}
}
```

#### 3. Run your query
It will automatically pick up your AWS credentials from your shell's environment.
```Shell
$ elasticsearchquery <es_index> <query_filepath>
$ elasticsearchquery places my_es_query.json
```


### Programmatic API

```
from elasticsearchquery import ElasticSearchQuery


esQuery = ElasticSearchQuery(
  es_endpoint='https://xxx.xxx.es.amazonaws.com',
  index_name='my_index',
  query_file='path_to_query.json',
  region='eu-west-1',
)
esQuery.run()
```
-----------------------------------------------------------
## Unit Tests

#### 1. Set Environment
Make a virtual environment and intall the dependencies.
```
$ make env
$ source env/bin/activate
$ make deps
```

#### 2. Run Unit Tests
```
$ make test
```
