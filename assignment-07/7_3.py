'''
Name: Piyush Bajaj
Roll no: 24BIT181
Branch: Information and Communication Technology (ICT)
'''

# Dept-wise min and max salary
data = {
    101: {1: 25000, 2: 30000},
    102: {3: 40000, 4: 28000},
    103: {5: 35000, 6: 45000}
}

for dept in data:
    sals = list(data[dept].values())
    print("dept:", dept)
    print("min:", min(sals))
    print("max:", max(sals))
