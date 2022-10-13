# 1. import 패키지.모듈
import unit.character as c

c.test()

# 2. from 패키지 import 모듈
from unit import item as i

i.test()

# 3. from 패키지 import *
from unit import *

character.test()
monster.test()
item.test()

#  4. import 패키지
import unit as u
u.character.test()
