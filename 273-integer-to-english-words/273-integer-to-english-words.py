"""
class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0:
            return "Zero"
        ans=[]
        def number(n):
            if n=="00":
                return ""
            if int(n)<20:
                return a[int(n)]
            else:
                if n[1]=="0":
                    return b[int(n[0])]
                return b[int(n[0])]+" "+a[int(n[1])]
            
            
        a=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        b=[None,None,"Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        c=["Thousand","Million","Billion"]
        num=str(num)

        num=num[::-1]

        n=len(num)
        i=0
        count=-1
        temp=""
        while i<n:
            temp=num[i]+temp
            if len(temp)==3:
                if count>-1:
                    ans.append(c[count])
                if temp[1:]=="00":
                    ans.append(a[int(temp[0])]+" Hundred")
                else:
                    ans.append(a[int(temp[0])]+" Hundred "+number(temp[1:]))
                count+=1
                temp=""
            i+=1
        if temp:
            if count>-1:
                ans.append(c[count])
            ans.append(number(temp))
        ans=ans[::-1]
        return " ".join(ans)
        
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        ## RC ##
        ## APPROACH : BRUTE FORCE ##
        ## Main intent of the interviewer when asked this question is , he is testing how you are handling the test cases and how elagantly you are using sub problems to get to the final solution ## (so focus on edge cases)
        ## 1. For a two digit number if there is no ones digit 20 -> twenty + " " (number generally), dont leave the space behind, use if else case with "" (empty). Similarly for 20,000 etc.
        
        one_digit = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        two_digit = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        
        def get_three_digit_num(num):
            if( not num ) : return ""
            if( not num// 100 ): return get_two_digit_num(num)
            return one_digit[ num // 100 ] + " Hundred" + ((" " + get_two_digit_num( num % 100 )) if( num % 100 ) else "")
        
        def get_two_digit_num( num ):
            if not num:
                return ''
            elif num < 10:
                return one_digit[ num ]
            elif num < 20:
                return two_digit[ num ]
                    # edge case 1
            return tens[ num//10 ] + ((" " + one_digit[ num % 10 ]) if( num % 10 ) else "")
        
        # edge case
        if(num == 0): return "Zero"
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        result = ''
        if billion:        
            result = get_three_digit_num(billion) + ' Billion'
        if million:
            # space only when prev result is not None
            result += ' ' if result else ''    
            result += get_three_digit_num(million) + ' Million'
        if thousand:
            result += ' ' if result else ''
            result += get_three_digit_num(thousand) + ' Thousand'
        if last_three:
            result += ' ' if result else ''
            result += get_three_digit_num(last_three)
        return result
                