from xml.dom.minidom import parseString

data = ''
with open('AndroidManifest.xml','r') as f:
    data = f.read()
dom = parseString(data)
activities = dom.getElementsByTagName('activity')
receivers = dom.getElementsByTagName('receiver')
perms = dom.getElementsByTagName('uses-permission')
services = dom.getElementsByTagName('service')


for activity in activities:
    print activity.getAttribute('android:name')
    intents = activity.getElementsByTagName('intent-filter')
    for intent in intents:
        actions = intent.getElementsByTagName('action')
        print intent
        for action in actions:
            if  action.getAttribute('android:name') == 'android.intent.action.MAIN':
                print action.getAttribute('android:name')
            else:
                print action.getAttribute('android:name')

for perm in perms:
    print perm.getAttribute('android:name')
    
for service in services:
    print service.getAttribute('android:name')
    
for receiver in receivers:
    print receiver.getAttribute('android:name')
