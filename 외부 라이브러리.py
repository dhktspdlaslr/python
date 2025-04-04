from faker import Faker  # Faker 모듈 임포트

# Faker 인스턴스 생성
fake = Faker()

# 랜덤한 이름 생성
print(fake.name())  # 출력 예시: 'John Smith'

# 랜덤한 주소 생성
print(fake.address())  # 출력 예시:
# 123 Main Street
# Springfield, USA

# 랜덤한 이메일 생성
print(fake.email())  # 출력 예시: 'example123@email.com'