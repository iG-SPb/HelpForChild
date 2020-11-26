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

f = open('venv/Scripts/data_file.json', 'w')
with f as outfile:
    json.dump(data, outfile)
f.close()

f = open('venv/Scripts/data_file.json', 'r')
with f as json_file:
    data_file = json.load(json_file)

print(data_file)

for p in data_file['people']:
    data['people'].append({
        'name': p['name'],
        'website': p['website'],
        'from': p['from']
    })
f.close()

print('=========================')
for z in data['people']:
    print('Name: ' + z['name'])
    print('Website: ' + z['website'])
    print('From: ' + z['from'])

f = open('venv/Scripts/data_file.json', 'w')
with f as outfile:
    json.dump(data, outfile)
f.close()
