import requests


r0 = requests.get("http://127.0.0.1:5000")

# Passing in an example latitude and longitude...

r1 = requests.get("http://127.0.0.1:5000/weather?latitude=22&longitude=88")


def function(r0, r1, r2):
    if r0.status_code == 200 and r1.status_code == 200 and r2.status_code == 400 :
        print("0")
        return 0
    else:
        print("-1")
        return -1



if __name__ == '__main__':
    function(r0, r1, r2)
