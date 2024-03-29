# PYTHON PROJECT
# DERIVATIVE ADVANCE PROGRAM IN PYTHON

"""1] putting currect number of bracket in the proper sequence is the heart of this program 
   2] program may behave unexpectadely if not proper brackets are given 
   3] input should be in the form of currect input method
   4] the examples are given for this refrence purpose"""


 
"""i also uploaded this program at github
   check my python reposetary at github"""

# my github link : https://github.com/rodeatharva1000

# DEFINING THE MAIN CLASS
class Derivative :

    # CLASS VARIABLES
    inp = None
    ans = None
    
    # CLASS CONSTRUCTOR FOR Derivative CLASS
    def __init__(self,catagory_inp) :
            self.inp = catagory_inp
            if self.inp == "-" :
                self.ans = " ] - [ "
                self.print_ans()
            else :
                self.remove_minus()
                self.check_inp()
    
    # PRINTING ANSWER
    def print_ans(self) :
        print(self.ans, end = " ") 
        
    
    # REMOVING MINUS 
    def remove_minus(self) :
        if self.inp == "-" :
            pass
        else :
            count_minus = self.inp.count("-")
            inp_replace = self.inp.replace("-","")
            self.inp = inp_replace
            self.ans = count_minus*"(-)"
            self.print_ans() 



    def seperate_constant(self) :
        cons_var_list = self.inp.split(".") 
        print(cons_var_list[0], end = "." )
        self.inp = cons_var_list[1]
        self.check_inp()

# example : 33.sin(90x)
    
    
    # CHECKING INPUT (CONSIDERING BOTH CLASSES)
    def check_inp(self) :
        if self.inp == "+" :
            self.ans = " ] + [ "
            self.print_ans()
        if "." in self.inp :
            self.seperate_constant()
        elif self.inp == "-" :
            pass
        elif self.inp == "/" :
            self.ans = "/"
            self.print_ans()
        elif self.inp.startswith("sin(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sin()
        elif self.inp.startswith("cos(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cos()
        elif self.inp.startswith("tan(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.tan()
        elif self.inp.startswith("cot(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cot()
        elif self.inp.startswith("sec(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.sec()
        elif self.inp.startswith("cosec(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.cosec()
        elif self.inp.startswith("log(") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.log()
        elif self.inp.startswith("e^") :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.exponential()
        elif "/" and ")^" in self.inp : 
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.twwo_in()
        elif "/" in self.inp :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.one_by_x()
        elif ")^" in self.inp :
            if "x" not in self.inp :
                self.ans = "0"
                self.print_ans()
            else :
                self.x_race_to_n()   
        elif not self.inp.isdigit() :
            self.nx()
        elif self.inp.isdigit() :
            self.constant()

    def twwo_in(self) :
        if self.inp.startswith("(") :
            self.x_race_to_n()    
        elif not self.inp.startswith("(") :
            self.one_by_x()
    
    # SIN(TRIGO) FUNCTION
    def sin(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"cos({str})")
            self.print_ans()
            if self.ans != "cos(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : sin(90x) , sin(cos(90x))

    # COS(TRIGO) FUNCTION
    def cos(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-sin({str})")
            self.print_ans()
            if self.ans != "-sin(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : cos(tan(90x))
    
    # TAN(TRIGO) FUNCTION
    def tan(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"sec^({str})")
            self.print_ans()
            if self.ans != "sec^(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : tan(sin(90x))

    # COT(TRIGO) FUNCTION
    def cot(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-cosec^({str})")
            self.print_ans()
            if self.ans != "-cosec^(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass

 # example : cot(sec(90x)) 

    # SEC(TRIGO) FUNCTION
    def sec(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"sec({str})*tan({str})")
            self.print_ans()
            if self.ans != "sec(x)*tan(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass

# example : sec(tan(cosec(90x))) 

    # COSEC(TRIGO) FUNCTION
    def cosec(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"-cosec({str})*cot({str})")
            self.print_ans()
            if self.ans != "-cosec(x)*cot({str})" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : cosec(tan(90x))   
    
    
    # LOG FUNCTION
    def log(self) :
        find = self.inp.find("(")
        list = []
        for i in range(find+1,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None
        for i in list :
            str = "".join(list)
        if str.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"1/{str}")
            self.print_ans()
            if self.ans != "1/x" :
                self.inp = str
                self.check_inp()
            else :
                pass
    
# example : log(sin(90x))

    # N(X) FUNCTION
    def nx(self) :
        str = self.inp.replace("x","(1)")
        self.ans = str
        self.print_ans()
         
        
    # ABOUT CONSTANT
    def constant(self) :
        self.ans = "0"
        self.print_ans()


# example : 33 , 43     
    
    
    # EXPONENTIAL FUNCTION
    def exponential(self):
        find = self.inp.find("e")
        list = []
        for i in range(find+3,len(self.inp)-1) :
            list.append(self.inp[i])
        str = None	
        for i in list  :
            str = "".join(list)
        if str.isdigit() :
            ans = 0
            self.print_ans()
        elif not str.isdigit():
            self.ans = (f"e^({str})")
            self.print_ans()
            if self.ans != "e^(x)" :
                self.inp = str
                self.check_inp()
            else :
                pass

 # example : e^(cos(90x))   
    
    
    # 1/X FUNCTION
    def one_by_x(self) :
        find = self.inp.find("/")
        find_second = self.inp.find("(")
        
        list = []
        list_second = []
        list_third = []
        str = None
        str_second = None
        str_third = None
        
        for i in range(0,find) :
            list.append(self.inp[i])
        for i in list :
            str = "".join(list)
        
        
        for i in range(find_second+1,len(self.inp)-1) :
            list_second.append(self.inp[i])        
        for i in list_second : 
            str_second = "".join(list_second)

        
        for i in range(find+1,find_second) :
            list_third.append(self.inp[i])        
        for i in list_third : 
            str_third = "".join(list_third)

        
        if str_second.isdigit() :
            self.ans = 0
            self.print_ans()
        elif not str_second.isdigit():
            self.ans = (f"-{str}/{str_third}({str_second})^2")
            self.print_ans()
            if self.ans != "-1/(x)^2" : 
                self.inp = str_second
                self.check_inp() 
            else :
                pass


# example : 1/(x) , 22/44(cos(90x))
    
    
    
    # VARIABLE RACE TO CONSTANT (Root functions also includes here)
    def x_race_to_n(self): 
        find = self.inp.find(")^")
        find_second = self.inp.find("^(")
        list = []
        list_second = []
        str = None
        str_second = None
        
        
        for i in range(1,find) :
            list.append(self.inp[i])	
        for i in list :
            str = "".join(list)

        for i in range(find_second+2,len(self.inp)-1) :
            list_second.append(self.inp[i])	
        for i in list_second :
            str_second = "".join(list_second)
        
        if str.isdigit() :
            self.ans = "0" 
            self.print_ans()

        elif not str.isdigit() : 
            self.ans = (f"{str_second}.{str}^{int(str_second)-1}")
            self.print_ans()
            if "(x)^" not in self.inp :
                self.inp = str
                self.check_inp()
            else :
                pass         

# example : (sin(cos(90x)))^(67)



# FINDING AND APPLYING CATYAGORY FOR 2 (U AND V) FUNCTIONS


class Catagory :

    # CATAGORY CLASS VARIABLES
    
    main_inp = None
    main_ans = None 
    
   
     # PRINTING MAIN ANSWER
    def print_main_ans(self) :
        print(self.main_ans , end = " ")
    
    
    # FOR SPECIAL ANSWER OF DIVIDION
    def print_main_division_ans(self) : 
        print(f"[({self.main_ans})^2]")
    
    
    # CLASS CONSTRUCTOR FOR Catagory CLASS
    def __init__(self) : 
        print("-------------------------------------------------")
        self.main_inp = input("Enter the function : ")
        self.main_inp = self.main_inp.replace(" ","")
        self.main_inp = self.main_inp.lower()
        print("")
        print(f" (d/dx) of {self.main_inp} is ")
        self.check_main_inp()
    
    
    
    # CHECKING MAIN INPUT
    def check_main_inp(self) :
        if "+" in self.main_inp :
            self.plus()
        elif "*" in self.main_inp :
            self.product()  
        elif ")/" in self.main_inp : 
            self.division()   
        elif ")-" in self.main_inp :
            self.minus()
        else :
            obj = Derivative(self.main_inp)

    
    # FUNCTION OF PLUS
    def plus(self) :
        plus_list = self.main_inp.split("+")
        plus_list.append("+")
        plus_list[1] , plus_list[2] = plus_list[2] , plus_list[1]
        
        
        print("[  ", end = "" )
        for object in range(0,len(plus_list)) :
            obj = Derivative(plus_list[object])
        print("  ]", end = "" )

    
    # FUNCTION OF MINUS
    def minus(self) : 
        if "-" in self.main_inp :
            count = self.main_inp.count("-")
            if count >= 2 :
                print(((count)-1)*"(-)",  end = " " ) 
                str = None
                list = []
                for item in self.main_inp :
                    list.append(item) 
                list.remove(list[0])
                for items in list :
                    str = "".join(list) 
                    self.main_inp = str
        minus_list = self.main_inp.split("-") 
        minus_list.append("-")
        minus_list[1] , minus_list[2] = minus_list[2] , minus_list[1]

        print("[  ", end = "" )
        for object in range(0,len(minus_list)) :
            obj = Derivative(minus_list[object])
        print("  ]", end = "" )
    
    
    
    # FUNCTION OF PRODUCT    
    def product(self) : 

        product_list = self.main_inp.split("*")
        product_list.append("+")
        product_list.append(product_list[0])
        product_list.append(product_list[1])
        
        print("[  ", end = "" )
        for object in range(0,len(product_list)) :   
            if object % 2 == 0 :
                obj = Derivative(product_list[object])
            else :
                self.main_ans = product_list[object]
                self.print_main_ans() 
        print("  ]", end = "" )        
        
       

    
    # FUNCTION OF DIVISION
    def division(self) :
        self.main_inp = self.main_inp.replace(")/","))/")
        division_list = self.main_inp.split(")/")
        division_list[0] , division_list[1] = division_list[1] , division_list[0]
        division_list.append("-")
        division_list.append(division_list[1])
        division_list.append(division_list[0])
        division_list.append("/")
        division_list.append(division_list[0])

        
        
        # FOR CREATING OBJECT ACCORDING TO LIST
        for object in range(0,len(division_list)) : 
            if object == 1 :
                obj = Derivative(division_list[object])
            elif object == 2 :
                obj = Derivative(division_list[object])
            elif object == 4 :
                obj = Derivative(division_list[object])
            elif object == 5 :
                print("  ] } ", end = "" )
                obj = Derivative(division_list[object])
            elif object == 0 :
                print(" { [  ", end = "" )
                self.main_ans = division_list[object]
                self.print_main_ans()
            elif object == 3 :
                self.main_ans = division_list[object] 
                self.print_main_ans() 
            elif object == 6 :
                self.main_ans = division_list[object] 
                self.print_main_division_ans()


print("0000000000[ WELCOME TO SOLVE@DERIVATIVE ]0000000000 \n1 } Enter The Function To Find Derivative ( limitaion till u and v )\n\n2 } Perfectly work for chain rule\n\n3 } Input according to the input methods is mandatory\n\n4 } Read instructions before using\n\n5 } Try provided examples to learn more about input methods \n")


while True :
    print(2*("\n"))
    obj = Catagory()


# EXAMPLES ON CATAGORIES :

# catagory (+) : sin(90x)+cos(90x)

# catagory (-) : sin(90x)-sin(tan(90x))

# catagory (*) : sin(90x)*sec(95x)

# catagory (/) : cosec(90x)/sec(90x)

# CREATING OBJECT OF CATAGORY CLASS

# program catagory - maths\calculus\derivatives
# work catagory - u+v / u-v / u.v | u/v
# code editor - visual studio (VS) code 
# language - python

# release : 30/03/2023
# last update : 16/04/23

# Developer - @ Rode Atharva Mahesh | on windows os

# for any queery  :  rodeatharva2@gmail.com
