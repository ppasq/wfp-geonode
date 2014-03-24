# -*- coding: utf-8 -*-
from settings import *

# read security stuff
import os
SITEURL = os.environ['site_url']
GEONODE_USER = os.environ['geonode_user']
GEONODE_PWD = os.environ['geonode_pwd']
GEONODE_DJANGO_DB = os.environ['geonode_django_db']
GEONODE_POSTGIS_DB = os.environ['geonode_postgis_db']
GEOSERVER_USER = os.environ['geoserver_user']
GEOSERVER_PWD = os.environ['geoserver_pwd']
GEOSERVER_URL = os.environ['geoserver_url']

DEBUG = TEMPLATE_DEBUG = False
DEBUG_STATIC = False

ALLOWED_HOSTS = ['localhost', '.wfp.org',]

SITENAME = 'GeoNode'
TIME_ZONE = 'Europe/Rome'

# OGC (WMS/WFS/WCS) Server Settings
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': GEONODE_DJANGO_DB,
        'USER': GEONODE_USER,
        'PASSWORD': GEONODE_PWD,
        'HOST': 'localhost',
        'PORT': '5432',
    },
    # vector datastore for uploads
    'uploaded' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': GEONODE_POSTGIS_DB,
        'USER' : GEONODE_USER,
        'PASSWORD' : GEONODE_PWD,
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : GEOSERVER_URL,
        # PUBLIC_LOCATION needs to be kept like this because in dev mode
        # the proxy won't work and the integration tests will fail
        # the entire block has to be overridden in the local_settings
        'PUBLIC_LOCATION' : GEOSERVER_URL,
        'USER' : GEOSERVER_USER,
        'PASSWORD' : GEOSERVER_PWD,
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINTNG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIT_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : True,
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'uploaded', #'datastore',
        'TIMEOUT': 10  # number of seconds to allow for HTTP requests
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

MAP_BASELAYERS = [{
    "source": {
        "ptype": "gxp_wmscsource",
        "url": GEOSERVER_URL + "wms",
        "restUrl": "/gs/rest"
     }
  },{
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer",
    "args":["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, 
  {
    "source": {"ptype": "gxp_mapboxsource"},
    "name": "geography-class",
    "title": "Political MapBox",
    "fixed": True,
    "visibility": False,
    "group":"background"
  },
  {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"naip",
    "title":"Satellite Imagery",
    "group":"background",
    "visibility": False
  }, {
    "source": {"ptype": "gxp_bingsource"},
    "name": "AerialWithLabels",
    "title":"Satellite Imagery with labels",
    "fixed": True,
    "visibility": False,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"osm",
    "title":"Terrain MapQuest",
    "group":"background",
    "visibility": False
  },
  {
    "source": {"ptype": "gxp_mapboxsource"},
    "name": "world-light",
    "title": "Light base layer",
    "fixed": True,
    "visibility": False,
    "group":"background"
  },
  {
    "source": {"ptype": "gxp_osmsource"},
    "name": "mapnik",
    "fixed": True,
    "visibility": True,
    "group":"background"
  },
]

LANGUAGES = (
    ('en', 'English'),
    ('es', 'Español'),
    ('it', 'Italiano'),
    ('fr', 'Français'),
)

MAX_DOCUMENT_SIZE = 20 # MB

INSTALLED_APPS = INSTALLED_APPS + (
    'django.contrib.gis',
    'djgeojson',
    'tastypie',
    'wfp.wfpdocs',
    'wfp.gis',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ['email_host']
EMAIL_HOST_USER = os.environ['email_host_user']
EMAIL_HOST_PASSWORD = os.environ['email_host_password']
EMAIL_PORT = 587
EMAIL_USE_TLS = True

THEME_ACCOUNT_CONTACT_EMAIL = 'wfp.geonode@gmail.com'

# Available download formats
DOWNLOAD_FORMATS_VECTOR = [
    'Zipped Shapefile', 'CSV', 'Excel', 'GeoJSON', 'KML',
]
DOWNLOAD_FORMATS_RASTER = [
    'GeoTIFF', 'JPEG', 'PNG', 'ArcGrid', 'KML',
]

# Load more settings from a file called dev_settings.py if it exists
try:
    from dev_settings import *
except ImportError:
    pass

