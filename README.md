# Project-reliable-NMBS
making a website that tracks the punctuality of NMBS trains 

The data is gathered from NMBS in realtime and static GTFS and NETEX format. This data is processed and than displayed to the user to simplify the process of checking the reliability of a given train run by the NMBS.

-------------HIGH-LEVEL PROJECT OVERVIEW-------------
the project has several stages of completion with the final stage being the most completed and polished version possible of this projects. 

Stage 1: the Beginning
plug all the available data (possibly excl. netex) into the program and create databases that store the static and realtime data. Add functionality to do very basic parsing of the received data like list of stations or list of train numbers

Stage 2: comprehensive backend
- link multiple databases to eachother
- create backend for train info fetching
- create backend for station info fetching
- create backend for train delay calculation and processing
- create backend for train composition
- create backend for Belgian network overview (amount of delayed trains, punctuality, etc.)

Stage 3: frontend learning
Since i have no frontend experience and the langauges used for the developing of such interfaces are foreign to me, an inital "discovery" phase will be necessary. In this phase, decisions will be taken to determine which frameworks and languages will be used to create the eventual website. Mini-projects that are not necessarily related to this project might be created for learning purposes.

Stage 4: basic frontend implementation
The lessons learned from Stage 3 will be implemted to transform this project from backend only to a nice website. If possible, attention should be given to the ease of use on mobile devices as well.

- create main page
- decide on and add general navigational layout (tab system with a column on the left side? or something else?)



Stage 5: final stage (fully completed project)
--> project in a nutshell: similar to zugfinder but for belgian trains and looks better

--> elaborated: the projects is made of 2 halved the frontend and the backend. The backend will be the inital focus and will be coded in python. It will gather the data provided by NMBS and process it into local databases (eg. using SQL). It will also process the data to feed it into the frontend (eg. train positions, station information, etc.). The frontend is a website that presents the gathered data and the aquired insights by data processing (backend). The presentation will be visiually appealing (better than the barebones UI approach of zugfinder). A possible list of possible fuctionalities on the website include: 

Tab stations:
- list of stations
- a digital remake of the physical timetable present at stations with realtime info

Tab trains:
- a search bar for trains using train numbers and/or departure + arrival stations that shows the trajectory of the train (which stations it serves and when)
- a visualisation of the path the train takes from start to finish on the map
- a visualisation using graphs, tables, etc. showing how often the selected train is late (between 2 specified stations) + further insights (eg. a graph of the amount of late trains over time)
- a visualisation of the current train composition

tab map:
- a map (gathered from openrailwaymap.org ?) that displays all current trains running on the belgian rail network. (the position can maybe be guesstimated based on the real-time punctuality info and the avarage speed of the train according to the timetable?)

tab Belgian network overview:
- bunch of general (national level) insights derived from the processing of the data. For example: amount of delayed trains that day/week/month/year, punctuality percentage of trains that day/week/month/year, 
