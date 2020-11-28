import json

data = {'people': []}
data['people'].append({
    'name': 'Scott',
    'website': 'starbucks.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})

for r in data['people']:
    print('Name: ' + r['name'])
    print('Website: ' + r['website'])
    print('From: ' + r['from'])

f = open('data_file.json', 'a')
with f as outfile:
    print(json.dumps(data, indent=4), file=f)
f.close()

f = open('data_file.json', 'r')
with f as json_file:
    data_file = json.load(json_file)
f.close()

for p in data_file['people']:
    data['people'].append({
        'name': p['name'],
        'website': p['website'],
        'from': p['from']
    })

print('=========================')
for z in data['people']:
    print('Name: ' + z['name'])
    print('Website: ' + z['website'])
    print('From: ' + z['from'])

f = open('data_file.json', 'w')
with f as outfile:
    json.dump(data, outfile)
f.close()
