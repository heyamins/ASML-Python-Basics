filename = '../Sandbox/ca-500.csv'

with open(filename, 'r') as f:
    headers = f.readline().strip().split(';')

    for line in f:
        line = line.strip()
        values = line.split(';')

        d = dict(zip(headers, values))

        if d['city'] in ('Montreal','Toronto'):
            print(f"{d['first_name']:16} {d['last_name']:16} {d['city']:16} {d['email']}")






        # d = dict(zip(headers, values))
        #
        # if d['city'] in ('Montreal', ):
        #     print(f"{d['first_name']:15} {d['last_name']:15} {d['city']:25} {d['email']:35}")
