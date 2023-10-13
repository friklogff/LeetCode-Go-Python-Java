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

// blank 返回长度为 n 的由空格组成的字符串
func blank(n int) string {
    return strings.Repeat(" ", n)
}

func fullJustify(words []string, maxWidth int) (ans []string) {
    right, n := 0, len(words)
    for {
        left := right // 当前行的第一个单词在 words 的位置
        sumLen := 0   // 统计这一行单词长度之和
        // 循环确定当前行可以放多少单词，注意单词之间应至少有一个空格
        for right < n && sumLen+len(words[right])+right-left <= maxWidth {
            sumLen += len(words[right])
            right++
        }

        // 当前行是最后一行：单词左对齐，且单词之间应只有一个空格，在行末填充剩余空格
        if right == n {
            s := strings.Join(words[left:], " ")
            ans = append(ans, s+blank(maxWidth-len(s)))
            return
        }

        numWords := right - left
        numSpaces := maxWidth - sumLen

        // 当前行只有一个单词：该单词左对齐，在行末填充剩余空格
        if numWords == 1 {
            ans = append(ans, words[left]+blank(numSpaces))
            continue
        }

        // 当前行不只一个单词
        avgSpaces := numSpaces / (numWords - 1)
        extraSpaces := numSpaces % (numWords - 1)
        s1 := strings.Join(words[left:left+extraSpaces+1], blank(avgSpaces+1)) // 拼接额外加一个空格的单词
        s2 := strings.Join(words[left+extraSpaces+1:right], blank(avgSpaces))  // 拼接其余单词
        ans = append(ans, s1+blank(avgSpaces)+s2)
    }
}

作者：力扣官方题解
链接：https://leetcode.cn/problems/text-justification/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
给出完善后带注释完整代码

给出测试输出语句
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
func insert(intervals [][]int, newInterval []int) [][]int {

}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {

    }
}
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
    public List<String> fullJustify(String[] words, int maxWidth) {

    }
}
我们用中文交流，分开介绍每个版本的所需要掌握的详细基础知识

再分别介绍每个版本的解题思路

git add .
git commit -m "Updated"
git push                                                                                                                                      

```

git config --global user.name "friklogff"
git config --global user.email "@qq.com"
git config user.name
git config user.email
ssh-keygen -t rsa -C '@qq.com'
cat ~/.ssh/id_rsa.pub