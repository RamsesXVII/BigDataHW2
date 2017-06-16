# Big Data Homework 2

[![N|Solid](https://www-static.ripe.net/static/rnd-ui/atlas/media/anchors/RIPE_NCC_Logo2015-256_q3prZmW.png)](https://atlas.ripe.net/)
### Dati
Per le analisi batch i dati fanno riferimento alle Anchoring Measurement running il 13 Giugno 2017. Il retrieve dei dati avviene tramite uno script che effettua un download di tutte le misurazioni specificate  nel file in input, aggiungendo i nuovi record in coda ad un file.
Le richieste sono nella forma:
> https://atlas.ripe.net/api/v2/measurements/"+id+"/results?start=1497312000&stop=1497398399&format=txt

### Task 1
Distribuzione del numero di hop

### Task 2
Individuazione di anomalie nella sequenza di rtt

### ToDo
Estendere ricerca anche su Built-In e UDM. Verificare che lo script scriva su file gli id dellle misurazioni effettivamente running (serve una lista degli id presenti, potrebbbe bastare  un grep con conta>0 per ciascun id nel file in input).
d>
