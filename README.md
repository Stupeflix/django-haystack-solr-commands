Solr 5.0.0 is easy to deploy with cloud Cores and automatic managed-schema but no more schema.xml file to copy.

Solr 5.0.0 can edit a core's configuration via with the Schema REST API.

Solr 5.0.0 breaked Haystack version 2.3.1 because it uses managed-schema by default and removes the need to copy a schema.xml file.
It also provide a ``bin/solr`` command that start and a Solr daemon service, or administrate the Cores.

This what the  ``manage.py solr`` command provided by this Django App

# Install

After cloning this repository

  mkvirtualenv django-haystack-solr-commands
  cd django-haystack-solr-commands
  python setup.py install

You will need **wget, tar, rm**

Configure Haystack and this app by adding at to your server settings.py to following:

    HAYSTACK_CONNECTIONS = {
      'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr/haystacksolrcommandsexamplecore/',
      },
    }

    SOLR_DIRECTORY = "."
    SOLR_VERSION = "5.0.0"
    SOLR_CORE = 'haystacksolrcommandsexamplecore'

Add ``haystack_solr_commands`` to your INSTALLED_APPS and run :

  python manage.py solr

# Versions tested:

- Python 2.7+
- Django 1.4+
- Haystack 2.3.1+ with Solr 5.0.0+ support
- Search engine used : Solr 5.0.0+ with the latest pysolr
- Oracle Java JVM version 7 or 8

# About Solr 5.0.0

What major changes in 5.0.0 breaks Haystack 2.3.1 apart from the schema.xml and the daemon service start and stop commands ?

Quoting CHANGES.txt in the 5.0.0 distribution :
```
* The following legacy numeric and date field types, deprecated in Solr 4.8, are no
  longer supported: BCDIntField, BCDLongField, BCDStrField, IntField, LongField,
  FloatField, DoubleField, SortableIntField, SortableLongField, SortableFloatField,
  SortableDoubleField, and DateField.  Convert these types in your schema to the
  corresponding Trie-based field type and then re-index.  See SOLR-5936 for more
  information.
```
**Sortable*Fields** have been replace with their equivalent **Trie*Field**

Since 4.8.0, Apache Solr now requires Java 7 or greater (recommended is Oracle Java 7 or OpenJDK 7, minimum update 55; earlier versions have known JVM bugs affecting Solr).
Apache Solr is fully compatible with Java 8.
