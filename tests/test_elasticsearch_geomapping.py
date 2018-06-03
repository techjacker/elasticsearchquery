# import os
# import pytest
# from handlers.elasticsearch_geomapping import geoMapperFactory


# @pytest.mark.parametrize(('endpoint', 'domain', 'index', 'mapping_file', 'region'), [
#     ('https://foo', 'foo', 'bar', 'baz', 'bam')
# ])
# def test_geomapper_factory(endpoint, domain, index, mapping_file, region):
#     os.environ['ES_ENDPOINT'] = endpoint
#     os.environ['ES_INDEX'] = index
#     os.environ['ES_GEO_MAPPING_FILE'] = mapping_file
#     os.environ['ES_REGION'] = region

#     geomapper = geoMapperFactory()
#     print('elasticsearch_geomapping.handler = %s' % geomapper)
#     assert geomapper.es_domain == domain
#     assert geomapper.region == region
#     assert geomapper.url == '%s/%s' % (endpoint, index)
#     assert geomapper.mapping_file == mapping_file
