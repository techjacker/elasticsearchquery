import json
import os
import requests
import argparse
from requests.exceptions import HTTPError
from aws_requests_auth.boto_utils import BotoAWSRequestsAuth


class ElasticSearchQuery():

    def __init__(self, es_endpoint, index_name, query_file, region):
        self.es_endpoint = es_endpoint
        self.es_domain = es_endpoint.replace('https://', '')
        self.url = '%s/%s' % (es_endpoint, index_name)
        self.query_file = query_file
        self.region = region

    def _load(self, filepath):
        with open(filepath) as f:
            return json.load(f)

    def load_query(self):
        return self._load(self.query_file)

    def _load_auth(self):
        return BotoAWSRequestsAuth(
            aws_host=self.es_domain,
            aws_region=self.region,
            aws_service='es'
        )

    def run(self):
        try:
            query = self.load_query()
            headers = {'Content-Type': 'application/json'}
            r = requests.put(
                self.url,
                data=json.dumps(query),
                headers=headers,
                auth=self._load_auth()
            )
            r.raise_for_status()
            return r
        except HTTPError as e:
            print('[HTTPError]: HTTP request failed')
            print(e)
            resp = r.json()
            if 'error' in resp:
                print(resp['error'])
        except Exception as e:
            print('[ERROR]: API update failed')
            print(e)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=(
            'Exports systemd logs to different storage backends'
            ', eg cloudwatch/elasticsearch.'
        )
    )
    parser.add_argument(
        'index',
        type=str,
        help='es index to fun query against'
    )
    parser.add_argument(
        'query',
        type=str,
        help='path to query file'
    )
    args = parser.parse_args()

    esQuery = ElasticSearchQuery(
        es_endpoint=os.environ['ES_ENDPOINT'],
        index_name=args.index,
        query_file=args.query,
        region=os.environ['ES_REGION'],
    )
    esQuery.run()
