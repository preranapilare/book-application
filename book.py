import json, os

FILE = "contacts.json"

def load(): return json.load(open(FILE)) if os.path.exists(FILE) else {}
def save(data): json.dump(data, open(FILE, "w"), indent=2)

def add():
    n = input("Name: "); p = input("Phone: "); e = input("Email: "); a = input("Address: ")
    c = load(); c[n] = {"phone": p, "email": e, "address": a}; save(c); print("✅ Added!")

def view():
    c = load()
    if not c: return print("No contacts yet.")
    for n, i in c.items(): print(f"{n}: {i['phone']} | {i['email']} | {i['address']}")

def search():
    q = input("Search name/phone: ").lower()
    for n, i in load().items():
        if q in n.lower() or q in i['phone']:
            print(f"🔍 {n}: {i['phone']} | {i['email']} | {i['address']}")
            return
    print("❌ Not found.")

def update():
    c = load(); n = input("Name to update: ")
    if n not in c: return print("❌ Not found.")
    i = c[n]
    c[n] = {"phone": input(f"Phone ({i['phone']}): ") or i['phone'],
            "email": input(f"Email ({i['email']}): ") or i['email'],
            "address": input(f"Address ({i['address']}): ") or i['address']}
    save(c); print("✅ Updated!")

def delete():
    c = load(); n = input("Name to delete: ")
    if n in c: c.pop(n); save(c); print("🗑️ Deleted!")
    else: print("❌ Not found.")

while True:
    print("\n1.Add 2.View 3.Search 4.Update 5.Delete 6.Exit")
    ch = input("Choose: ")
    if ch == "1": add()
    elif ch == "2": view()
    elif ch == "3": search()
    elif ch == "4": update()
    elif ch == "5": delete()
    elif ch == "6": break
    else: print("⚠️ Invalid!")