#!/usr/bin/env python
import urllib

file = urllib.URLopener()
file.retrieve("https://api.import.io/store/data/288c83ca-7d56-4831-ac06-7568cd8a833f/_query?input/webpage/url=http%3A%2F%2Fwww.acgov.org%2Frov%2Fcurrent_election%2F226%2F8484.htm&_user=3deb53d8-6aa2-4c54-9e89-e94b80e2feca&_apikey=j5CqZDxsIbOhbAv5cNbMDs4x8M5%2BPyMODYk%2B2N57SWGTqrDOr4OPi4lhAMfOZltDjGv%2Fc%2F5N2XKMIEIFgfrpxg%3D%3D","/home/media/public_html/projects/2014/20141104_election/precincts.json")
file.retrieve("https://api.import.io/store/data/2e619ff1-b506-436c-aed6-6c4e79ff0e72/_query?input/webpage/url=http%3A%2F%2Fwww.acgov.org%2Frov%2Fcurrent_election%2F226%2F8484.htm&_user=3deb53d8-6aa2-4c54-9e89-e94b80e2feca&_apikey=j5CqZDxsIbOhbAv5cNbMDs4x8M5%2BPyMODYk%2B2N57SWGTqrDOr4OPi4lhAMfOZltDjGv%2Fc%2F5N2XKMIEIFgfrpxg%3D%3D","/home/media/public_html/projects/2014/20141104_election/candidates.json")
		
#open and write the new file
#thefile = open("/home/mission/public_html/wp-content/uploads/restaurant-inspections/data.xml", 'w+')
#thefile.write(html)
#thefile.close()