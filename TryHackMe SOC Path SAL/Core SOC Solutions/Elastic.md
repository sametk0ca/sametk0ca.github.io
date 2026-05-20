Elastic Stack (ELK) was originally developed to store, search, and visualize large amounts of data. Organizations used it to monitor application performance and perform searches on large datasets. Over time, its features made it popular in security operations as well. Now, many SOC teams use ELK almost as a SIEM solution. 

Elastic Stack is a collection of different open-source components that work together to collect data from any source, store and search it, and visualize it in real time.

![[f858c0d22d015b663438dae207981532.png]]

## 1. Elasticsearch

The first component, Elasticsearch, is a full-text search and analytics engine for JSON-formatted documents. It stores, analyzes, and correlates data and supports a RESTful API for interacting with it.

## 2. Logstash

Logstash is a data processing engine that takes data from different sources, filters it, or normalizes it, and then sends it to the destination, which could be Kibana or a listening port. A Logstash configuration file is divided into three parts, as shown below.

1. The **Input** part is where the user defines the source from which the data is being ingested.
2. The **Filter** part is where the user specifies the filter options to normalize the log ingested above. 
3. The **Output** part is where the user wants the filtered data to be sent. It can be a listening port, Kibana Interface, Elasticsearch database, or file. 

Logstash supports many Input, Output, and Filter plugins.

## 3. Beats

Beats are host-based agents known as data-shippers that ship/transfer data from the endpoints to Elasticsearch. Each beat is a single-purpose agent that sends specific data to Elasticsearch. 

## 4. Kibana

Kibana is a web-based data visualization tool that works with Elasticsearch to analyze, investigate, and visualize data streams in real time. It allows users to create multiple visualizations and dashboards for better visibility. There is more on Kibana in the following tasks.

## How they work together:

Now that we have learned about all the components of the Elastic Stack, let's see how these components work together step-by-step:

- **Beats** collect data from multiple agents. For example, Winlogbeat collects Windows event logs, and Packetbeat collects network traffic flows.
- **Logstash** collects data from beats, ports, or files, parses/normalizes it into field value pairs, and stores them into Elasticsearch.
- **Elasticsearch** acts as a database used to search and analyze data.
- **Kibana** is responsible for displaying and visualizing the data stored in Elasticsearch. The data stored in Elasticsearch can easily be shaped into different visualizations, time charts, infographics, etc., using Kibana.


![[ec4f681a412aa825b284523dcd5b8650.png]]


## Discover Tab

The Discover tab is where the SOC analysts spend most of their time. This tab shows the ingested logs, the search bar, normalized fields, and more. Analysts can search for the logs, investigate anomalies, and apply filters based on search terms and time periods.

![[9635453d465f7625f5dfda21966aa6a6.png]]

1. **Logs  
    **Each row shows a single log containing information about the event, along with the fields and values found in that log.
2. **Fields Pane  
    **The left panel of the interface shows the list of fields parsed from the logs. We can click on any field to add it to the filter or remove it from the search.
3. **Index Pattern  
    **Each type of log is stored in a different index pattern. We can select the index pattern from which we need the logs. For example, for VPN logs, we would need to select the index pattern in which VPN logs are stored.
4. **Search Bar  
    **It is a place where the user adds search queries and applies filters to narrow down the results. In the next task, we will learn how to perform searches through queries.
5. **Time Filter  
    **We can narrow down results based on any specific time duration. 
6. **Time Interval  
    **This chart shows the event counts over time.
7. **TOP Bar  
    **This bar contains various options to save the search, open the saved searches, share or save the search, etc.
8. **Discover Tab  
    **This is the main workspace in Kibana for exploring, searching, and analyzing raw data.
9. **Add Filter  
    **We can apply filters to specific fields to narrow down results, rather than manually typing entire queries.


There is a special language that we can use inside this search bar to perform our searches. KQL **(Kibana Query Language)** is a search query language used to search the ingested logs/documents in Elasticsearch.

With KQL, we can search for the logs in two different ways.

- Free text search
- Field-based search


## Free text Search

Free text search allows users to search for logs based on text only. That means a simple search of the term `security` will return all the documents that contain this term, irrespective of the field.
![[beb9f3912904e689952027ced1475755.png]]

## Field-based search

In the Field-based search, we will provide the field name and the value we are looking for in the logs. This search has a special syntax as `Field: Value`. It uses a colon as a separator between the field and the value.

![[ffbf735277d98273d6229f4d9ee586bf.gif]]

---
## 🔗 Bağlantılar
- [[TryHackMe SOC Path SAL/index|🛡️ TryHackMe: SOC Analyst Learning Path]]
- [[index|🏠 Ana İndeks]]
