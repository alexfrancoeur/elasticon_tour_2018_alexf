Ingest boston data:

Add the csv, template and configuration to your logstash directory and run the following command

```
cat boston_energy_water_metrics_2017.csv | bin/logstash -f boston_energy_water_metrics_2017.conf
```
