# Python Learning

我的 Python 学习与编程实践记录仓库。

本项目记录我从 Python 基础编程逐步学习算法与数据结构、数据分析、机器学习和 AI 应用开发的过程。

主要目标是提高**独立编程能力、算法思维和解决实际问题的能力**，为后续机器学习、大语言模型（LLM）及 AI Agent 开发打好基础。

当前以 Python 独立编程和算法基础巩固为重点。基础语法与面向对象已经学习或练习过，但数据结构选择、组合使用、递归执行过程和独立调试仍需加强。**完成题目不等于已经能够独立解决所有同类问题。**

## 一、学习目标

- 熟练掌握 Python 基础语法和常用数据结构。
- 能够独立分析问题、编写代码、调试和优化程序。
- 通过 LeetCode 练习常见算法与数据结构，理解算法执行过程和复杂度。
- 学习 NumPy、Pandas 和机器学习基础。
- 掌握大模型 API 调用、Tool Calling 和 AI Agent 开发。
- 使用 Git、GitHub 和 Codex 管理学习代码与学习记录。

## 二、LeetCode 练习记录

截至 **2026 年 11 月 23 日**，按仓库中已保存的题解文件统计，共收录 **42 道 LeetCode 题目（27 道 Easy、15 道 Medium）**。题目列表与实际文件一一对应。

不能仅凭题解文件存在判断是否独立掌握。

| 题号 | 题目 | 难度 | 核心知识点 | 代码 |
| ---- | ---- | ---- | ---- | ---- |
| 1480 | [一维数组的动态和](https://leetcode.cn/problems/running-sum-of-1d-array/) | Easy | 列表、循环、前缀和 | [leetcode_1480.py](leetcode_1480.py) |
| 1672 | [最富有客户的资产总量](https://leetcode.cn/problems/richest-customer-wealth/) | Easy | 二维列表、嵌套循环、最大值 | [leetcode_1672.py](leetcode_1672.py) |
| 1207 | [独一无二的出现次数](https://leetcode.cn/problems/unique-number-of-occurrences/) | Easy | 字典计数、集合去重 | [leetcode_1207.py](leetcode_1207.py) |
| 1 | [两数之和](https://leetcode.cn/problems/two-sum/) | Easy | 哈希表、补数查找 | [leetcode_1.py](leetcode_1.py) |
| 11 | [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/) | Medium | 双指针、贪心思想 | [leetcode_11.py](leetcode_11.py) |
| 283 | [移动零](https://leetcode.cn/problems/move-zeroes/) | Easy | 同向双指针、原地修改 | [leetcode_283.py](leetcode_283.py) |
| 167 | [两数之和 II — 输入有序数组](https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/) | Medium | 有序数组、双指针 | [leetcode_167.py](leetcode_167.py) |
| 20 | [有效的括号](https://leetcode.cn/problems/valid-parentheses/) | Easy | 字典、栈、括号匹配 | [leetcode_20.py](leetcode_20.py) |
| 933 | [最近的请求次数](https://leetcode.cn/problems/number-of-recent-calls/) | Easy | 队列、双端队列、滑动时间窗口 | [leetcode_933.py](leetcode_933.py) |
| 1971 | [寻找图中是否存在路径](https://leetcode.cn/problems/find-if-path-exists-in-graph/) | Easy | 图、邻接表、BFS、队列、集合去重 | [leetcode_1971.py](leetcode_1971.py) |
| 217 | [存在重复元素](https://leetcode.cn/problems/contains-duplicate/) | Easy | 集合、成员判断、提前返回 | [leetcode_217.py](leetcode_217.py) |
| 752 | [打开转盘锁](https://leetcode.cn/problems/open-the-lock/) | Medium | BFS 最短路径、`deque`、集合、状态建模 | [leetcode_752.py](leetcode_752.py) |
| 994 | [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/) | Medium | 二维网格、多源 BFS、队列、时间传播 | [leetcode_994.py](leetcode_994.py) |
| 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/) | Medium | BFS、二维网格、连通区域、集合去重 | [leetcode_200.py](leetcode_200.py) |
| 733 | [图像渲染](https://leetcode.cn/problems/flood-fill/) | Easy | 递归 DFS、颜色替换、原地标记、递归终止 | [leetcode_733.py](leetcode_733.py) |
| 695 | [岛屿的最大面积](https://leetcode.cn/problems/max-area-of-island/) | Medium | 递归 DFS、连通区域面积、递归返回值累加、`visited` | [leetcode_695.py](leetcode_695.py) |
| 206 | [反转链表](https://leetcode.cn/problems/reverse-linked-list/) | Easy | 单向链表、三引用迭代、指针反转、边界处理 | [leetcode_206.py](leetcode_206.py) |
| 21 | [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/) | Easy | 链表归并、节点连接、双指针、边界判断 | [leetcode_21.py](leetcode_21.py) |
| 876 | [链表的中间结点](https://leetcode.cn/problems/middle-of-the-linked-list/) | Easy | 链表遍历、长度统计、快慢指针 | [leetcode_876.py](leetcode_876.py) |
| 141 | [环形链表](https://leetcode.cn/problems/linked-list-cycle/) | Easy | 快慢指针、对象身份判断、环检测 | [leetcode_141.py](leetcode_141.py) |
| 704 | [二分查找](https://leetcode.cn/problems/binary-search/) | Easy | 闭区间二分查找、左右边界、循环条件 | [leetcode_704.py](leetcode_704.py) |
| 35 | [搜索插入位置](https://leetcode.cn/problems/search-insert-position/) | Easy | 二分查找、插入位置、`return left` | [leetcode_35.py](leetcode_35.py) |
| 34 | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/) | Medium | 左右边界二分查找、候选答案、函数复用 | [leetcode_34.py](leetcode_34.py) |
| 69 | [x 的平方根](https://leetcode.cn/problems/sqrtx/) | Easy | 二分查找、候选答案、平方根向下取整、边界更新 | [leetcode_69.py](leetcode_69.py) |
| 912 | [排序数组](https://leetcode.cn/problems/sort-an-array/) | Medium | 随机基准、三路快速排序、递归返回值、列表拼接 | [leetcode_912.py](leetcode_912.py) |
| 102 | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/) | Medium | 二叉树、BFS、`deque`、分层遍历 | [leetcode_102.py](leetcode_102.py) |
| 104 | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/) | Easy | BFS、DFS、递归返回值、树高 | [leetcode_104.py](leetcode_104.py) |
| 100 | [相同的树](https://leetcode.cn/problems/same-tree/) | Easy | 二叉树、DFS、双节点递归、布尔返回值、`and` | [leetcode_100.py](leetcode_100.py) |
| 226 | [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/) | Easy | 二叉树、DFS、递归修改节点、左右子树交换 | [leetcode_226.py](leetcode_226.py) |
| 101 | [对称二叉树](https://leetcode.cn/problems/symmetric-tree/) | Easy | 双节点镜像递归、结构与节点值比较、布尔返回值 | [leetcode_101.py](leetcode_101.py) |
| 110 | [平衡二叉树](https://leetcode.cn/problems/balanced-binary-tree/) | Easy | BFS 求高度、后序 DFS、`-1` 向上传递、提前返回 | [leetcode_110.py](leetcode_110.py) |
| 112 | [路径总和](https://leetcode.cn/problems/path-sum/) | Easy | DFS、剩余目标值、叶子节点、`or` 短路 | [leetcode_112.py](leetcode_112.py) |
| 111 | [二叉树的最小深度](https://leetcode.cn/problems/minimum-depth-of-binary-tree/) | Easy | DFS、子树深度、单侧子树边界 | [leetcode_111.py](leetcode_111.py) |
| 643 | [子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/) | Easy | 固定长度窗口、增量更新窗口和 | [leetcode_643.py](leetcode_643.py) |
| 209 | [长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/) | Medium | 可变长度窗口、窗口和、最短长度 | [leetcode_209.py](leetcode_209.py) |
| 3 | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/) | Medium | 可变长度窗口、`set` 成员维护 | [leetcode_3.py](leetcode_3.py) |
| 438 | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/) | Medium | 固定长度窗口、`dict` 字符频次 | [leetcode_438.py](leetcode_438.py) |
| 1004 | [最大连续 1 的个数 III](https://leetcode.cn/problems/max-consecutive-ones-iii/) | Medium | 可变长度窗口、剩余翻转次数 | [leetcode_1004.py](leetcode_1004.py) |
| 703 | [数据流中的第 K 大元素](https://leetcode.cn/problems/kth-largest-element-in-a-stream/) | Easy | 最小堆、对象状态、动态 Top K | [leetcode_703.py](leetcode_703.py) |
| 215 | [数组中的第 K 个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/) | Medium | 原地建最小堆、弹出多余元素、静态 Top K | [leetcode_215.py](leetcode_215.py) |
| 1046 | [最后一块石头的重量](https://leetcode.cn/problems/last-stone-weight/) | Easy | 负数模拟最大堆、连续两次出堆 | [leetcode_1046.py](leetcode_1046.py) |
| 347 | [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/) | Medium | 字典计数、元组优先级、频次堆 | [leetcode_347.py](leetcode_347.py) |

题目来源：[LeetCode 中文站](https://leetcode.cn/)。

### 算法专题与学习进度

已练习的题目见上表。题意、实现、复杂度和逐题复盘写在对应源文件的模块注释中。

- **前缀和、哈希表、集合与双指针**已完成基础练习。练习了累加、计数、去重及移动边界，仍需间隔复现。
- **栈、队列与双端队列**已练习后进先出、队列中的坐标元组、队列配合集合去重，以及 `deque` 两端操作与列表首部删除的复杂度差异。
- **图与 BFS**基础专题已完成，练习了邻接表、可达性、最短路径、多源传播和连通区域计数。后续复现边界处理与去重。
- **DFS、递归与二叉树**已完成入门练习。已练习层序遍历、前中后序 DFS、原地修改、汇总子调用返回值和特殊值的传递。仍需独立复现，并留意 Python 的递归深度限制。
- **链表与快慢指针**已完成入门练习。从 `ListNode`、遍历、节点值求和和插入删除，练习到引用反转、链表归并及对象身份比较。仍需复习空链表、单节点和尾部边界。
- **二分查找**已完成基础搜索与边界查找入门，仍需巩固闭区间和候选答案。左闭右开、二分答案和旋转数组等进阶题型尚未系统学习。
- **滑动窗口**基础阶段已完成。练习了固定窗口与可变窗口，以及用窗口和、`set`、`dict` 和剩余次数维护状态。
- **堆与优先队列**基础阶段已完成，后续需要间隔复习。练习了最小堆、O(n) 的 `heapify()` 建堆、O(log n) 的入堆与出堆调整、Top K、负数模拟最大堆，以及字典计数和元组优先级。双堆中位数、手写堆的上浮与下沉、复杂优先级调度尚未系统学习。

## 三、Python 学习进度

**2026 年 11 月 6 日**归档第 912 题，练习随机基准、三路划分与复杂度分析。

**2026 年 11 月 16 日**归档二叉树基础与分层遍历练习。

**2026 年 11 月 17 日**归档镜像比较与平衡判断题解。

**2026 年 11 月 19 日**归档根到叶子路径和最小深度题解。二叉树基础转入间隔复习。第 404 题「左叶子之和」目前只了解了题意，尚未编写代码。

**2026 年 11 月 20 日**完成滑动窗口基础专题。

**2026 年 11 月 23 日**完成堆与优先队列基础专题，后续间隔复习。下一阶段为前缀和进阶与差分。

### 1. Python 基础

下列内容已学习或练习过，仍需通过独立编程巩固；不表示所有基础内容已经熟练掌握。

| 知识模块 | 当前状态 |
| ---- | ---- |
| 变量、数据类型、类型转换 | 已学习，需巩固；重点辨别字符串 `'1'` 与整数 `1` |
| 运算符、条件判断 | 已学习，需巩固 |
| `for` / `while`、`break`、`continue` | 已学习，需巩固嵌套循环执行顺序 |
| 列表及其常用操作 | 已学习，需巩固 |
| 二维列表、行列索引与边界判断 | 已在 BFS/DFS 网格题中练习 |
| 字典、集合及其应用 | 已练习 `set()`、`add()`、成员判断和去重 |
| 字符串及常用操作 | 已学习，需巩固 |
| `enumerate()`、`range()` | 已学习，需巩固 |
| 列表推导式 | 已学习，需巩固 |
| 函数定义、参数、返回值与作用域 | 已学习；新增嵌套函数与递归返回值累加练习 |
| 递归调用顺序、终止条件、调用栈 | 已练习逐层推导调用、返回和恢复位置，待用新题独立验证 |
| 模块导入与文件组织 | 已学习，需巩固 |
| `try` / `except` 异常处理 | 已学习，需巩固 |
| 文件读写、JSON 数据处理 | 已学习，需巩固 |

当前需要加强：独立实现算法、根据问题选择合适数据结构、组合使用循环与函数、定位报错、解释递归与分治过程，以及区分平均、最坏时间和额外空间复杂度。

### 2. 面向对象编程（OOP）

已学习或练习过：类与对象、`self`、`__init__()`、继承、方法重写、`super()`、封装、`@property` 与 setter、多态，以及对象之间的方法调用；曾通过英雄战斗系统等程序理解基本机制。

当前状态：**已学习基础，仍需通过独立编程巩固**。LeetCode 中的 `class Solution` 不代表已全面掌握工程化面向对象设计。

### 3. 算法与数据结构

| 知识模块 | 当前状态 |
| ---- | ---- |
| 时间与空间复杂度 | 已结合 BFS/DFS 和排序练习，仍需巩固平均、最坏情况及递归列表占用 |
| 数组、列表与二维网格遍历 | 已练习 |
| 哈希表（字典）、集合去重 | 已练习 |
| 前缀和 | 已练习 |
| 双指针 | 已完成基础题目 |
| 滑动窗口 | 基础阶段已完成，已练习固定与可变长度窗口、窗口和、集合及字典状态维护 |
| 堆与优先队列（`heapq`） | 已完成基础学习，涉及 Top K、负数模拟最大堆、字典计数与元组优先级，后续间隔复习 |
| 栈的基础应用 | 已练习基础应用，需巩固 |
| 单调栈 | 尚未系统学习 |
| 队列与 `deque` | 已在滑动窗口与 BFS 中练习 |
| 图与 BFS | 已完成基础专题，需复现 |
| 递归与网格 DFS | **已完成 733、695 两道入门题，需巩固** |
| 链表基础操作 | 已完成入门，需巩固 |
| 链表反转 | 已完成 206，仍需独立复现 |
| 链表归并 | 已完成 21，需巩固 |
| 快慢指针寻找中间节点 | 已完成 876，需巩固 |
| 快慢指针判断环 | 已完成 141，需巩固对象身份判断 |
| 显式栈 DFS、图 DFS、回溯 | 尚未系统学习 |
| 二分查找基础 | 已完成 704 |
| 二分查找插入位置 | 已完成 35 |
| 二分查找左右边界 | 已完成 34 |
| 整数平方根、合法候选答案 | 已练习 69；简化版本含 AI 辅助讲解 |
| 二分查找复杂度分析 | 已学习 O(log n) |
| 二分查找区间不变量 | 已初步理解，仍需巩固边界初始化与独立实现 |
| 左闭右开区间写法 | 尚未系统学习 |
| 二分答案、旋转数组等进阶题型 | 尚未系统学习 |
| 随机基准三路快速排序 | 已完成 912 代码练习并保存正式题解，仍需巩固递归、重复元素与复杂度 |
| 二叉树与基础树遍历 | 已练习 LeetCode 102、104、100、226、101、110、112、111，涉及层序遍历、树高、双节点递归、路径判断和单侧子树边界，后续间隔复习 |
| 动态规划 | 尚未系统学习 |

### 4. Python 工程工具

| 工具或技能 | 当前状态 |
| ---- | ---- |
| VS Code 编写和运行 Python | 已掌握基础操作 |
| Git 状态检查、暂存、提交与推送 | 已实践，继续巩固 |
| GitHub 仓库管理 | 已实践 |
| README.md 与 Markdown | 已实践 |
| Git Clone | 已实践 |
| Git 分支基本概念 | 已接触 |
| 多文件模块导入 | 已学习 |
| `assert` 和基础测试 | 已接触，题解文件中已有测试 |
| Codex 辅助整理题解与 Git 操作 | 已实践；也开始手动管理题解文件 |

## 四、当前学习路线

现阶段以 Python 独立编程和算法训练为主。堆与优先队列基础阶段已完成，下一专题是前缀和进阶与差分。NumPy、Pandas、机器学习和大模型 API 保留为后续方向。

| 阶段 | 学习重点 | 状态 |
| ---- | ---- | ---- |
| 阶段 1 | Python 基础语法 | 已学习，需独立练习巩固 |
| 阶段 2 | Python 综合编程、面向对象基础 | 已学习，继续巩固 |
| 阶段 3 | LeetCode 常见算法与数据结构 | BFS、DFS/递归、二叉树、链表、二分查找及排序基础已练习。滑动窗口、堆与优先队列基础已完成，下一步学习前缀和进阶与差分 |
| 阶段 4 | NumPy 数值计算 | 待学习 |
| 阶段 5 | Pandas 数据处理与可视化 | 待学习 |
| 阶段 6 | 机器学习基础与模型评估 | 待学习 |
| 阶段 7 | 大模型 API 与 AI 应用开发 | 待学习 |
| 阶段 8 | Tool Calling、RAG 和 AI Agent | 长期目标 |

### 近期计划

按以下顺序推进。基础前缀和已经练习过，从进阶应用与差分开始。

1. 前缀和进阶与差分
2. 区间
3. 单调栈
4. 二叉搜索树与字典树
5. 贪心
6. 回溯
7. 动态规划
8. 图论进阶
9. 位运算、矩阵等未覆盖模块

二分查找、链表、基础 BFS/DFS、二叉树、排序、滑动窗口和堆基础采用间隔复习。新题先独立编写，再根据实际问题纠错。布置新题前先核对 README 与已有题解。

### 算法知识总目录

以面试经典 150 题的 23 个模块作为覆盖范围，近期学习顺序见上方。题单中未单列的前缀和与差分、单调栈、贪心、排序、并查集和拓扑排序也纳入学习目录。[LeetCode 面试经典 150 题](https://leetcode.cn/studyplan/top-interview-150/)

1. 数组与字符串
2. 双指针
3. 滑动窗口
4. 矩阵
5. 哈希表
6. 区间
7. 栈
8. 链表
9. 二叉树
10. 二叉树层序遍历
11. 二叉搜索树
12. 图
13. 图的广度优先搜索
14. 字典树
15. 回溯
16. 分治
17. Kadane 算法
18. 二分查找
19. 堆
20. 位运算
21. 数学
22. 一维动态规划
23. 多维动态规划

## 五、项目结构

```text
python-learning/
├── README.md
├── AGENTS.md
├── leetcode_1.py
├── leetcode_3.py
├── leetcode_11.py
├── leetcode_20.py
├── leetcode_21.py
├── leetcode_34.py
├── leetcode_35.py
├── leetcode_69.py
├── leetcode_100.py
├── leetcode_101.py
├── leetcode_102.py
├── leetcode_104.py
├── leetcode_110.py
├── leetcode_111.py
├── leetcode_112.py
├── leetcode_141.py
├── leetcode_167.py
├── leetcode_200.py
├── leetcode_206.py
├── leetcode_209.py
├── leetcode_215.py
├── leetcode_217.py
├── leetcode_226.py
├── leetcode_283.py
├── leetcode_347.py
├── leetcode_438.py
├── leetcode_643.py
├── leetcode_695.py
├── leetcode_703.py
├── leetcode_704.py
├── leetcode_733.py
├── leetcode_752.py
├── leetcode_876.py
├── leetcode_912.py
├── leetcode_933.py
├── leetcode_994.py
├── leetcode_1004.py
├── leetcode_1046.py
├── leetcode_1207.py
├── leetcode_1480.py
├── leetcode_1672.py
└── leetcode_1971.py
```

其中：

- `README.md`：题解索引、专题进度和学习计划。
- `AGENTS.md`：Codex 仓库维护规则。
- `leetcode_*.py`：正式 LeetCode 题解与学习复盘，部分题解带有测试代码。

题解保留用户最终实现及实际学习过程，区分独立实现、提示修正、参考实现后完成和 AI 辅助优化。

## 六、如何运行

### 环境要求

- Python 3（建议使用 Python 3.9 或更新版本，以支持部分题解中的 `list[list[int]]` 注解）。
- Git（用于版本管理）。

当前题解主要使用 Python 标准库，无需额外安装第三方依赖。

### 克隆仓库

```bash
git clone https://github.com/khymeow/python-learning.git
cd python-learning
```

### 运行题解

例如：

```bash
python leetcode_200.py
python leetcode_733.py
python leetcode_695.py
python leetcode_206.py
python leetcode_21.py
python leetcode_876.py
python leetcode_141.py
python leetcode_704.py
python leetcode_35.py
python leetcode_34.py
python leetcode_69.py
python leetcode_912.py
```

其他带独立运行入口的题解也可以使用 `python leetcode_题号.py` 运行，具体测试与输出以对应文件内容为准。第 100、101、102、104、110、111、112、226 题提供接收二叉树根节点的 `Solution` 方法。

## 七、学习与代码提交方式

本仓库坚持**独立解题为主、AI 辅助工程管理**的原则。

学习流程：

1. 理解 Python 知识点或算法题目。
2. 独立分析问题并编写第一版代码。
3. 用户自行运行测试并检查边界条件，再交由助手整理保存。
4. 分析时间复杂度与空间复杂度。
5. 尝试优化算法，理解原理。
6. 将正式题目的实现、实际错误和复盘整理到对应的题解文件，README 更新索引与专题进度。GitHub 提交按用户授权执行。

遇到困难可以借助讲解和调试指导，但题目完成后仍需复盘错误、不看完整答案重写，并检查是否能解释实现原理。

### Codex 与其他辅助工具的职责

- 整理**已有**题解，保留用户提供的算法结构。
- 根据真实过程补充题意、必要注释、复杂度和错误复盘。
- 讲解针对用户的实际错误，先让用户独立尝试，再提供必要提示，不直接给出新题完整答案或代替核心算法训练。
- 维护代码文件，在用户授权范围内协助 Git 提交和推送；用户交来的代码默认已自行测试，助手不重复运行测试，也不要求额外编写测试，仅在用户明确要求时执行。
- 按实际文件数量及确认的学习进度维护 README。
- 不在未要求的情况下代替独立解题，不把计划中的知识写成已掌握。

具体规则见 [AGENTS.md](AGENTS.md)。

## 八、长期目标

- 独立编写和调试 Python 程序。
- 理解并实现常见算法与数据结构。
- 使用 Python 处理实际数据。
- 理解机器学习模型的训练与评估过程。
- 通过 API 构建大模型应用。
- 开发具有工具调用、知识检索和任务执行能力的 AI Agent。
- 使用 GitHub 持续积累和展示个人项目。

---

**持续学习，独立思考，重视实践，记录每一次进步。**

*学习进度最后更新：2026 年 11 月 23 日。*
