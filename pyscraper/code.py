
import pyrust
import json


def writetoJSON(path, filename, data) :
    pathfilenameext = path + '/' + filename + '.json'
    
    with open(pathfilenameext, 'w') as fp:
        json.dump(data, fp, indent=4)



url = "https://summerofcode.withgoogle.com/api/program/2022/organizations/"
# url = "https://summerofcode.withgoogle.com/programs/2022/organizations"



req_file = pyrust.request_url(url)

orgs = json.loads(req_file)

data = []


for org in orgs :
    org_dict = {}
    org_dict["name"]= org["name"]
    org_dict["topics"] = org["topic_tags"]
    org_dict["tagline"] = org["tagline"]
    org_dict["tech"] = org["tech_tags"]
    org_dict["fields"] = org["categories"]
    org_dict["guidance_link"] = org["contributor_guidance_url"]
    org_dict["brief"] = ( org["description"][slice(150)] + "..." )
    
    
    data.append(org_dict)
    

writetoJSON("C:/Users/Rohan/GitHubstuff/test_git/pyrust", "details", data)