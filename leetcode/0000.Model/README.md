## 代码

## Go

```Go

```

## Python

```Python

```

## Java

```Java

```

## Cpp

```Cpp

```

## Prompt

```Prompt
我们用中文交流，你能理解这段代码么，逐行加上注释
func isMatch(s string, p string) bool {
    for len(s) > 0 && len(p) > 0 && p[len(p)-1] != '*' {
        if charMatch(s[len(s)-1], p[len(p)-1]) {
            s = s[:len(s)-1]
            p = p[:len(p)-1]
        } else {
            return false
        }
    }
    if len(p) == 0 {
        return len(s) == 0
    }
    sIndex, pIndex := 0, 0
    sRecord, pRecord := -1, -1
    for sIndex < len(s) && pRecord < len(p) {
        if p[pIndex] == '*' {
            pIndex++
            sRecord, pRecord = sIndex, pIndex
        } else if charMatch(s[sIndex], p[pIndex]) {
            sIndex++
            pIndex++
        } else if sRecord != -1 && sRecord + 1 < len(s) {
            sRecord++
            sIndex, pIndex = sRecord, pRecord
        } else {
            return false
        }
    }
    return allStars(p, pIndex, len(p))
}

func allStars(str string, left, right int) bool {
    for i := left; i < right; i++ {
        if str[i] != '*' {
            return false
        }
    }
    return true
}

func charMatch(u, v byte) bool {
    return u == v || v == '?'
}



给出完善后带注释完整代码

给出测试输出语句


你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public boolean isMatch(String s, String p) {

    }
}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
public:
    bool isMatch(string s, string p) {

    }
};
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
func countAndSay(n int) string {

}
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push

```


