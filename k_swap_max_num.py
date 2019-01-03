import collections

class number_swaps:
    def find_indexes(self, num=0):
        num_str = str(num)
        length = len(num_str)
        dict = {}
        for i in range(0,length):
            digit = num_str[i]
            if i==0:
                dict[digit] = [i]
                continue
            if not dict.get(digit):
                dict[digit] = [i]
            else:
                val = dict.get(digit)
                val.append(i)
                dict[digit] = val
        od = collections.OrderedDict(sorted(dict.items())) #Creating a sorted and ordered dictionary to access the digits from highest to lowest
        return od

    def find_max(self, num=0, k_swaps=0):
        num_str = str(num)  # Processing number as string for easy swap
        length_num = len(num_str) #Calculate the length of the input number
        if k_swaps==0:
            print("Swap input is 0. No swap allowed")
            return
        if num==0:
            print("Number input is 0. Maximum Number is 0")
            return
        ind_dic = self.find_indexes(num) #Getting the dictionary with key as digits and values as a list of indexes
        l_keys = list(ind_dic.keys()) #Getting a list of keys/digits (of the number)
        digits = len(l_keys) #Calculating total number of digits in number
        max_dig = l_keys[digits-1]
        max_num = num_str #Creating a copy of the initial input to do changes on
        num_swaps = 0 #Keeping a count of swaps
        for i in range(0,length_num):
            if(num_swaps==k_swaps):
                break

            digit = max_num[i]

            if digit==str(max_dig): #if digit is already the max then no swap needed
                continue
            swapflag = False
            for j in range(digits-1,-1, -1): #Iterating in reverse to start checking from the highest digits
                if(swapflag):
                    break
                if(l_keys[j]<=digit): #If the next number (and remaining, if any) is less than the current digit no point in swapping
                    break
                indexes = ind_dic.get(l_keys[j]) #Getting the list of indexes of the digit
                indexes_copy = indexes.copy() #Making an index list copy to operate on
                l = len(indexes)
                for k in range(0,l):
                    if indexes_copy[k]<=i:
                        continue
                    elif(num_swaps+indexes[k]-i)<=k_swaps: #checking that the swap is less than max allowed swaps
                        max_num = max_num[0:i]+str(l_keys[j])+max_num[i+1:indexes[k]]+str(digit)+max_num[indexes[k]+1:]
                        num_swaps = num_swaps + indexes[k] - i
                        val = ind_dic.get(digit)
                        val.remove(i)
                        val.append(indexes[k])
                        val.sort()
                        ind_dic[digit] = val #Update the index list for the digit exchanged to right after the swap
                        indexes.remove(indexes_copy[k]) #Popping out the current index
                        ind_dic[j] = indexes
                        swapflag = True
                        break
                    else:
                        break
        return max_num

ns = number_swaps()

# print("Orginal Number : ", 9825462363467666912689362389632896438968961238963896238969)
# print("Maximum number for 50 swaps ",ns.find_max(9825462363467666912689362389632896438968961238963896238969, 50))
# print("Maximum number for 60 swaps ",ns.find_max(9825462363467666912689362389632896438968961238963896238969, 60))
# print("Maximum number for 70 swaps ",ns.find_max(9825462363467666912689362389632896438968961238963896238969, 70))
# print("Maximum number for 80 swaps ",ns.find_max(9825462363467666912689362389632896438968961238963896238969, 80))
# print("Maximum number for 90 swaps ",ns.find_max(9825462363467666912689362389632896438968961238963896238969, 90))
print("Orginal Number : ", 98259999)
print("Maximum number for 1 swaps ",ns.find_max(98259999, 1))
print("Maximum number for 2 swaps ",ns.find_max(98259999, 2))
print("Maximum number for 3 swaps ",ns.find_max(98259999, 3))
print("Maximum number for 4 swaps ",ns.find_max(98259999, 4))
print("Maximum number for 5 swaps ",ns.find_max(98259999, 5))
