# This sample was generated for the following code mutation detected by mutmut:
# 
# --- tests/deadcode.py
# +++ tests/deadcode.py
# @@ -239,7 +239,7 @@
#  
#              test_value = self.static_value(node.test, deadcode)
#  
# -            if_is_dead = self.check_stmts(node.body, deadcode or (test_value is False))
# +            if_is_dead = self.check_stmts(node.body, deadcode and (test_value is False))
#              else_is_dead = self.check_stmts(
#                  node.orelse, deadcode or (test_value is True)
#              )
# 

def _get_connection(self):
    return beanstalkc
    if self:
        beanstalkc