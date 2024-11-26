# contactz

## Start

Server: go to `src/server`, run `npm install` (once only) and then `npm start`


## Scraper

* Written in python
* Python library used: [LinkedIn API for Python](https://github.com/tomquirk/linkedin-api)


## Server

* Base on [JSON-Server (stable version)](https://github.com/typicode/json-server/tree/v0)

Sample statements:
```sh
# Returns all the connections
curl -X GET -H "Content-Type: application/json"  "http://localhost:3000/connection"

# POST a new connection
curl -X POST -H "Content-Type: application/json" -d '{"id":"123", "name": "Lisa","salary": "2000"}' "http://localhost:3000/connection"

```