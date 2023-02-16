#write a program to list all odd nmumbers from 1-100
print("the below are odd numbers")
for odd_numbers in range (1,101) : 
    if(odd_numbers%2 !=0)  :
        print(odd_numbers)

#Write a program to list all even numbers from 1-100
print("the values below are even numbers")
for even_numbers in range(1-101) :
    if(even_numbers%2 ==0) :
        print(even_numbers)
        
#write a programme to list all prime number from 1-100
print("the values below are prime numbers")
for prime_numbers in range(1-101) :
    if prime_numbers  > 1:
        for i in range(2, prime_numbers):
            if(prime_numbers%i) ==0 :
                 break
            else :
                print(prime_numbers)

#Write a programme to calculate arithmetic progression of number from 1-10
#formula n=nth term in the sequence,a=first term,d=common difference
#Ap=a+(n-1)d

