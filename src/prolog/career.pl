% Facts: Interests and associated careers
has_interest(programming, software_engineer).
has_interest(mathematics, data_scientist).
has_interest(art, graphic_designer).
has_interest(communication, public_relations_officer).
has_interest(writing, journalist).
has_interest(science, researcher).

has_skill(coding, software_engineer).
has_skill(statistics, data_scientist).
has_skill(illustration, graphic_designer).
has_skill(networking, public_relations_officer).
has_skill(storytelling, journalist).
has_skill(experimentation, researcher).

% Rules: Career suggestions based on interests and skills
suggest_career(Career) :- 
    has_interest(Interest, Career),
    has_skill(Skill, Career),
    write('You might excel as a: '), write(Career), nl,
    write('Based on your interest in: '), write(Interest), nl,
    write('And your skill in: '), write(Skill), nl.

% Queries
:- initialization(main).

main :-
    % Example: List potential careers based on interests and skills
    has_interest(Interest, Career),
    write('Career: '), write(Career), nl,
    write('  Interest: '), write(Interest), nl,
    fail; % Backtrack to find all interests and careers

    % Suggest careers based on both interests and skills
    suggest_career(software_engineer),
    suggest_career(data_scientist),
    suggest_career(graphic_designer),
    nl.
