HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/defaultcore/',
        'TIMEOUT': 60,
        'INCLUDE_SPELLING': True
    },
}

SOLR_DIRECTORY = "."
SOLR_VERSION = "5.0.0"
SOLR_CORE = 'defaultcore'
