import random
from collections import Counter

def gen_birthdays(N):
    days = [str(i) for i in range(1, 32)]
    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    birthdays = []
    for i in range(N):
        d = random.randrange(1, 31)
        m = random.randrange(1, 12)
        bthday = f"{months[m]} {days[d]}"
        
        birthdays.append(bthday)
    return birthdays


num_iteration = 100_000
n = 70
global_counter = 0

def main():
    global num_iteration
    global n
    global global_counter

    print(f"\n" + "*"*90)
    print(f"\nBirthday Paradox")
    print(f"\n" + "*"*90)
    for i in range(num_iteration):
        counter = 0
        brthdys = gen_birthdays(n)
        brthdays_counter = Counter(brthdys).values()
        for j in brthdays_counter:
            if j > 1 :
                counter += 1
        if i % 10000 == 0:
            print(f"\nInteration #{i}: {counter} have the same birthday")
    
        if counter > 0:
            global_counter += 1

    print(f"\n" + "*"*90)
    print(f"\nResult : {(global_counter / num_iteration) * 100}%")
    print(f"\n" + "*"*90)


if __name__ == "__main__":
    main()