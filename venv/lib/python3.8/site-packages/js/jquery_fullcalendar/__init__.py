import fanstatic
import js.jquery

library = fanstatic.Library('jquery_fullcalendar', 'resources')

fullcalendar = fanstatic.Group([
    fanstatic.Resource(library, 'fullcalendar.css'),
    fanstatic.Resource(
        library, 'fullcalendar.js',
        minified='fullcalendar.min.js',
        depends=[js.jquery.jquery])
    ])
