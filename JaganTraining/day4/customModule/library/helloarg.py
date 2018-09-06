#!/usr/bin/python

from ansible.module_utils.basic import *;

class Hello:
    def sayHello(self,msg): 
        return msg

def main():
    module = AnsibleModule (argument_spec = dict (
        message = dict (required=True, type='str')
        ))
    hello = Hello()
    msg=module.params['message']
    result = {"Result": hello.sayHello(msg)}
    module.exit_json (changed=False, meta=result)
main()
