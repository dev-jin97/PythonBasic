# 변수
# 변수이름 = 데이터

# 리그오브레전드 
# 마스터이 챔피언 데이터를 변수에 저장
champ_name = "Master Lee"
champ_level = 5
champ_health = 800
champ_attack = 90

# Before
print(champ_name, champ_level, champ_health, champ_attack) # 변수 안에 저장되어 있는 데이터를 출력한다.

# 변수에 저장된 데이터를 변경하기
champ_level = champ_level + 1 # champ_level += 1
champ_health = champ_health + 200 # champ_health += 200
champ_attack = 100

# After
print(champ_name, champ_level, champ_health, champ_attack) # 변경된 데이터를 기반으로 출력한다.
