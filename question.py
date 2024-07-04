regex_pattern = r"^(([IVXCDM])\2{,2}(?!\2)|(L)(?!\3))*$"

import re
print(str(bool(re.match(regex_pattern, input()))))