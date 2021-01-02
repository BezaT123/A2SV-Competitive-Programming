def bonAppetit(bill, k, b):
    false_case=False
    if len(bill)<2 or len(bill)>10**5:
        false_case=True
    if k<0 or k>=len(bill):
        false_case=True
    if b<0:
        false_case=True
    
    actual_charge = 0
    if not false_case:
        for i in range (0,len(bill)):
            if bill[i]<0 or bill[i]>10**4:
                continue
            if i==k:
                continue
            actual_charge+=bill[i]
        actual_charge=actual_charge//2
        if b == actual_charge:
            print("Bon Appetit")
        else:
            print(b-actual_charge)