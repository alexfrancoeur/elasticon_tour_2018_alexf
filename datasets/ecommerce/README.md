Ingest sample_ecommerce data:

```
curl --user elastic -H 'Content-Type: application/x-ndjson' -XPOST 'localhost:9400/sample_ecommerce/_bulk?pretty' --data-binary @ecommerce.json
```

or run the python script to generate data in real time

`ecommerce_ingest.py`
