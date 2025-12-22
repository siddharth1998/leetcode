# LeetCode Solutions — Repository Overview

This repository contains my Python solutions to selected LeetCode problems, organized by folder. The file for each problem is linked in the per-problem section below and contains an implementation and (often) a short comment or approach.

Summary:
- This README provides a Blind 75 ordered checklist (heuristic mapping) that marks which problems are present in this repo.
- For each implemented problem there are two short tips and a one-line "How I solved" note, plus a one-line code summary and a link to the file.

Usage:
- Browse the `./` folders to open solution files (each problem is in its own folder). Filepaths are linked in the tables below.

---

**Blind 75 checklist (ordered, with topics)**

The table below follows the common Blind 75 ordering and groups topics. For each entry it marks `Done` when a solution file is present in this repo and includes a path to the implementation. If you'd like I can re-run a web-sync to guarantee exact canonical ordering from a chosen source.

| # | Problem | Topic | Status | Repo Path |
|---:|---|---|---:|---|
| — | Two Sum | Array / Hash | Not Done | - |
| — | Add Two Numbers | Linked List | Not Done | - |
| — | Longest Substring Without Repeating Characters | Sliding Window | Not Done | - |
| — | Median of Two Sorted Arrays | Binary Search | Not Done | - |
| — | Longest Palindromic Substring | DP / Two Pointers | Not Done | - |
| — | ZigZag Conversion | String | Not Done | - |
| — | Container With Most Water | Two Pointers | Not Done | - |
| — | 3Sum | Two Pointers / Sorting | Not Done | - |
| — | Letter Combinations of a Phone Number | Backtracking | Not Done | - |
| — | Valid Parentheses | Stack | Not Done | - |
| — | Merge Two Sorted Lists | Linked List | Not Done | - |
| — | Swap Nodes in Pairs | Linked List | Not Done | - |
| — | Reverse Linked List | Linked List | Not Done | - |
| 19 | Remove Nth Node From End of List | Linked List / Two Pointers | Done | `q19-remove-nth-node-from-end-of-list/q19-remove-nth-node-from-end-of-list.py` |
| — | Valid Anagram | Hash Table | Not Done | - |
| — | Group Anagrams | Hash Table / Sorting | Not Done | - |
| — | Top K Frequent Elements | Heap / Hash | Not Done | - |
| — | Kth Largest Element in an Array | Heap / Quickselect | Not Done | - |
| — | Product of Array Except Self | Array / Prefix products | Not Done | - |
| — | Valid Sudoku | Hash Table | Not Done | - |
| — | Search in Rotated Sorted Array | Binary Search | Not Done | - |
| — | Find Minimum in Rotated Sorted Array | Binary Search | Not Done | - |
| — | Minimum Window Substring | Sliding Window | Not Done | - |
| — | Subarray Sum Equals K | Hash / Prefix Sum | Not Done | - |
| — | Combination Sum | Backtracking | Not Done | - |
| — | Permutations | Backtracking | Not Done | - |
| — | Word Search | Backtracking / DFS | Not Done | - |
| — | Letter Case Permutation | Backtracking | Not Done | - |
| — | Binary Tree Inorder Traversal | Tree / DFS | Not Done | - |
| 98 | Validate Binary Search Tree | BST / DFS | Done | `98-validate-binary-search-tree/98-Validate-binary-search-tree.py` |
| — | Symmetric Tree | Tree / DFS | Not Done | - |
| 104 | Maximum Depth of Binary Tree | Tree / DFS | Done | `q104-max-depth-of-binary-tree/q104-max-depth-of-binary-tree.py` |
| 102 | Binary Tree Level Order Traversal | Tree / BFS | Done | `q-102-binary-tree-order-traversal/q102-binary-tree-level-roder-traversal.py` |
| — | Convert Sorted Array to Binary Search Tree | Tree / Recursion | Not Done | - |
| — | Balanced Binary Tree | Tree / DFS | Not Done | - |
| — | Minimum Depth of Binary Tree | Tree / BFS | Not Done | - |
| — | Path Sum | Tree / DFS | Not Done | - |
| — | Sum Root to Leaf Numbers | Tree / DFS | Not Done | - |
| — | Binary Tree Maximum Path Sum | Tree / DFS | Not Done | - |
| 543 | Diameter of Binary Tree | Tree / DFS | Done | `q543-diameter-of-tree/q543.py` |
| 230 | Kth Smallest Element in a BST | BST / Tree | Done | `230-kth-smallest-element-in-bst/230-kth-smallest-element-in-bst.py` |
| 235 | Lowest Common Ancestor of a BST | BST / Tree | Done | `q235-lowest-common-ancestor/q235-lca.py` |
| — | Serialize and Deserialize Binary Tree | Tree / Design | Not Done | - |
| — | Implement Trie (Prefix Tree) | Trie / Design | Not Done | - |
| — | Word Search II | Trie / Backtracking | Not Done | - |
| — | Number of Islands | Graph / DFS / BFS | Not Done | - |
| — | Clone Graph | Graph / DFS / BFS | Not Done | - |
| — | Course Schedule | Graph / Topological Sort | Not Done | - |
| — | Pacific Atlantic Water Flow | Graph / BFS / DFS | Not Done | - |
| — | Longest Increasing Path in a Matrix | Graph / DFS / DP | Not Done | - |
| — | Minimum Height Trees | Graph / BFS | Not Done | - |
| — | Evaluate Division | Graph / DFS | Not Done | - |
| — | Word Ladder | Graph / BFS | Not Done | - |
| — | Binary Tree Right Side View | Tree / BFS | Not Done | - |
| — | Find Peak Element | Array / Binary Search | Not Done | - |
| — | House Robber | Dynamic Programming | Not Done | - |
| — | House Robber II | Dynamic Programming | Not Done | - |
| — | Decode Ways | Dynamic Programming | Not Done | - |
| — | Coin Change | Dynamic Programming | Not Done | - |
| — | Longest Increasing Subsequence | Dynamic Programming | Not Done | - |
| — | Word Break | Dynamic Programming | Not Done | - |
| — | Palindrome Partitioning | Backtracking / DP | Not Done | - |
| — | Combination Sum IV | Dynamic Programming | Not Done | - |
| — | Jump Game | Greedy / DP | Not Done | - |
| — | Maximum Product Subarray | DP / Greedy | Not Done | - |

---

## Problems implemented in this repo

Below are compact writeups for each implemented problem: two quick tips and a one-line "How I solved" summary, plus a one-line code summary and a link to the file.

### Remove Nth Node From End of List (19)
- Tip 1: Create a gap by moving fast pointer n steps ahead, then move both.
- Tip 2: Use a dummy head to handle removal of the first node gracefully.
- How I solved: Two-pointer (fast/slow) gap then remove the slow node.
Code summary: Advances fast n steps, then moves both to unlink the target node. Path: `q19-remove-nth-node-from-end-of-list/q19-remove-nth-node-from-end-of-list.py`

### Validate Binary Search Tree (98)
- Tip 1: Use min/max bounds in recursion to ensure each node fits the valid range.
- Tip 2: Initialize with infinite bounds and update for left/right subtrees.
- How I solved: Recursive helper passing valid (low, high) range.
Code summary: Recursively verifies node values lie within allowed bounds. Path: `98-validate-binary-search-tree/98-Validate-binary-search-tree.py`

### Binary Tree Level Order Traversal (102)
- Tip 1: Use a queue and iterate over the current queue size to capture a level.
- Tip 2: Append children while processing the current level’s nodes.
- How I solved: Standard BFS collecting nodes level-by-level.
Code summary: Uses `collections.deque` to perform BFS and collect levels. Path: `q-102-binary-tree-order-traversal/q102-binary-tree-level-roder-traversal.py`

### Maximum Depth of Binary Tree (104)
- Tip 1: Depth = 1 + max(depth(left), depth(right)).
- Tip 2: Base case: null node returns 0.
- How I solved: Simple recursive max of child depths.
Code summary: Recursive function returning height; uses base-case 0. Path: `q104-max-depth-of-binary-tree/q104-max-depth-of-binary-tree.py`

### Diameter of Binary Tree (543)
- Tip 1: At each node, diameter candidate = leftHeight + rightHeight.
- Tip 2: Return 1 + max(leftHeight, rightHeight) from recursion.
- How I solved: DFS helper computes heights and updates global max diameter.
Code summary: DFS returns heights and updates max diameter variable. Path: `q543-diameter-of-tree/q543.py`

### Kth Smallest Element in a BST (230)
- Tip 1: Inorder traversal yields sorted values for a BST.
- Tip 2: Stop early when the k-th element is reached to save work.
- How I solved: Recursive inorder traversal with a counter capturing the k-th value.
Code summary: Inorder recursion with a counter and early-stop when found. Path: `230-kth-smallest-element-in-bst/230-kth-smallest-element-in-bst.py`

### Lowest Common Ancestor of a BST (235)
- Tip 1: Use BST property: if both nodes < root go left; if both > root go right.
- Tip 2: First node where p and q split (or equal root) is the LCA.
- How I solved: Iterative descent using comparisons of p/q to root.
Code summary: Iteratively finds the split point using node values. Path: `q235-lowest-common-ancestor/q235-lca.py`

### Merge k Sorted Lists (23)
- Tip 1: Use a min-heap to always pop the smallest current head among lists.
- Tip 2: Use a tie-breaker index when pushing tuples to avoid node comparisons.
- How I solved: Push initial heads, pop smallest and push its next until heap empties.
Code summary: Min-heap (value, idx, node) merges lists into one. Path: `q23-mekrge-k-sorted-lists/q23-merge-k-sorted-lists.py`

### Subtree of Another Tree (572)
- Tip 1: Write an `isSameTree` helper and test it at each node of the big tree.
- Tip 2: Short-circuit early when matches are found; handle null cases carefully.
- How I solved: DFS caller that uses `isSameTree` at each node to check.
Code summary: Traverses main tree and compares subtree equality via helper. Path: `q572-subtree-of-another-tree/q572-subtree-of-another-tree.py`

### Same Tree (100)
- Tip 1: Compare node values and recursively test both left and right children.
- Tip 2: Treat null-vs-non-null differences as false immediately.
- How I solved: Simple recursive equality check of both subtrees.
Code summary: Recursively compares structure and values for equality. Path: `q100-same-tree/q100-same-tree.py`

### Invert Binary Tree (226)
- Tip 1: Swap left and right for each node; recurse on children.
- Tip 2: In-place modification is fine; null nodes return immediately.
- How I solved: Recursively swap children and descend.
Code summary: Performs in-place left/right swap recursively. Path: `q226-invert-binary-tree/q226-invert-binary-tree.py`

---

## Notes & next steps
- The Blind 75 canonical ordering can be fetched from a web source and re-applied; tell me if you want me to re-generate the checklist strictly following a specific canonical source (I can fetch and re-order the table).
- If you want I can also:
  - Add problem links to the official LeetCode pages, or
  - Add small test harnesses that run each file with sample inputs.

If this README looks good I can commit it to `main` or open a PR — tell me which you prefer.

---

Generated: December 22, 2025
