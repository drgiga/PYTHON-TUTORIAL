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
        print("-----------------------------------")
        do_local()
        do_nonlocal()
        do_global()
        print("*****************************************")
        print("1:",do_local(),myVariable)
        print("2:",do_nonlocal(),myVariable)
        print("3:",do_global(),myVariable)
        print(myVariable)
print("*****************************************")
obj = AAA().master()
print("*****************************************")
print(obj)
