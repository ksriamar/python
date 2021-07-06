def checkIfMatch(elem):
    if len(elem) == 5:
        return True;
    else :
        return False;
def main():
    
    listOfStrings = ['Hi' , 'hello', 'GM', 'GA', 'there', 'from']
    
    print(listOfStrings)
    
  #check if element exist in list using 'in'
    if 'GM' in listOfStrings :
        print("Yes, 'GM' found")
        
  #check if element NOT exist in list using 'in'
    if 'str' not in listOfStrings :
        print("Yes, 'str' NOT found")    
    
   #  check if element exist in list using count() function
    if listOfStrings.count('GM') > 0 :
        print("Yes, 'GM' found ")

   #  check if element exist in list based on custom logic
   #  Check if any string with length 5 exist in List
    result = any(len(elem) == 5 for elem in listOfStrings)
    if result:
        print("Yes")
    
   #   Check if any string that satisfies the condition in checkIfMatch() function  exist in List
    result = any(checkIfMatch for elem in listOfStrings)
    if result:
        print("Yes")
    
if __name__ == '__main__':
    main()