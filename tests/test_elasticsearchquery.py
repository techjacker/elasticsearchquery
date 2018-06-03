from elasticsearchquery import ElasticSearchQuery
import json
import pytest


query_file = 'tests/fixtures/query.json'


@pytest.fixture
def expected_query():
    with open(query_file, 'r') as f:
        data = json.loads(f.read())
    return json.dumps(data)


def test_load_query(expected_query):
    esQuery = ElasticSearchQuery('blah', 'blah', query_file, 'region')
    result = esQuery.load_query()
    assert expected_query == json.dumps(result)
