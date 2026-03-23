"""Testes unitários de montagem de query e parsing — não carregam Prolog."""

import pytest
from werkzeug.datastructures import ImmutableMultiDict

from form_query import montar_query, parse_search_form


class TestMontarQuery:
    def test_sem_restricoes(self):
        assert montar_query({}) == "curso(Curso)"

    def test_area_valida(self):
        q = montar_query({"area": "exatas"})
        assert q == "curso(Curso), area(Curso, exatas)"

    def test_area_invalida_ignorada(self):
        assert montar_query({"area": "sql_injection"}) == "curso(Curso)"

    def test_combinacao_filtros(self):
        q = montar_query({
            "area": "saude",
            "turno": "integral",
            "campus": "campus1",
            "grau": "bacharelado",
        })
        assert "curso(Curso)" in q
        assert "area(Curso, saude)" in q
        assert "turno(Curso, integral)" in q
        assert "campus(Curso, campus1)" in q
        assert "grau(Curso, bacharelado)" in q

    def test_duracao_max_valida(self):
        q = montar_query({"duracao_max": 4})
        assert "duracao(Curso, D), D =< 4" in q

    def test_duracao_max_fora_faixa(self):
        assert "duracao" not in montar_query({"duracao_max": 0})
        assert "duracao" not in montar_query({"duracao_max": 99})

    def test_duracao_max_string_invalida(self):
        assert montar_query({"duracao_max": "x"}) == "curso(Curso)"

    def test_nota_enem_valida(self):
        q = montar_query({"nota_enem": 680})
        assert "nota_corte(Curso, Nc), Nc =< 680" in q

    def test_nota_enem_fora_faixa(self):
        assert "nota_corte" not in montar_query({"nota_enem": -1})
        assert "nota_corte" not in montar_query({"nota_enem": 1001})

    def test_carga_max_valida(self):
        q = montar_query({"carga_max": 3600})
        assert "carga_horaria(Curso, H), H =< 3600" in q

    def test_carga_max_fora_faixa(self):
        assert "carga_horaria" not in montar_query({"carga_max": 1999})
        assert "carga_horaria" not in montar_query({"carga_max": 10001})


class TestParseSearchForm:
    def test_vazio(self):
        form = ImmutableMultiDict([])
        r, i = parse_search_form(form)
        assert r == {}
        assert i == []

    def test_restricoes_validas(self):
        form = ImmutableMultiDict([
            ("area", "humanas"),
            ("turno", "noturno"),
            ("campus", "campus4"),
            ("grau", "bacharelado"),
            ("duracao_max", "5"),
        ])
        r, i = parse_search_form(form)
        assert r == {
            "area": "humanas",
            "turno": "noturno",
            "campus": "campus4",
            "grau": "bacharelado",
            "duracao_max": 5,
        }
        assert i == []

    def test_restricoes_invalidas_ignoradas(self):
        form = ImmutableMultiDict([
            ("area", "inexistente"),
            ("turno", ""),
            ("duracao_max", "abc"),
        ])
        r, _ = parse_search_form(form)
        assert r == {}

    def test_interesses_dedup_e_whitelist(self):
        form = ImmutableMultiDict([
            ("interesses", "tecnologia"),
            ("interesses", "tecnologia"),
            ("interesses", "matematica"),
            ("interesses", "campo_falso"),
        ])
        r, i = parse_search_form(form)
        assert r == {}
        assert i == ["tecnologia", "matematica"]

    def test_nota_enem_e_carga_max(self):
        form = ImmutableMultiDict([
            ("nota_enem", "680"),
            ("carga_max", "4000"),
        ])
        r, i = parse_search_form(form)
        assert r == {"nota_enem": 680, "carga_max": 4000}
        assert i == []
