**https://leetcode.com/problems/implement-trie-prefix-tree/**

## правильное решени
```python
class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEndWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()
		
	def insert(self, word: str):
		current = self.root
		# traverse each character in the word
		for char in word:
			# check if such character already added or not
			if not char in current.children:
				current.children[char] = TrieNode()
			# move to the next character
			current = current.children[char]
		current.isEndWord = True
		
	def search(self, word: str):
		current = self.root
		for char in word:
			if char not in current.children:
				return False
			current = current.children[char]
		return current.isEndWord
	
	def startsWith(self, prefix: str):
		current = self.root
		for char in prefix:
			if char not in current.children:
				return False
			current = current.children[char]
		return True
```

## оценку по времени и памяти
insert - Time O(n)
search - Time O(n)
startsWith - Time O(n) | - Time O(1)

## идея
Префиксное дерево - структура данных, которая позволяет хранить слова (строки) и делать быстрый поиск слов и префиксов слов.
В ноде для хранения символов мы используем hashmap, также в каждой ноде есть флаг - это нода конец слова или нет;