import module_one as m_one
from module_one import print_name as p_name
import math

print(type(m_one))
print(dir(m_one))

m_one.print_name("Damian")
p_name("Kinga")
# help("modules")
# help("time")
print(dir(math))
