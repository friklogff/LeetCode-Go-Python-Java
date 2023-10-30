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
func maximalRectangle(matrix [][]byte) int {
    m, n := len(matrix), len(matrix[0])
    heights := make([]int, n+1)
    res := 0
    stack := []int{-1}
    max := func(x, y int) int {
        if x > y {
            return x
        }
        return y
    }
    for i := 0; i < m; i++ {
        for j := 0; j <= n; j++ {
            if j < n && matrix[i][j] == '1' {
                heights[j]++
            } else {
                heights[j] = 0
            }
            top := stack[len(stack)-1]
            for top != -1 && heights[top] >= heights[j] {
                stack = stack[:len(stack)-1]
                left := stack[len(stack)-1]
                res = max(res, heights[top]*(j-left-1))
                top = left
            }
            if j < n {
                stack = append(stack, j)
            }
        }
    }
    return res
}

给出测试输出语句
你能用同样的思路同样数量的解法用go实现么，以此为开头，给出带注释完整代码
func combine(n int, k int) [][]int {

}
你能用同样的思路同样数量的解法用Python实现么，以此为开头，给出带注释完整代码
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
你能用同样的思路同样数量的解法用Java实现么，以此为开头，给出带注释完整代码
class Solution {
    public int maximalRectangle(char[][] matrix) {

    }
}
你能用同样的思路同样数量的解法用c++实现么，以此为开头，给出带注释完整代码
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        
    }
};
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