"""This module demonstrates the usage of the PriorityQueue class"""

from priority_queue import PriorityQueue
def main():
  """
  This function demonstrates the usage of the PriorityQueue class
  """
  pq = PriorityQueue()

  pq.push("Task 1", 3)
  pq.push("Task 2", 1)
  pq.push("Task 3", 2)

  print(pq.pop())
  print(pq.pop())
  print(pq.pop())

if __name__ == "__main__":
  main()
