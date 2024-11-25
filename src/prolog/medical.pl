% Facts: Symptoms associated with diseases
has_symptom(fever, flu).
has_symptom(cough, flu).
has_symptom(sore_throat, flu).

has_symptom(headache, migraine).
has_symptom(nausea, migraine).
has_symptom(sensitivity_to_light, migraine).

has_symptom(chest_pain, heart_attack).
has_symptom(shortness_of_breath, heart_attack).
has_symptom(dizziness, heart_attack).

% Rules: Diagnosis based on symptoms
diagnose(Disease) :- 
    has_symptom(Symptom1, Disease),
    has_symptom(Symptom2, Disease),
    has_symptom(Symptom3, Disease),
    write('You might have: '), write(Disease), nl,
    write('Based on symptoms: '), write(Symptom1), write(', '), write(Symptom2), write(', '), write(Symptom3), nl.

% Queries
:- initialization(main).

main :-
    % Example query: diagnose flu
    has_symptom(Symptom, flu), 
    write('Flu symptom detected: '), write(Symptom), nl,
    fail; % Backtrack to list all symptoms of flu
    
    % Diagnose based on symptoms
    diagnose(flu),
    diagnose(migraine),
    diagnose(heart_attack),
    nl.
