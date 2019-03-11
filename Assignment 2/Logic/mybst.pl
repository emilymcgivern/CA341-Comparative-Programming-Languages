binary_tree(empty).
binary_tree(bst(_,L,R)) :-  binary_tree(L), binary_tree(R).

sample(bst(6, bst(4, bst(2, nil, nil), bst(5, nil, nil)), bst(9, bst(7, nil, nil), nil))).

insert(X, null, tree(X, null, null)).
insert(X, tree(K,L,R), tree(K,LR,R)) :- X < K, insert(X,L,LR), !.
insert(X, tree(K,L,R), tree(K,L,RR)) :- X > K, insert(X,R,RR), !.

search(node(X, _, _), X) :- !.
search(node(K, L, _), X) :- X < K, !, search(L, X).
search(node(_K, _, R), X) :- search(R, X).

inorder(empty, []).
inorder(bst(K,L,R), Tree) :- inorder(L, LL), inorder(R, LR), append(LL, [K|LR], Tree).


preorder(empty, []).
preorder(bst(K,L,R), Tree) :- preorder(L, LL), preorder(R, LR), append([K|LL], LR, Tree).


postorder(empty, []).
postorder(bst(K,L,R), Tree) :- postorder(L, LL), postorder(R, LR), append(LL, LR, List1), append(List1, [K], Tree).
