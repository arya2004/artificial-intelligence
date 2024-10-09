% Facts
% Parents (parent(child, parent))
parent(umesh, arun).
parent(mahesh, arun).
parent(ashwini, umesh).
parent(swara, ashwini).
parent(aiya, mahesh).
parent(neel, pratibha).
parent(ainav, prakash).

parent(umesh, archana).
parent(mahesh, archana).
parent(ashwini, umesh).
parent(swara, ashwini).
parent(aiya, mahesh).
parent(neel, pratibha).
parent(ainav, prakash).

% Grandparents
parent(arun, ganpat).
parent(archana, ganpat).
parent(ganpat, bhalchandra).
parent(smita, bhalchandra).

% Spouses
spouse(umesh, ashwini).
spouse(mahesh, pratibha).
spouse(prashant, pallavi).
spouse(prakash, smita).
spouse(arun, archana).
spouse(ganpat, smita).

% Define rules
father(X, Y) :- parent(Y, X), male(X).
mother(X, Y) :- parent(Y, X), female(X).
grandfather(X, Y) :- parent(Z, Y), father(X, Z).
grandmother(X, Y) :- parent(Z, Y), mother(X, Z).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- sibling(X, Y), male(X).
sister(X, Y) :- sibling(X, Y), female(X).
uncle(X, Y) :- brother(X, Z), parent(Z, Y).
aunt(X, Y) :- sister(X, Z), parent(Z, Y).

% Gender facts
male(arun).
male(ganpat).
male(umesh).
male(mahesh).
male(bhalchandra).
male(prashant).
male(prakash).
male(neel).
male(ainav).

female(archana).
female(smita).
female(pratibha).
female(ashwini).
female(swara).
female(pallavi).
female(aiya).
