# Storefront
OwlHacks 2020

## Searching for Deals on Electronics

The purpose of this program is to detect deals on electronics within a certain proximity given a location and radius.

The user provides a location via latitude & longitude, along with a radius in miles. Storefront then takes these parameters and finds deals on electronics within the radius of the location.

## APIs Utilized

Google Place Search API
Google Place Details API

## Build Requirements

This program requires that you generate an API key at Google Cloud Platform, and that key has to be stored in a key.txt, located in the project folder.
Running the program requires that you run the userGUI.jar file, and after pressing the search button, the user is granted ten seconds to run the main.py file. 
The system running the program requires the java runtime, python, and the BeautifulSoup library.

## Possible Improvements

While the program works in the contexts that we demonstrated, there are parameters for which the program may crash. To solve this, we would have to spend more time on handling
exceptions, and making sure that dead links, missing ratings/names/etc. would be handled accordingly. 
We could work on connecting the currently functioning GUI with the rest of the program.
More time could also be spent finding out how different companies advertise their sales to find a wider breadth of valid websites, and we would also look further than
just the landing page for those deals.
Our program would benefit from being hosted on a website, as it would allow for easier user access, improvements to the UI by use of HTML and CSS, and a more seamless
integration of sample links.
Through our current version, we show that we can handle multiple Google APIs to find information about websites, but more tuning could be done as to what information
is output, and the manner in which it is displayed. 
This program could also be adapted for other uses, such as finding a specific dish at restaurants near the user.
Many aspects of the current implementation are clunky, such as having to input latitude and longitude, but we feel fairly proud of the end result for our first hackathon.

## Trello Board
https://trello.com/b/uRjEz38m/owlhacks-storefront

## Team

 * Alex Liu
 * Steven Giang
 * Matthew Jacobs
 * Athan Kim
