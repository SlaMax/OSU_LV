brojevi= []

while True:
    unos=input()
    unos=unos.lower()
    if unos=="done":
        break

    try:
        broj=float(unos)
        brojevi.append(broj)
    except:
        print("upišite broj ili done za završetak")

for br in brojevi:
    print(br)
