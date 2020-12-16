# Thanks to Ceyhun Uzunoglu for the original script

import requests, json
from itertools import groupby

url = "https://monit-grafana.cern.ch/api/datasources/proxy/8983/_msearch"

payload_index_props = {"search_type":"query_then_fetch","ignore_unavailable":True,"index":["cms-20*"]}
payload_query = {
  "size": 0,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "RecordTime": {
              "gte": "now-2y",
              "lte": "now",
              "format": "epoch_millis"
            }
          }
        },
        {
          "query_string": {
            "analyze_wildcard": True,
            #"query": "Type:production AND Status:Completed AND Campaign:\"RunIISummer19UL17wmLHEGEN\" AND WMAgent_SubTaskName:/.*GEN.*/"
            "query": "Type:production AND Status:Completed AND Campaign:\"RunIISummer19UL17GEN\" AND WMAgent_SubTaskName:/.*GEN.*/ AND (NOT WMAgent_SubTaskName:/.*DIGI.*/) AND (NOT WMAgent_SubTaskName:/.*SIM.*/) AND (NOT WMAgent_SubTaskName:/.*RECO.*/) AND (NOT WMAgent_SubTaskName:/.*AOD.*/) AND (NOT WMAgent_SubTaskName:/.*MINIAOD.*/)"
            #"query": "Type:production AND Status:Completed AND Campaign:\"RunIISummer19UL17GEN\""
            #"query": "Type:production AND Status:Completed AND Campaign:\"RunIISummer19UL17wmLHEGEN\""
            #"query": "Type:production AND Status:Completed AND Campaign:\"RunIIFall17GS\""
          }
        }
      ]
    }
  },
  "aggs": {
    "agg_campaign": {
      "terms": {
        "field": "Campaign",
        "size": 500000,
        "order": {
          "_key": "asc"
        },
        "min_doc_count": 1
      },
      "aggs": {
        "agg_sub_task_name": {
          "terms": {
            "field": "WMAgent_SubTaskName",
            "size": 500000,
            "order": {
              "_key": "asc"
            },
            "min_doc_count": 1
          },
          "aggs": {
            "agg_sum_of_HS06CoreHr": {
              "sum": {
                "field": "HS06CoreHr"
              }
            }
          }
        }
      }
    }
  }
}


payload = json.dumps(payload_index_props) + " \n" + json.dumps(payload_query) + "\n"


headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <TOKEN>'
}

response = requests.request("POST", url, headers=headers, data = payload)
result = requests.request("POST", url, headers=headers, data = payload).json()

#print(response.text.encode('utf8'))

list_prepid_hs06 = []
for response in result["responses"]:
    for campaign in response["aggregations"]["agg_campaign"]["buckets"]:
        for sub_task in campaign["agg_sub_task_name"]["buckets"]:
            #print("Campaign: " + campaign["key"] + " SubTask: " + sub_task["key"], " ")
            #print("SubTask: ",str(sub_task["key"]).split("/")[2]," HS06CoreHr", sub_task["agg_sum_of_HS06CoreHr"]["value"])
            newtuple = str(sub_task["key"]).split("/")[2]+" = "+str(sub_task["agg_sum_of_HS06CoreHr"]["value"])
            if "GEN" in newtuple:
            	list_prepid_hs06.append(newtuple)
#        for sub_task in campaign["agg_sub_task_name"]["buckets"]:

grouped={}
for x in list_prepid_hs06:
    key = x.partition('_')[0]
    grouped.setdefault(key,[]).append(x)
grouped=grouped.values()
final_sum_for_campaign = 0
for x in grouped:
    total_hs06 = 0
    for y in x:
        listtmp = y.split(" = ")
        total_hs06 += float(listtmp[1])
        print(y)
    print("total Hs06(hr)=",total_hs06)
    print("----------------------------------------------------------------------------")
    final_sum_for_campaign += total_hs06
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Total HS06(hr) for the GEN campaign = ",final_sum_for_campaign)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
