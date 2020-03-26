from fanstatic import Library, Resource

library = Library('jquery', 'resources')

jquery = Resource(
    library,
    'jquery-3.3.1.js',
    minified='jquery-3.3.1.min.js')

jquery_slim = Resource(
    library,
    'jquery-3.3.1.slim.js',
    minified='jquery-3.3.1.slim.min.js')
