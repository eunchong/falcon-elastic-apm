# falcon-elastic-apm

 [Falcon](https://github.com/falconry/falcon) elastic-apm middleware for application performance monitoring.

## Installation

```
pip install falcon-elastic-apm
```

## Usage

Add middleware to your app:

```python
from falcon_elastic_apm import ElasticApmMiddleware
...
app = falcon.API(middleware=[
    ElasticApmMiddleware(
        service_name='falcon_apm', 
        server_url='http://localhost:8200'
    )
])
```
