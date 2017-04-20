def thousands_with_commas(i):
# Write your code here.
    s = str(i)
    res=""
    for x in range(len(s)):
        if ((x>0) and ((x%3)==0)):
            res = "," + res
        res = str(s[-(1+x)]) + res
    return res

if __name__ == '__main__':
    assert thousands_with_commas(1234) == '1,234'
    assert thousands_with_commas(123456789) == '123,456,789'
    assert thousands_with_commas(12) == '12'    