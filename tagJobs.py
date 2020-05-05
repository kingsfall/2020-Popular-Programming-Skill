textString = open('Output.txt','r').read()

textString = textString.lower().replace("-","").replace(" ","")

array = list(textString.split(",\'"))


tagObject = {
    "Full Stack Web developer" : ["fullstack", "rails", "django","node","react","php","ruby","AWS","cloud","LAMP"],
    "Back End" : ["backend","rails", "django","node", "mongodb","python","backend","ruby"],
    "Front End" : ["frontend","javascript", "wordpress","react","shopify","liquid","html","css","net","php","web"],
    "Dev ops" : ["devops","mulesoft","cloud","server"],
    "Native" : ["app", "android","ios","macos", "native","mobile"],
    "Data Science" : ["research","data","science","analyst","artificial","intelligence"]

}

countObject = {}
skillObject = {}
jobNotInList = []
def countJobs(arrayValue):
    bAdded = 0
    for keys in tagObject:  
        # countObject.update({keys:0})
        count = 0
        for values in tagObject[keys]:
            # print(values)
            if values in arrayValue:
                # print("match")
                count = count + 1
                if values not in skillObject:
                    skillObject[values] = 0
                skillObject[values] += 1
            
        
        if(count != 0):
            # print(keys)
            # print("plus one")
            if keys not in countObject:
                countObject[keys] = 0
            countObject[keys] += 1
            bAdded = 1
    if bAdded == 0:
        jobNotInList.append(arrayValue)


for arrayValue in array:
    countJobs(arrayValue)

# print(countObject)
# print(len(jobNotInList))


import matplotlib.pyplot as plt
import operator

data = skillObject
data = dict(sorted(data.items(), key=operator.itemgetter(1),reverse=True))
names = list(data.keys())
values = list(data.values())

fig, axs = plt.subplots(figsize=(60, 30))
axs.bar(names, values)
fig.suptitle('Skill Popularity')
plt.show()
