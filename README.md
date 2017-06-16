# Big Data Homework 2

[![N|Solid](https://www-static.ripe.net/static/rnd-ui/atlas/media/anchors/RIPE_NCC_Logo2015-256_q3prZmW.png)](https://atlas.ripe.net/)
### Dati
Data used in batch analysis are anchoring measurements traceroutes running on the 13th of June in 2017. 
Traceroute records are obtained by a script that downloads  measurements specified in input file, adding new records on tail of output file.
Requests are structured as  follows:

> https://atlas.ripe.net/api/v2/measurements/"+id+"/results?start=1497312000&stop=1497398399&format=txt

### Task 1
Distribution of hop counts.

### Task 2
Detection of anomalies in rtt

### ToDo
  - Extend the input on Built-In and UDM. 
  - Check that ids in idFile.txt correspond to measurement running (grep is enough?)
  - Magic

