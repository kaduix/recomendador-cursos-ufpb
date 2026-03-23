"""
Integração com SWI-Prolog (PySwip). Marcados para pular se o motor não estiver disponível.
"""

import pytest

pytest.importorskip("pyswip", reason="pyswip não instalado")


def _prolog_disponivel() -> bool:
    try:
        from pathlib import Path

        from pyswip import Prolog

        base = Path(__file__).resolve().parent.parent
        p = Prolog()
        p.consult(str(base / "prolog" / "main.pl"))
        next(p.query("curso(ciencia_computacao)"))
        return True
    except Exception:
        return False


needs_prolog = pytest.mark.skipif(
    not _prolog_disponivel(),
    reason="SWI-Prolog indisponível ou consult falhou",
)


@needs_prolog
def test_buscar_cursos_exatas_tecnologia():
    import app as app_module

    out = app_module.buscar_cursos(
        {"area": "exatas"},
        ["tecnologia"],
    )
    ids_comp = {c["id"] for c in out["compativeis"]}
    ids_outros = {c["id"] for c in out["outros"]}
    assert "ciencia_computacao" in ids_comp
    assert ids_comp.isdisjoint(ids_outros)
    cc = next(c for c in out["compativeis"] if c["id"] == "ciencia_computacao")
    assert cc["score"] >= 2
    assert cc["afinidade"] in ("alta", "media", "baixa")
    ids_p = {p["id"] for p in cc.get("parecidos", [])}
    # Até 3 sugestões; com perfil "tecnologia", só parecidos que também têm tecnologia nos indicado_para.
    assert len(cc["parecidos"]) <= 3
    assert "engenharia_computacao" in ids_p or "engenharia_eletrica" in ids_p
    assert all("nome" in p for p in cc["parecidos"])


@needs_prolog
def test_buscar_varios_interesses_separa_grupos_na_resposta():
    import app as app_module

    out = app_module.buscar_cursos({}, ["tecnologia", "comportamento"])
    assert out["compativeis_grupos"] is not None
    ids_grupos = {g["interesse_id"] for g in out["compativeis_grupos"]}
    assert "tecnologia" in ids_grupos
    assert "comportamento" in ids_grupos
    g_tec = next(g for g in out["compativeis_grupos"] if g["interesse_id"] == "tecnologia")
    g_com = next(g for g in out["compativeis_grupos"] if g["interesse_id"] == "comportamento")
    assert any(c["id"] == "ciencia_computacao" for c in g_tec["cursos"])
    assert any(c["id"] == "psicologia" for c in g_com["cursos"])
    assert "psicologia" not in {c["id"] for c in g_tec["cursos"]}


@needs_prolog
def test_buscar_cursos_sem_interesses_todos_em_compativeis():
    import app as app_module

    out = app_module.buscar_cursos({"area": "humanas"}, [])
    assert out["outros"] == []
    assert len(out["compativeis"]) >= 1


@needs_prolog
def test_label_afinidade_normalizada():
    import app as app_module

    assert app_module._label_afinidade_normalizada(0, 1) == "baixa"
    assert app_module._label_afinidade_normalizada(2, 1) == "alta"
    assert app_module._label_afinidade_normalizada(2, 3) == "media"
    assert app_module._label_afinidade_normalizada(4, 3) == "alta"


@needs_prolog
def test_flask_post_retorna_resultados(flask_client):
    rv = flask_client.post(
        "/",
        data={
            "area": "exatas",
            "interesses": "tecnologia",
        },
        follow_redirects=True,
    )
    assert rv.status_code == 200
    body = rv.data.decode("utf-8")
    assert "Ciência da Computação" in body or "ciencia_computacao" in body
    assert "Cursos parecidos" in body


@needs_prolog
def test_comparar_pagina_ok(flask_client):
    rv = flask_client.get(
        "/comparar",
        query_string={"c1": "ciencia_computacao", "c2": "sistemas_informacao"},
    )
    assert rv.status_code == 200
    body = rv.data.decode("utf-8")
    assert "Ciência da Computação" in body
    assert "Sistemas de Informação" in body
    assert "mesmo_campus" in body


@needs_prolog
def test_buscar_com_filtro_nota_corte():
    import app as app_module

    out = app_module.buscar_cursos({"nota_enem": 650}, [])
    ids = {c["id"] for c in out["compativeis"]}
    assert "medicina" not in ids
    assert "pedagogia" in ids


@needs_prolog
def test_badges_prolog_presentes():
    import app as app_module

    out = app_module.buscar_cursos({}, [])
    med = next(c for c in out["compativeis"] if c["id"] == "medicina")
    assert any("5+" in b or "anos" in b for b in med["badges_prolog"])
