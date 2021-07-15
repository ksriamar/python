user = {'sriamar': {'first': 'sriamar', 'last': 'koganti', 'location': 'vizag',}, 'nitesh': {'first': 'nitesh', 'last': 'kesamneni','location': 'hyd', }}
for username, user_info in user.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())