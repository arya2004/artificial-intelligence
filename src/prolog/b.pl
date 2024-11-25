% Facts
male(albert).
male(bob).
male(bill).
male(carl).
male(charlie).
male(dan).
male(edward).

female(alice).
female(betsy).
female(diana).

happy(albert).
happy(alice).

parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).




% Rules
runs(albert) :- happy(albert).

% Queries
:- initialization(main).


main :-
      male(alice) -> write(true); write(false),
      
      parent(Y, carl),
      parent(X, Y),
      write(Y),
      write(X), nl,
      
      'alice' = bob -> write(true); write(false).

      
      
      
      
      
      
      