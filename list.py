void main() {
  //  Create an empty list called my_list
  List<int> my_list = [];

  // 2. Append elements to my_list
  my_list.add(10);
  my_list.add(20);
  my_list.add(30);
  my_list.add(40);

  //  Insert the value 15 at the second position
  my_list.insert(1, 15);

  //  Extend my_list with another list [50, 60, 70]
  my_list.addAll([50, 60, 70]);

  //  Remove the last element from my_list
  my_list.removeLast();

  //  Sort my_list in ascending order
  my_list.sort();

  //  Find and print the index of the value 30 in my_list
  int indexOf30 = my_list.indexOf(30);
  print("Index of 30: $indexOf30");

  // Printing the final list to see the result
  print("Final list: $my_list");
}
