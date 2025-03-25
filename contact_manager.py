import csv

def add_contact(name, phone, email):
    with open('contacts.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("✔️ Đã thêm liên hệ thành công.")

def view_contacts():
    try:
        with open('contacts.csv', mode='r') as file:
            reader = csv.reader(file)
            print("\n📒 Danh bạ:")
            for row in reader:
                print(f"Tên: {row[0]} | SĐT: {row[1]} | Email: {row[2]}")
    except FileNotFoundError:
        print("⚠️ Chưa có danh bạ nào.")

def search_contact(name_to_find):
    found = False
    with open('contacts.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if name_to_find.lower() in row[0].lower():
                print(f"🔍 Tìm thấy: {row[0]} | {row[1]} | {row[2]}")
                found = True
    if not found:
        print("❌ Không tìm thấy liên hệ.")

def main():
    while True:
        print("\n📱 MENU QUẢN LÝ DANH BẠ")
        print("1. Thêm liên hệ")
        print("2. Xem danh bạ")
        print("3. Tìm liên hệ")
        print("4. Thoát")

        choice = input("👉 Chọn chức năng (1-4): ")

        if choice == '1':
            name = input("Nhập tên: ")
            phone = input("Nhập số điện thoại: ")
            email = input("Nhập email: ")
            add_contact(name, phone, email)

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            name_to_find = input("Nhập tên cần tìm: ")
            search_contact(name_to_find)

        elif choice == '4':
            print("Tạm biệt! 👋")
            break

        else:
            print("❗ Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
