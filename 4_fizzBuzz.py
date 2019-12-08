class Solution(object):
    #Regular Approach
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        z=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                z.append("FizzBuzz")
            elif i%3==0:
                z.append("Fizz")
            elif i%5==0:
                z.append("Buzz")
            else:
                z.append(str(i))
        return z
    #Efficient Approach
    def fizzBuzz1(self,n):
        combo={3:'Fizz',5:'Buzz'}
        #Can be added any combination in a easyway
        #combo={3:'Fizz',5:'Buzz',7:'Jazz'}
        ans=[]
        for i in range(1,n+1):
            nums_ans_str=''
            for key in combo.keys():
                if i%key==0:
                    nums_ans_str+=combo[key]
            if not nums_ans_str:
                nums_ans_str=str(i)
            ans.append(nums_ans_str)
        return ans
