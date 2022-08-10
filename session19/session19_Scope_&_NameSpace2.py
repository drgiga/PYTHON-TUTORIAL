class AAA:
    def master(self):
        def do_local():
            myVariable = "local"
            print(myVariable)

        def do_nonlocal():
            nonlocal myVariable
            myVariable = "nonlocal"
            print(myVariable)

        def do_global():
            global myVariable
            myVariable = "global"
            print(myVariable)

        myVariable = "'my new value'"
        # print("-----------------------------------")
        # do_local()
        # print("After local assignment:", myVariable)
        # print("-----------------------------------")
        # do_nonlocal()
        # print("After nonlocal assignment:", myVariable)
        print("-----------------------------------")
        do_global()
        print("After global assignment:", myVariable)

class BBB:
    def master(self):
        def do_local():
            myVariable = "local"
            print(myVariable)

        def do_nonlocal():
            nonlocal myVariable
            myVariable = "nonlocal"
            print(myVariable)

        def do_global():
            global myVariable
            myVariable = "global"
            print(myVariable)

        myVariable = "'my new value'"
        print("-----------------------------------")
        do_local()
        print("After local assignment:", myVariable)
        print("-----------------------------------")
        do_nonlocal()
        print("After nonlocal assignment:", myVariable)
        print("-----------------------------------")
        do_global()
        print("After global assignment:", myVariable)

AAA().master()
print("*****************************************")
BBB().master()
# print("In global scope:", myVariable)