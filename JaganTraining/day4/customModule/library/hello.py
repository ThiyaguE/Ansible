#!/usr/bin/python

from ansible.module_utils.basic import *;

class Hello:
    def sayHello(self): 
        return 'Hello Ansible Module !'

def main():
    module = AnsibleModule (argument_spec = dict ())
    hello = Hello()
    result = {"Result": hello.sayHello()}
    module.exit_json (changed=False, meta=result)
main()
