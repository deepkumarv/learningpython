class functioncalls:
    def first_function(self):
        print("In first function")
    def second_function(self):
        print("In second function")
        
        
functioncall_obj=functioncalls()
functioncall_obj.first_function()
functioncalls.second_function(functioncall_obj)
if hasattr(functioncall_obj, "number"):
    print("Yes")
else:
    print("No")