"""Montagem de query Prolog e parsing do formulário."""

from labels import AREAS, CAMPUS_LABELS, GRAUS, INTERESSES_LABELS, TURNOS


def montar_query(restricoes: dict) -> str:
    """Monta query Prolog atômica compatível com PySwip (cláusulas individuais)."""
    partes = ["curso(Curso)"]
    if restricoes.get("area") and restricoes["area"] in AREAS:
        partes.append(f"area(Curso, {restricoes['area']})")
    if restricoes.get("turno") and restricoes["turno"] in TURNOS:
        partes.append(f"turno(Curso, {restricoes['turno']})")
    if restricoes.get("campus") and restricoes["campus"] in CAMPUS_LABELS:
        partes.append(f"campus(Curso, {restricoes['campus']})")
    if restricoes.get("grau") and restricoes["grau"] in GRAUS:
        partes.append(f"grau(Curso, {restricoes['grau']})")
    if restricoes.get("duracao_max"):
        try:
            dur_max = int(restricoes["duracao_max"])
            if 1 <= dur_max <= 12:
                partes.append(f"duracao(Curso, D), D =< {dur_max}")
        except ValueError:
            pass
    if restricoes.get("nota_enem") is not None:
        try:
            ne = int(restricoes["nota_enem"])
            if 0 <= ne <= 1000:
                partes.append(f"nota_corte(Curso, Nc), Nc =< {ne}")
        except ValueError:
            pass
    if restricoes.get("carga_max") is not None:
        try:
            cm = int(restricoes["carga_max"])
            if 2000 <= cm <= 10000:
                partes.append(f"carga_horaria(Curso, H), H =< {cm}")
        except ValueError:
            pass
    return ", ".join(partes)


def parse_search_form(form):
    """Extrai restrições e interesses do formulário POST. Retorna (restricoes, interesses)."""
    restricoes = {}
    campos_validos = {
        "area": AREAS,
        "turno": TURNOS,
        "campus": CAMPUS_LABELS,
        "grau": GRAUS,
    }
    for campo in ("area", "turno", "campus", "grau", "duracao_max", "nota_enem", "carga_max"):
        v = form.get(campo, "").strip()
        if not v:
            continue
        if campo == "duracao_max":
            try:
                dur = int(v)
                if 1 <= dur <= 12:
                    restricoes[campo] = dur
            except ValueError:
                pass
        elif campo == "nota_enem":
            try:
                ne = int(v)
                if 0 <= ne <= 1000:
                    restricoes[campo] = ne
            except ValueError:
                pass
        elif campo == "carga_max":
            try:
                cm = int(v)
                if 2000 <= cm <= 10000:
                    restricoes[campo] = cm
            except ValueError:
                pass
        else:
            if v in campos_validos[campo]:
                restricoes[campo] = v

    interesses = []
    vistos = set()
    for i in form.getlist("interesses"):
        interesse = i.strip()
        if interesse and interesse in INTERESSES_LABELS and interesse not in vistos:
            interesses.append(interesse)
            vistos.add(interesse)
    return restricoes, interesses
