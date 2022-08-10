def scope_test():
    def do_local():
        myVariable = "local"

    def do_nonlocal():
        nonlocal myVariable
        myVariable = "nonlocal"

    def do_global():
        global myVariable
        myVariable = "global"

    myVariable = "test spam"
    do_local()
    print("After local assignment:", myVariable)
    do_nonlocal()
    print("After nonlocal assignment:", myVariable)
    do_global()
    print("After global assignment:", myVariable)

scope_test()
print("In global scope:", myVariable)