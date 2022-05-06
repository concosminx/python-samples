"""
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

print(long_timers)
"""

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
friends_last_seen = dict(zip(friends, time_since_seen))
print(friends_last_seen)

friends = ["Rolf", "Bob", "Jen"]
for counter, friend in enumerate(friends, start=1):
    print(counter)
    print(friend)

print(list(enumerate(friends))) 
print(list(zip([0,1,2], friends)))
print(dict(enumerate(friends)))

