// problem from hackerrank: https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
// A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
// Given a pointer to the head of a linked list, determine if it contains a cycle.
// Complete the has_cycle function in the editor below.
// It has the following parameter:
// SinglyLinkedListNode pointer head: a reference to the head of the list

import java.io.*;
import java.util.*;

public class Solution {
    static boolean hasCycle(SinglyLinkedListNode head) {
        if (head == null){
            return false;
        }
        Set<SinglyLinkedListNode> anteriores = new HashSet<SinglyLinkedListNode>();
        while (head != null){
            if(anteriores.contains(head)){
                return true;
            }
            anteriores.add(head);
            head = head.next;
        }
        return false;
    }
}