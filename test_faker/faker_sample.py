from faker import Faker

# 日本語データを指定
fake = Faker(['ja-JP'])

# 確認用データの生成
print("--- Generate Fake Data ---")
print("name        : ", fake.name())
print("address     : ", fake.address())
print("company     : ", fake.company())
print("email       : ", fake.email())
print("phone number: ", fake.phone_number())

print("color", fake.color())
print("file", fake.jan())
print("emoji", fake.emoji())

fake_en = Faker(['en-US'])
print(fake_en.profile())