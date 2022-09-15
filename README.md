# Connect Databricks using cli and flask 

[![Python application test with Github Actions](https://github.com/nogibjj/bokai-databricks/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/bokai-databricks/actions/workflows/main.yml)

__Author: Bokai Zhou__

This is the first individual project to talk to Databricks using a microservice(flask) and command-line tool(click).

Demo link: [Youtube](https://youtu.be/iYT4a8ucho0)

## Test CLI
```linux
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```

## Schema and sample data for the table 
![image](https://user-images.githubusercontent.com/97444802/190298924-7b922984-1058-4deb-af6a-4c6c1c01d64a.png)


## Use CLI to query Databricks SQL
`query-firstn` is to find the first n rows in the table. `max_price` is to find the maximum price for a specific diamond color. 
```linux
chmod +x hello_sql_query.py
./hello_sql_query.py query-firstn --n 5 
./hello_sql_query.py max_price --color D
```

## Mircroservice
```linux
python app.py
```

* Home page
![image](https://user-images.githubusercontent.com/97444802/190297028-222fb4c6-67ca-421e-a62d-71c88f407d3b.png)

* Demo router: default SQL query to select first two rows in the table 
![image](https://user-images.githubusercontent.com/97444802/190297878-c900064a-f596-424a-a43b-2b04441d5e42.png)

* Directly add SQL query after the url
![image](https://user-images.githubusercontent.com/97444802/190298428-0f6abc56-9686-4eaf-b3a2-4600fd728212.png)


