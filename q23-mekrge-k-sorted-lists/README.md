![alt text](image.png)

The logic :: 
You create  a heap 

First you put all the values, index, node as tuple into the heap => will result in a heap with the mean heap with lowest value at top of the heap, we added idx if the values are similar then the index will compared preventing from node comparisons.

have a dummy which will now start re connecting the nodes

Then until the mheap ends 
pop the lowest values 
connect the prev dummy node to node which you got from the heap 
move prev to this node 


if there is .next to the poped node
push the .next node into heap


