% Each disease rule includes: disease(Plant, DiseaseName, [ListOfSymptoms])

% --- Tomato ---
disease(tomato, nitrogen_deficiency, [yellow_leaves, stunted_growth]).
disease(tomato, bacterial_wilt, [wilting, yellow_leaves]).
disease(tomato, early_blight, [leaf_spots, yellow_leaves]).

% --- Lettuce ---
disease(lettuce, downy_mildew, [yellow_leaves, leaf_spots]).
disease(lettuce, root_rot, [wilting, stunted_growth]).
disease(lettuce, bacterial_leaf_spot, [leaf_spots, yellow_leaves]).

% --- Potato ---
disease(potato, late_blight, [leaf_spots, wilting, dark_lesions]).
disease(potato, black_leg, [yellow_leaves, stem_rot, wilting]).
disease(potato, early_blight, [leaf_spots, stunted_growth]).

% --- Cucumber ---
disease(cucumber, powdery_mildew, [white_powdery_spots, yellow_leaves]).
disease(cucumber, downy_mildew, [leaf_spots, wilting]).
disease(cucumber, bacterial_wilt, [wilting, stunted_growth]).

% --- Pepper ---
disease(pepper, bacterial_spot, [leaf_spots, fruit_spots, yellow_leaves]).
disease(pepper, root_rot, [wilting, stunted_growth]).
disease(pepper, mosaic_virus, [yellow_leaves, distorted_leaves]).

% --- Corn ---
disease(corn, leaf_blight, [leaf_spots, yellow_stripes, wilting]).
disease(corn, gray_leaf_spot, [gray_spots, stunted_growth]).
disease(corn, rust, [orange_pustules, yellow_leaves]).

% --- Rice ---
disease(rice, blast, [leaf_spots, wilting, brown_lesions]).
disease(rice, bacterial_leaf_blight, [yellow_stripes, wilting]).
disease(rice, sheath_blight, [stem_lesions, stunted_growth]).

% --- Wheat ---
disease(wheat, leaf_rust, [rust_spots, yellow_patches]).
disease(wheat, powdery_mildew, [white_powdery_spots, stunted_growth]).
disease(wheat, take_all, [root_rot, wilting, stunted_growth]).

% --- Strawberry ---
disease(strawberry, gray_mold, [gray_fungus, fruit_rot]).
disease(strawberry, leaf_spot, [leaf_spots, yellow_halos]).
disease(strawberry, powdery_mildew, [white_powdery_spots, curling_leaves]).

% --- Bean ---
disease(bean, anthracnose, [dark_spots, leaf_spots, stem_lesions]).
disease(bean, rust, [orange_pustules, yellow_leaves]).
disease(bean, root_rot, [wilting, stunted_growth]).

% --- Grapevine ---
disease(grapevine, downy_mildew, [yellow_spots, gray_fungus, leaf_drop]).
disease(grapevine, powdery_mildew, [white_powdery_spots, curling_leaves]).
disease(grapevine, black_rot, [black_spots, fruit_rot, leaf_spots]).

% --- Apple ---
disease(apple, apple_scab, [dark_spots, leaf_curling, fruit_spots]).
disease(apple, powdery_mildew, [white_powdery_spots, yellow_leaves]).
disease(apple, fire_blight, [wilting, blackened_branches, leaf_burn]).

% --- Mango ---
disease(mango, anthracnose, [black_spots, fruit_rot, leaf_spots]).
disease(mango, powdery_mildew, [white_powdery_spots, young_leaf_drop]).
disease(mango, bacterial_canker, [leaf_spots, twig_dieback, oozing_gum]).

% Start plant disease detection  system
diagnose_disease :-
    
    write('Plant Disease Diagnosis Expert System'), nl,
    nl,
    write('Available plants:'), nl,
    write('  tomato, lettuce, potato, cucumber, pepper, corn,'), nl,
    write('  rice, wheat, strawberry, bean, grapevine, apple, mango'), nl,
    nl,
    write('Enter the plant type (end with a period): '), nl,
    read(Plant),
    diagnose(Plant).

diagnose(Plant) :-
    findall(D, disease(Plant, D, _), Diseases),
    (   Diseases = []
    ->  format('No data for the plant "~w".~n', [Plant])
    ;   collect_symptoms,
        find_best_match(Plant)
    ).

collect_symptoms :-
    nl,
    write('List the observed symptoms as a list.'), nl,
    write('Example: [yellow_leaves, wilting, leaf_spots].'), nl,
    read(SymptomList),
    retractall(symptom(_)),
    assert_symptoms(SymptomList).

assert_symptoms([]).
assert_symptoms([H|T]) :-
    assertz(symptom(H)),
    assert_symptoms(T).

find_best_match(Plant) :-
    findall((Disease, Score),
        ( disease(Plant, Disease, Symptoms),
            match_score(Symptoms, Score)
        ),
        Scores),
    sort(2, @>=, Scores, Sorted),
    report_diagnosis(Sorted).

match_score(SymptomList, Score) :-
    findall(S, symptom(S), InputSymptoms),
    intersection(SymptomList, InputSymptoms, Common),
    length(Common, Matches),
    length(SymptomList, Total),
    ( Total > 0 -> Score is (Matches / Total) * 100 ; Score is 0 ).

report_diagnosis([]) :-
    write('No possible diseases match the given symptoms.'), nl.

report_diagnosis([(Disease, Score)|_]) :-
    (   Score > 70
    ->  format('Most likely disease: ~w (~2f%% confidence).~n', [Disease, Score])
    ;   Score > 30
    ->  format('Possible disease: ~w (~2f%% confidence).~n', [Disease, Score]),
        write('More symptoms may be needed for a precise diagnosis.'), nl
    ;   write('No sufficient evidence for any disease.'), nl
    ).
