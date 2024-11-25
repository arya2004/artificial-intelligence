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

% Rules
runs(albert) :- happy(albert).

% Queries
:- initialization(main).


main :-
      male(alice) -> write(true); write(false).