# MRBS Kiosk

### Structured for UBC MRBS pages. 

The current url templating function is made to build a series of tabs that the kiosk can cycle through for displaying bookings.

### Dependencies

 - Raspberry pi 3B+ or newer
 - A screen, power, and an internet connection (!)
 - Ubuntu MATE 18.04
 - Chromium web browser
 - `xdotool` and `unclutter`

### Services

The core service generates well formatted URLs to provide `chromium`, and launches the browser. A secondary service feeds tab switching commands to the display, which proved inconsistent from the python-based service.

### Todo

 - [x] ~~Get the screen turning off and on over the course of the day
 - [x] ~~Have a reliable daily service reset to get the current day
