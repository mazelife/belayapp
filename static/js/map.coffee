#
#   Geocoding functionality.
#

window.map_image = (latitude, longitude, container, options={}) ->
    default_options =
        zoom: 14
        size: "400x400"
        color: "blue"
    _.defaults options, default_options
    pieces = [
        "center=#{ latitude },#{ longitude }",
        "zoom=#{ options.zoom }",
        "size=#{ options.size }",
        "sensor=true",
        "markers=color:#{ options.color }%7Clabel:S%7C#{ latitude },#{ longitude }"
    ]
    url = "http://maps.googleapis.com/maps/api/staticmap?" + pieces.join "&"
    image = jQuery "<img src=#{ url } width=\"400\" height=\"400\">"
    jQuery("body").append image
