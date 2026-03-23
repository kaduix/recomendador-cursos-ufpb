% Testes de consistência da base (PlUnit, SWI-Prolog).
% Executar a partir desta pasta:
%   swipl -q -g "consult(kb_tests), run_tests(knowledge_base), halt" -t halt

:- begin_tests(knowledge_base).
:- [main].

test(cada_curso_declarado_tem_area) :-
    forall(curso(C), once(area(C, _))).

test(cada_curso_tem_turno) :-
    forall(curso(C), once(turno(C, _))).

test(cada_curso_tem_campus) :-
    forall(curso(C), once(campus(C, _))).

test(cada_curso_tem_centro) :-
    forall(curso(C), once(centro(C, _))).

test(cada_curso_tem_grau) :-
    forall(curso(C), once(grau(C, _))).

test(cada_curso_tem_duracao) :-
    forall(curso(C), once(duracao(C, _))).

test(cada_curso_tem_carga_horaria) :-
    forall(curso(C), once(carga_horaria(C, _))).

test(cada_curso_tem_nota_corte) :-
    forall(curso(C), once(nota_corte(C, _))).

test(cada_curso_tem_modalidade) :-
    forall(curso(C), once(modalidade(C, _))).

test(cada_curso_tem_pelo_menos_um_indicado_para) :-
    forall(curso(C), once(indicado_para(C, _))).

:- end_tests(knowledge_base).
