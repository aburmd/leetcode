"""
Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).



Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.


Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.


Follow up:

If this function is called many times, how would you optimize it?
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        x=0
        while n!=0:
            if n&1==1: #Check if the last bit is 1 or zero
                x+=1 #count if last bit is 1
            n=n>>1 #shift 1 bit to right side
        return x


"""
FirstCommit:
Runtime: 28 ms, faster than 71.90% of Python3 online submissions for Number of 1 Bits.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of 1 Bits.
"""