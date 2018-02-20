import json
import pprint
import requests
from couchbase.bucket import Bucket
import hashlib
import time
from couchbase.exceptions import NotFoundError
import csv

cb = Bucket("couchbase://cbs1.local/fp")

def createCampaign(campaignName):
    endPoint = "http://localhost:8080/FPRest/campaign/create"

    campaignPayload =  {
      "name": "cc",
      "lastEdited":23456789,
      "startDate" : "11/13/2017",
      "endDate" : "12/13/2017",
      "campaignDuration": 30,
      "type": {
        "id": "campaigntype:Activate"
      },
      "tags": ["tagA","tagB","tagC"]
    }

    campaignPayload["name"] = campaignName
    headers = {"Content-Type": "application/json"}
    response = requests.request(method="POST",url=endPoint,data=json.dumps(campaignPayload),headers=headers).json()
    print("Create Campaign Response")
    pprint.pprint(response)
    campaignObject = {"id" : response["entity"]["metaData"]["id"],
                      "name" : campaignName}

    return campaignObject

def createSegment(segmentName):
    endPoint = "http://localhost:8080/FPRest/segment/create"
    segmentPayload = {
        "name": "ss",
        "lastEdited": 12123111000,
        "tags": ["A/B", "Email"],
        "parentSegmentId": "",
        "filters": [
      {
        "field": "account_subscriber_status",
        "operation": "=",
        "operand": {
          "value": "ACTIVE"
        },
        "joinCondition": ""
      },
      {
        "field": "bundle_plan_name",
        "operation": "=",
        "operand": {
          "value": "Premium 2GB LTE Unlimited"
        },
        "joinCondition": "and"
      },
      {
        "field": "voice_plan_name",
        "operation": "=",
        "operand": {
          "value": "Unlimited Talk and Text"
        },
        "joinCondition": "and"
      },
      {
        "field": "businessUnit",
        "operation": "=",
        "operand": {
          "value": "SIMVOICE"
        },
        "joinCondition": "and"
      },
      {
        "field": "groupType",
        "operation": "=",
        "operand": {
          "value": "CONSUMER"
        },
        "joinCondition": "and"
      }
    ]
    }
    segmentPayload["name"] = segmentName

    headers = {"content-type": "application/json"}

    response = requests.request(method="POST", url=endPoint, data=json.dumps(segmentPayload), headers=headers).json()
    print("Create Segment Response")
    pprint.pprint(response)
    segmentObject = {"id": response["entity"]["metaData"]["id"],
                      "name": segmentName}

    return segmentObject

def createChannel(channelName):
    endPoint = "http://localhost:8080/FPRest/channel/create"

    channelPayload = {

        "channelName":"sms"

        }
    channelPayload["channelName"] = channelName

    headers = {"content-type": "application/json"}

    response = requests.request(method="POST", url=endPoint, data=json.dumps(channelPayload), headers=headers).json()
    channelObject = {"id": "channel:"+channelName.replace("_",""),
                     "name": channelName}

    return channelObject

def createTemplate(templateName):

    endPoint = "http://localhost:8080/FPRest/templates/create"

    templatePayload = {

        "templateName": "tt"

    }
    templatePayload["templateName"] = templateName

    headers = {"content-type": "application/json"}

    response = requests.request(method="POST", url=endPoint, data=json.dumps(templatePayload), headers=headers).json()
    templateObject = {"id": "templates:" + templateName.replace("_",""),
                     "name": templateName}

    return templateObject

def generateHashValueForCampaignInstanceId(campaignInstanceIdName):
    hashM = hashlib.md5(campaignInstanceIdName.encode("utf-8"))
    hashV = hashM.hexdigest()
    print("campaignInstanceIdName====",campaignInstanceIdName)
    print("hashV=====",hashV)
    return hashV

def createCampaignInstance(campaignInstanceIdName,campaignResObj,segmentResObj,channelResObj,templateResObj):

    docid = "campaigninstance:"+campaignInstanceIdName
    print("hashValue====",docid)

    campaignInstancePayload = {
        "data": {
            "campaign" : campaignResObj,
            "segment" : segmentResObj,
            "channel" : channelResObj,
            "templates" : templateResObj
        },
        "metaData": {
            "id": docid,
            "objectType": "campaigninstance",
            "creationTime": int(round(time.time() * 1000)),
            "lastUpdateTime": int(round(time.time() * 1000)),
            "valid": True,
            "deleted": False
        }

    }

    cb.insert(docid,campaignInstancePayload)

def getCampaign(campaignName):

    response = requests.request("GET",url="http://localhost:8080/FPRest/campaign/getByName/"+campaignName).json()
    print("Campaign Response")
    pprint.pprint(response)
    returnObj = {"id" : response["entity"]["metaData"]["id"],
                 "name" : campaignName}
    return returnObj

def getSegment(segmentName):

    response = requests.request("GET", url="http://localhost:8080/FPRest/segment/getByName/" + segmentName).json()
    print("Segment Response")
    pprint.pprint(response)
    returnObj = {"id": response["entity"]["metaData"]["id"],
                 "name": segmentName}

    return returnObj


if __name__ == '__main__':

    uniqueCampaignInstanceIdsListFile = "CIID_NEW.csv"
    uniqueCampaignInstanceIdsList = []
    # with open(uniqueCampaignInstanceIdsListFile,"r") as inf:
    #     for line in inf:
    #         print('line===',line)
    #         uniqueCampaignInstanceIdsList.append(line.strip("\n").strip())
    # print(len(uniqueCampaignInstanceIdsList))
    # pprint.pprint(uniqueCampaignInstanceIdsList)
    #uniqueCampaignInstanceIdsList = list(filter(None,uniqueCampaignInstanceIdsList))
    #uniqueCampaignInstanceIdsList = ["AllSubsUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-US_FreeMotoEendofsummer_082217"]
    uniqueCampaignInstanceIdsList = ["AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_092717",
                                     "AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_091817",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_080117",
                                     "AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_092617",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_080217",
                                     "AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_091517",
                                     "AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_092517",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_080417",
                                     "AllSubsUpsell-ESALL_FreeOrPaid_AnyDataUsage-EMAIL-ES_6-12mPrePayPromo_091917",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_072617",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_072717",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_080317",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-MotoE-kids_071917",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_072817",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-MotoE-kids_072017",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_072517",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-MotoE-kids_071817",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-US_Pre-MemorialDayPromos_Trial_051617",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_073117",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-MotoE-kids_071717",
                                     "AllSubUpsell-USALL_FreeOrPaid_AnyDataUsage-EMAIL-LGTributePriceDrop-r850_072417"]
    # with open("ciid.csv", newline='') as f:
    #     reader = csv.reader(f)
    #     for row in reader:
    #         uniqueCampaignInstanceIdsList.append(row[0])
    # print(len(uniqueCampaignInstanceIdsList))
    #pprint.pprint(uniqueCampaignIdsList)
    # print(len(uniqueCampaignInstanceIdsList))
    campaignList = []
    segmentList = []
    channelList = []
    templateList = []
    ambiguousCampaignInstanceIdsList = []
    i=0
    for campaignInstanceId in uniqueCampaignInstanceIdsList:
        print("i===",i)
        print("campaignInstanceId===",campaignInstanceId)
        #if(bucket.get(campaignInstanceId)!=None):
        try:
            existing_doc = cb.get(key=campaignInstanceId).value
            print("campaignExist=",campaignInstanceId)
            flag="false"
        except NotFoundError:
            flag="true"
        if len(campaignInstanceId.split("-")) == 5 and flag=="true":
            campaignName = campaignInstanceId.split("-")[0]
            print("campaignName===", campaignName)
            # if campaignName not in campaignList:
            #     campaignResObj = createCampaign(campaignName=campaignName)
            #     campaignList.append(campaignName)
            # else:
            campaignResObj = getCampaign(campaignName)

            segmentName = campaignInstanceId.split("-")[1]
            print("segmentName===", segmentName)
            # if segmentName not in segmentList:
            #     segmentResObj = createSegment(segmentName=segmentName)
            #     segmentList.append(segmentName)
            # else:
            segmentResObj = getSegment(segmentName)

            channelName = campaignInstanceId.split("-")[2]
            print("channelName===", channelName)
            if channelName not in channelList:
                channelResObj = createChannel(channelName=channelName)
                channelList.append(channelName)
            else:
                channelResObj = {
                    "id" : "channel:"+channelName.replace("_",""),
                    "name" : channelName
                }

            templateName = campaignInstanceId.split("-")[3]+"-"+campaignInstanceId.split("-")[4]
            print("templateName===", templateName)
            if templateName not in templateList:
                templateResObj = createTemplate(templateName=templateName)
                templateList.append(templateName)
            else:
                templateResObj = {
                    "id": "templates:" + templateName.replace("_", ""),
                    "name": templateName
                }

            createCampaignInstance(campaignInstanceId,campaignResObj,segmentResObj,channelResObj,templateResObj)

        else:
            ambiguousCampaignInstanceIdsList.append(campaignInstanceId)
        i+=1

    with open("ambiguousCampaignInstanceIdsList_AWS_New","w") as amb_out:
        json.dump(ambiguousCampaignInstanceIdsList,amb_out)