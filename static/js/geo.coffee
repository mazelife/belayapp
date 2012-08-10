#
#   Geocoding functionality.
#

class GPS
    
    threshold: 50
    
    constructor: (@callback=null) ->
        return false unless Modernizr.geolocation
        @watch_id = navigator.geolocation.watchPosition @watch_position_callback

    watch_position_callback: (location) =>
        if location.coords.accuracy >= @threshold
            navigator.geolocation.clearWatch @watch_id
            @callback and @callback location

    watch_position_error: (error) =>
        alert error.message


window.GPS = GPS
