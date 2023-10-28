jobs = [
    {
        "id": 1,
        "content": "fırın ısıt",
        "time": 10,
        "busy": False,
        "preq": []
    },
    {
        "id": 2,
        "content": "hamur yap",
        "time": 15,
        "busy": True,
        "preq": []
    },
    {
        "id": 3,
        "content": "Hamuru soğut",
        "time": 30,
        "busy": False,
        "preq": [2]
    },
    {
        "id": 4,
        "content": "İç harc hazırla",
        "time": 15,
        "busy": True,
        "preq": []
    },
    {
        "id": 5,
        "content": "Hamur ve iç harc birleştir",
        "time": 20,
        "busy": True,
        "preq": [3, 4]
    },
    {
        "id": 6,
        "content": "Fırını koy",
        "time": 20,
        "busy": False,
        "preq": [1, 5]
    },
    {
        "id": 7,
        "content": "Servis et",
        "time": 1,
        "busy": True,
        "preq": [1]
    },
]

counter = 0
biggerthanzero = 0
stepcounter = {}

def preq(job):
    global counter
    global stepcounter
    if job['busy']:
        counter += job['time']
        stepcounter[job['id']] = 0
        for i in stepcounter.keys():
            if not stepcounter[i] == stepcounter[job['id']]:
                stepcounter[i] -= job['time']
                if stepcounter[i] < 0:
                    stepcounter[i] = 0
    else:
        stepcounter[job['id']] = job['time']

def main():
    global counter
    global stepcounter
    global biggerthanzero
    global jobs
    for job in jobs:
        if not job["preq"]:
            preq(job)
        else:
            for i in stepcounter.keys():
                if stepcounter[i] > biggerthanzero:
                    biggerthanzero = stepcounter[i]
                    counter += biggerthanzero
            preq(job)


if __name__ == "__main__":
    main()
    print(counter)
