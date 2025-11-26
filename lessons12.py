def rps(p1, p2):
    if p1 == p2:
        return "Draw!"
    winning = { "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"}
    if winning[p1] == p2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
print(rps("scissors",     "paper" ))    





def is_palindrome(s):
    s= s.lower()
    return s ==s[::-1]




def sum_array(a):
    total = 0
    for  num in a :
        total += num
    return total        
print(sum_array([1,2,3]))


def quarter_of(month):
    return (month - 1)// 3 +1
print(quarter_of(3))




def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_years = 15
        dog_years =15
    elif human_years == 2:
        cat_years = 15 + 9
        dog_years = 15 + 9
    else:
        cat_years =   15 + 9 + (human_years - 2) * 4
        dog_years = 15 + 9 + (human_years - 2) * 5  
    return [ human_years, cat_years, dog_years]
        
print(human_years_cat_years_dog_years(1))


def make_negative( number ):
    return -abs(number)



def positive_sum(arr):
    total = 0
    for n in arr:
        if n > 0:
            total += n
    return total        

