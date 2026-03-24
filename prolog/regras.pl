% REGRAS DO SISTEMA v5

% score_interesses/3 — +2 se indicado_para; 0 caso contrário. Espelhado em app.py.
score_interesses(Curso, Interesse, 2) :-
    atom(Interesse),
    Interesse \= '',
    indicado_para(Curso, Interesse), !.
score_interesses(_, _, 0).


% label_afinidade/2 — legado (score absoluto). A UI usa _label_afinidade_normalizada() em app.py.
label_afinidade(Score, alta)  :- Score >= 4, !.
label_afinidade(Score, media) :- Score >= 2, !.
label_afinidade(_, baixa).


% Classificações auxiliares — inferência pura sobre fatos.
curso_curto(Curso)       :- duracao(Curso, D), D =< 4.
curso_longo(Curso)       :- duracao(Curso, D), D >= 5.
curso_noturno(Curso)     :- turno(Curso, noturno).
curso_integral(Curso)    :- turno(Curso, integral).
curso_tecnologico(Curso) :- indicado_para(Curso, tecnologia).
curso_saude(Curso)       :- area(Curso, saude).
curso_exatas(Curso)      :- area(Curso, exatas).
curso_humanas(Curso)     :- area(Curso, humanas).

mesmo_centro(C1, C2) :-
    curso(C1), curso(C2), C1 \= C2,
    centro(C1, Centro), centro(C2, Centro).

mesmo_campus(C1, C2) :-
    curso(C1), curso(C2), C1 \= C2,
    campus(C1, Cam), campus(C2, Cam).

% Parecidos por mesma área + interesse compartilhado.
cursos_similares(C1, C2) :-
    curso(C1), curso(C2), C1 \= C2,
    area(C1, A), area(C2, A),
    indicado_para(C1, I), indicado_para(C2, I).

% Parecidos por mesmo centro + mesma área.
cursos_similares_centro_area(C1, C2) :-
    curso(C1), curso(C2), C1 \= C2,
    centro(C1, Ce), centro(C2, Ce),
    area(C1, A), area(C2, A).
