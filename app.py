# Sistema de Busca e Recomendação de Cursos — UFPB v5
# Flask + PySwip + SWI-Prolog

from pathlib import Path
from flask import Flask, render_template, request
from pyswip import Prolog

from form_query import montar_query, parse_search_form
from labels import AREAS, CAMPUS_LABELS, GRAUS, INTERESSES_LABELS, TURNOS

BASE_DIR   = Path(__file__).resolve().parent
PROLOG_DIR = BASE_DIR / "prolog"

app    = Flask(__name__)
prolog = Prolog()
prolog.consult(str(PROLOG_DIR / "main.pl"))

NOMES = {
    "ciencia_computacao":    "Ciência da Computação",
    "sistemas_informacao":   "Sistemas de Informação",
    "engenharia_civil":      "Engenharia Civil",
    "engenharia_eletrica":   "Engenharia Elétrica",
    "engenharia_computacao": "Engenharia de Computação",
    "arquitetura_urbanismo": "Arquitetura e Urbanismo",
    "matematica":            "Matemática",
    "fisica":                "Física",
    "medicina":              "Medicina",
    "enfermagem":            "Enfermagem",
    "farmacia":              "Farmácia",
    "odontologia":           "Odontologia",
    "nutricao":              "Nutrição",
    "fisioterapia":          "Fisioterapia",
    "psicologia":            "Psicologia",
    "direito":               "Direito",
    "administracao":         "Administração",
    "economia":              "Economia",
    "pedagogia":             "Pedagogia",
    "comunicacao_social":    "Comunicação Social",
}

CENTROS = {
    "ci":    "CI — Centro de Informática",
    "ct":    "CT — Centro de Tecnologia",
    "ccm":   "CCM — Centro de Ciências Médicas",
    "ccs":   "CCS — Centro de Ciências da Saúde",
    "ccj":   "CCJ — Centro de Ciências Jurídicas",
    "ccsa":  "CCSA — Centro de Ciências Sociais Aplicadas",
    "ccae":  "CCAE — Centro de Ciências Aplicadas e Educação",
    "cchla": "CCHLA — Centro de Ciências Humanas, Letras e Artes",
    "ccen":  "CCEN — Centro de Ciências Exatas e da Natureza",
    "ccta":  "CCTA — Centro de Comunicação, Turismo e Artes",
}

INTRODUCOES = {
    "ciencia_computacao": (
        "Forma profissionais para desenvolver software, sistemas e soluções tecnológicas. "
        "Combina raciocínio lógico, matemática e programação para resolver problemas complexos. "
        "Ampla atuação em tecnologia, startups, pesquisa e inteligência artificial."
    ),
    "sistemas_informacao": (
        "Une tecnologia da informação e gestão empresarial. Ideal para quem quer atuar "
        "na ponte entre TI e negócios. Forte demanda no mercado corporativo e setor público."
    ),
    "engenharia_civil": (
        "Responsável pelo projeto e execução de obras: pontes, edifícios, estradas e infraestrutura urbana. "
        "Exige base sólida em matemática e física, com constante demanda no mercado."
    ),
    "engenharia_eletrica": (
        "Atua no projeto de sistemas elétricos, eletrônicos e de automação. "
        "Da geração de energia à robótica e telecomunicações. Alta empregabilidade em indústrias e startups."
    ),
    "engenharia_computacao": (
        "Une engenharia elétrica e ciência da computação para projetar hardware e software embarcado. "
        "Atua em robótica, IoT e sistemas de tempo real. Alta demanda industrial."
    ),
    "arquitetura_urbanismo": (
        "Projeta espaços habitáveis, edificações e cidades com equilíbrio entre estética e funcionalidade. "
        "Combina técnica de engenharia com sensibilidade artística e visão urbanística."
    ),
    "matematica": (
        "Forma professores e pesquisadores com domínio do raciocínio lógico-dedutivo. "
        "Licenciatura essencial para a educação básica, com grande demanda por professores qualificados."
    ),
    "fisica": (
        "Explora as leis fundamentais do universo, da mecânica clássica à física quântica. "
        "Licenciatura voltada para a docência, com base sólida para pesquisa e pós-graduação."
    ),
    "medicina": (
        "Uma das graduações mais concorridas do Brasil. Forma médicos capacitados para diagnóstico, "
        "tratamento e prevenção de doenças. Seis anos de intensa dedicação, com internato clínico e cirúrgico."
    ),
    "enfermagem": (
        "Prepara enfermeiros para cuidar de pacientes em hospitais, postos de saúde e domicílios. "
        "Curso essencial ao sistema de saúde, com foco em cuidados diretos e gestão de equipes."
    ),
    "farmacia": (
        "Forma farmacêuticos para atuar em drogarias, laboratórios e indústria farmacêutica. "
        "Combina química, biologia e farmacologia. Profissional fundamental no desenvolvimento de medicamentos."
    ),
    "odontologia": (
        "Forma cirurgiões-dentistas para prevenção, diagnóstico e tratamento de doenças bucais. "
        "Abrange clínica geral, ortodontia e saúde pública. Alta autonomia profissional no mercado."
    ),
    "nutricao": (
        "Estuda a relação entre alimentação, saúde e doença. "
        "Forma nutricionistas para hospitais, clínicas, esporte e indústria alimentícia."
    ),
    "fisioterapia": (
        "Atua na reabilitação e prevenção de disfunções do movimento humano. "
        "Trabalha em hospitais, clínicas e esporte. Exige conhecimento profundo de anatomia e empatia."
    ),
    "psicologia": (
        "Estuda o comportamento humano, os processos mentais e as relações interpessoais. "
        "Forma psicólogos para clínicas, empresas, escolas e pesquisa."
    ),
    "direito": (
        "Estuda o ordenamento jurídico e a aplicação das leis na sociedade. "
        "Forma advogados, promotores, juízes e gestores públicos. Exige raciocínio argumentativo e leitura extensiva."
    ),
    "administracao": (
        "Capacita para gerir organizações públicas e privadas. "
        "Abrange finanças, marketing, recursos humanos e estratégia. Uma das graduações mais versáteis."
    ),
    "economia": (
        "Analisa a produção, distribuição e consumo de bens e serviços na sociedade. "
        "Forma economistas para bancos, consultorias, governo e pesquisa acadêmica."
    ),
    "pedagogia": (
        "Forma educadores para a educação infantil, ensino fundamental e gestão escolar. "
        "Licenciatura que reflete sobre os processos de ensino-aprendizagem e políticas educacionais."
    ),
    "comunicacao_social": (
        "Prepara profissionais para jornalismo, publicidade, relações públicas e produção audiovisual. "
        "Desenvolve competências em escrita, narrativa e estratégias de comunicação."
    ),
}

# Chaves espelham os átomos de área do Prolog. Psicologia → humanas (CCHLA).
CORES_AREA = {"exatas": "exatas", "saude": "saude", "humanas": "humanas"}

PARECIDOS_POR_CURSO = 3

# Predicados de regras.pl → rótulos na UI
BADGES_PROLOG = (
    ("curso_curto", "Até 4 anos"),
    ("curso_longo", "5+ anos"),
    ("curso_noturno", "Noturno"),
    ("curso_integral", "Integral"),
    ("curso_tecnologico", "Foco tecnologia"),
    ("curso_saude", "Perfil saúde"),
    ("curso_exatas", "Perfil exatas"),
    ("curso_humanas", "Perfil humanas"),
)

CURSOS_ORDENADOS_NOME = sorted(NOMES.items(), key=lambda kv: kv[1].casefold())


def _pl(val):
    """Normaliza resultado de query PySwip para string Python."""
    if isinstance(val, bytes):
        return val.decode("utf-8")
    return str(val)


def _coletar_fatos(ids: set[str]) -> dict:
    """Carrega fatos básicos em lote para reduzir queries por curso."""
    dados: dict[str, dict] = {
        "area": {}, "turno": {}, "campus": {}, "grau": {}, "centro": {},
        "duracao": {}, "carga_horaria": {}, "nota_corte": {}, "interesses": {},
    }
    if not ids:
        return dados

    specs = (
        ("area", "A"), ("turno", "T"), ("campus", "C"), ("grau", "G"),
        ("centro", "Ce"), ("duracao", "D"), ("carga_horaria", "H"), ("nota_corte", "N"),
    )
    for pred, var in specs:
        try:
            for r in prolog.query(f"{pred}(Curso, {var})"):
                curso_id = _pl(r["Curso"])
                if curso_id in ids:
                    dados[pred][curso_id] = _pl(r[var])
        except Exception as e:
            app.logger.warning("Prolog ao coletar %s: %s", pred, e)

    try:
        for r in prolog.query("indicado_para(Curso, I)"):
            curso_id = _pl(r["Curso"])
            if curso_id in ids:
                dados["interesses"].setdefault(curso_id, []).append(_pl(r["I"]))
    except Exception as e:
        app.logger.warning("Prolog ao coletar indicado_para: %s", e)

    return dados


def _coletar_mapa_parecidos(predicado: str) -> dict[str, set[str]]:
    """Agrupa C2 por C1 para um predicado simétrico de pares."""
    bruto: dict[str, set[str]] = {}
    try:
        for r in prolog.query(f"{predicado}(C1, C2)"):
            c1 = _pl(r["C1"])
            c2 = _pl(r["C2"])
            bruto.setdefault(c1, set()).add(c2)
    except Exception as e:
        app.logger.warning("Prolog ao coletar %s: %s", predicado, e)
    return bruto


def _coletar_parecidos(ids: set[str], limite: int = PARECIDOS_POR_CURSO) -> dict[str, list[str]]:
    """Recomendação em camadas: mesma área+interesse; depois mesmo centro+área."""
    if not ids:
        return {}

    def _nome(cid: str) -> str:
        return NOMES.get(cid, cid.replace("_", " ").title())

    mapas = (
        _coletar_mapa_parecidos("cursos_similares"),
        _coletar_mapa_parecidos("cursos_similares_centro_area"),
    )

    out: dict[str, list[str]] = {}
    for cid in ids:
        vistos: list[str] = []
        visto_set: set[str] = set()
        for mp in mapas:
            candidatos = sorted((mp.get(cid, set()) - {cid}) - visto_set, key=_nome)
            for c2 in candidatos:
                if len(vistos) >= limite:
                    break
                vistos.append(c2)
                visto_set.add(c2)
            if len(vistos) >= limite:
                break
        out[cid] = vistos[:limite]
    return out


def _coletar_badges_prolog(ids: set[str]) -> dict[str, list[str]]:
    """Consulta predicados auxiliares de regras.pl para selos de classificação."""
    out: dict[str, list[str]] = {cid: [] for cid in ids}
    if not ids:
        return out
    for pred, label in BADGES_PROLOG:
        try:
            for r in prolog.query(f"{pred}(Curso)"):
                cid = _pl(r["Curso"])
                if cid in ids:
                    out[cid].append(label)
        except Exception as e:
            app.logger.warning("Prolog ao coletar badge %s: %s", pred, e)
    return out


def _label_afinidade_normalizada(score: int, n_interesses: int) -> str:
    """Rótulo relativo ao máximo possível (2 pts por interesse marcado)."""
    if n_interesses <= 0 or score <= 0:
        return "baixa"
    max_score = 2 * n_interesses
    ratio = score / max_score
    if ratio >= 2 / 3:
        return "alta"
    if ratio >= 1 / 3:
        return "media"
    return "baixa"


def _calcular_score_de_indicados(interesses: list[str], interesses_curso: list[str]) -> int:
    """+2 por interesse do usuário presente em indicado_para do curso."""
    if not interesses:
        return 0
    return sum(2 for i in interesses if i in interesses_curso)


def _filtrar_parecidos_pelo_perfil(
    curso_id: str,
    parecidos_ids: list[str],
    interesses_usuario: list[str],
    interesses_por_curso: dict[str, list[str]],
) -> list[str]:
    """Filtra parecidos para compartilhar ao menos um eixo de interesse com o usuário."""
    if not interesses_usuario:
        return list(parecidos_ids)
    alvo = set(interesses_usuario) & set(interesses_por_curso.get(curso_id, []))
    if not alvo:
        return []
    out: list[str] = []
    for pid in parecidos_ids:
        comuns = alvo & set(interesses_por_curso.get(pid, []))
        if comuns:
            out.append(pid)
    return out


def _gerar_motivos(curso_id: str, restricoes: dict, interesses: list[str],
                   interesses_curso: list[str]) -> list[str]:
    """Gera frases explicando por que o curso apareceu nos resultados."""
    motivos = []

    if restricoes.get("area"):
        motivos.append(f"Pertence à área de {AREAS.get(restricoes['area'], restricoes['area'])}")

    if restricoes.get("turno"):
        motivos.append(f"Ofertado no turno {str(TURNOS.get(restricoes['turno'], restricoes['turno'])).lower()}")

    if restricoes.get("campus"):
        motivos.append(f"Disponível no {str(CAMPUS_LABELS.get(restricoes['campus'], restricoes['campus']))}")

    if restricoes.get("grau"):
        motivos.append(f"Grau: {str(GRAUS.get(restricoes['grau'], restricoes['grau'])).lower()}")

    if restricoes.get("duracao_max") is not None:
        motivos.append(f"Duração máxima de {restricoes['duracao_max']} anos (filtro aplicado)")

    if restricoes.get("nota_enem") is not None:
        motivos.append(
            f"Nota de corte de referência até {restricoes['nota_enem']} (ENEM — seu valor informado; predicado nota_corte/2)"
        )

    if restricoes.get("carga_max") is not None:
        motivos.append(f"Carga horária até {restricoes['carga_max']}h (predicado carga_horaria/2)")

    for i in interesses:
        if i in interesses_curso:
            motivos.append(f"Compatível com seu interesse em {str(INTERESSES_LABELS.get(i, i)).lower()}")

    return motivos


def _enriquecer(
    curso_id: str,
    restricoes: dict,
    interesses: list[str],
    fatos: dict,
    parecidos_ids: list[str],
    badges_prolog: list[str],
) -> dict:
    """Constrói o dict completo de um curso para o template."""
    area_id = fatos["area"].get(curso_id, "")
    turno_id = fatos["turno"].get(curso_id, "")
    campus_id = fatos["campus"].get(curso_id, "")
    grau_id = fatos["grau"].get(curso_id, "")
    centro_id = fatos["centro"].get(curso_id, "")
    dur = fatos["duracao"].get(curso_id, "")
    carga = fatos["carga_horaria"].get(curso_id, "")
    nota = fatos["nota_corte"].get(curso_id, "")
    interesses_curso = fatos["interesses"].get(curso_id, [])

    score = _calcular_score_de_indicados(interesses, interesses_curso)
    max_score = 2 * len(interesses) if interesses else 0
    label = _label_afinidade_normalizada(score, len(interesses))
    motivos = _gerar_motivos(curso_id, restricoes, interesses, interesses_curso)
    interesses_alinhados = [
        str(INTERESSES_LABELS.get(i, i)) for i in interesses if i in interesses_curso
    ]

    ids_parecidos = _filtrar_parecidos_pelo_perfil(
        curso_id, parecidos_ids, interesses, fatos["interesses"]
    )
    parecidos = [
        {"id": pid, "nome": NOMES.get(pid, pid.replace("_", " ").title())}
        for pid in ids_parecidos
    ]

    return {
        "id":         curso_id,
        "nome":       NOMES.get(curso_id, curso_id.replace("_", " ").title()),
        "area_id":    area_id,
        "area":       AREAS.get(area_id, area_id),
        "turno":      TURNOS.get(turno_id, turno_id),
        "campus_id":  campus_id,
        "campus":     CAMPUS_LABELS.get(campus_id, campus_id),
        "grau":       GRAUS.get(grau_id, grau_id),
        "centro_id":  centro_id,
        "centro":     CENTROS.get(centro_id, centro_id.upper()),
        "duracao":    f"{dur} anos" if dur else "",
        "carga":      f"{carga}h" if carga else "",
        "nota_corte": str(nota) if nota else "",
        "interesses": [INTERESSES_LABELS.get(i, i) for i in interesses_curso],
        "interesses_ids": list(interesses_curso),
        "introducao": INTRODUCOES.get(curso_id, ""),
        "score":      score,
        "max_score":  max_score,
        "afinidade":  label,   # 'alta' | 'media' | 'baixa'
        "motivos":    motivos,
        "cor_area":   CORES_AREA.get(area_id, ""),
        "sem_interesse": bool(interesses) and score == 0,
        "parecidos":  parecidos,
        "badges_prolog": badges_prolog,
        "interesses_alinhados": interesses_alinhados,
    }


def buscar_cursos(restricoes: dict, interesses: list[str]) -> dict:
    """
    Retorna 'compativeis' (score > 0, ordenados por score desc) e
    'outros' (score == 0). Sem interesses, todos vão para 'compativeis'.
    """
    query = montar_query(restricoes)
    try:
        ids_raw = list(prolog.query(query))
    except Exception as e:
        app.logger.error(f"Erro na query Prolog: {e}")
        return {"compativeis": [], "outros": [], "compativeis_grupos": None}

    ids = list(dict.fromkeys(_pl(r["Curso"]) for r in ids_raw))
    id_set = set(ids)
    fatos = _coletar_fatos(id_set)
    parecidos_por_id = _coletar_parecidos(id_set)
    badges_por_id = _coletar_badges_prolog(id_set)
    cursos = [
        _enriquecer(cid, restricoes, interesses, fatos,
                    parecidos_por_id.get(cid, []), badges_por_id.get(cid, []))
        for cid in ids
    ]

    if not interesses:
        cursos.sort(key=lambda c: c["nome"])
        return {"compativeis": cursos, "outros": [], "compativeis_grupos": None}

    compativeis = sorted(
        [c for c in cursos if c["score"] > 0],
        key=lambda c: (-c["score"], c["nome"])
    )
    outros = sorted(
        [c for c in cursos if c["score"] == 0],
        key=lambda c: c["nome"]
    )
    grupos = None
    if len(interesses) > 1:
        grupos = []
        for ik in interesses:
            sub = sorted(
                [c for c in compativeis if ik in c.get("interesses_ids", [])],
                key=lambda c: (-c["score"], c["nome"]),
            )
            if sub:
                grupos.append({
                    "interesse_id": ik,
                    "interesse_label": str(INTERESSES_LABELS.get(ik, ik)),
                    "cursos": sub,
                })
        visto_anchor: set[str] = set()
        for g in grupos:
            for c in g["cursos"]:
                cid = c["id"]
                c["anchor_aqui"] = cid not in visto_anchor
                visto_anchor.add(cid)
    else:
        for c in compativeis:
            c["anchor_aqui"] = True
    for c in outros:
        c["anchor_aqui"] = True
    return {"compativeis": compativeis, "outros": outros, "compativeis_grupos": grupos}


def comparar_dois_cursos(c1: str, c2: str) -> dict:
    """Compara dois cursos via predicados Prolog e fatos indicado_para/2."""
    ids = {c1, c2}
    fatos = _coletar_fatos(ids)
    mesmo_campus = False
    mesmo_centro = False
    try:
        mesmo_campus = bool(list(prolog.query(f"mesmo_campus({c1}, {c2})")))
    except Exception as e:
        app.logger.warning("Prolog comparar campus: %s", e)
    try:
        mesmo_centro = bool(list(prolog.query(f"mesmo_centro({c1}, {c2})")))
    except Exception as e:
        app.logger.warning("Prolog comparar centro: %s", e)

    a1, a2 = fatos["area"].get(c1), fatos["area"].get(c2)
    mesma_area = bool(a1 and a2 and a1 == a2)

    i1 = set(fatos["interesses"].get(c1, []))
    i2 = set(fatos["interesses"].get(c2, []))
    comuns_atoms = sorted(i1 & i2)
    interesses_comuns = [str(INTERESSES_LABELS.get(x, x)) for x in comuns_atoms]

    return {
        "nome1": NOMES.get(c1, c1),
        "nome2": NOMES.get(c2, c2),
        "mesmo_campus": mesmo_campus,
        "mesmo_centro": mesmo_centro,
        "mesma_area": mesma_area,
        "area1": AREAS.get(a1 or "", a1 or ""),
        "area2": AREAS.get(a2 or "", a2 or ""),
        "interesses_comuns": interesses_comuns,
        "campus1": CAMPUS_LABELS.get(fatos["campus"].get(c1, ""), ""),
        "campus2": CAMPUS_LABELS.get(fatos["campus"].get(c2, ""), ""),
        "centro1": CENTROS.get(fatos["centro"].get(c1, ""), ""),
        "centro2": CENTROS.get(fatos["centro"].get(c2, ""), ""),
        "turno1": TURNOS.get(fatos["turno"].get(c1, ""), fatos["turno"].get(c1, "")),
        "turno2": TURNOS.get(fatos["turno"].get(c2, ""), fatos["turno"].get(c2, "")),
        "duracao1": fatos["duracao"].get(c1, ""),
        "duracao2": fatos["duracao"].get(c2, ""),
        "nota1": str(fatos["nota_corte"].get(c1, "")),
        "nota2": str(fatos["nota_corte"].get(c2, "")),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    resultado   = {"compativeis": [], "outros": []}
    restricoes  = {}
    interesses  = []
    total       = 0

    ids_na_pagina: set[str] = set()
    if request.method == "POST":
        restricoes, interesses = parse_search_form(request.form)
        resultado = buscar_cursos(restricoes, interesses)
        total = len(resultado["compativeis"]) + len(resultado["outros"])
        ids_na_pagina = {c["id"] for c in resultado["compativeis"]} | {
            c["id"] for c in resultado["outros"]
        }

    return render_template(
        "index.html",
        resultado=resultado,
        total=total,
        restricoes=restricoes,
        interesses=interesses,
        ids_na_pagina=ids_na_pagina,
        areas=AREAS,
        turnos=TURNOS,
        campus_opts=CAMPUS_LABELS,
        graus=GRAUS,
        interesses_opts=INTERESSES_LABELS,
    )


@app.route("/comparar", methods=["GET"])
def comparar():
    c1 = (request.args.get("c1") or "").strip()
    c2 = (request.args.get("c2") or "").strip()
    resultado_cmp = None
    erro = None
    if c1 or c2:
        if not c1 or not c2:
            erro = "Selecione dois cursos para comparar."
        elif c1 == c2:
            erro = "Escolha dois cursos diferentes."
        elif c1 not in NOMES or c2 not in NOMES:
            erro = "Curso inválido."
        else:
            resultado_cmp = comparar_dois_cursos(c1, c2)
    return render_template(
        "comparar.html",
        cursos_opts=CURSOS_ORDENADOS_NOME,
        c1=c1,
        c2=c2,
        resultado=resultado_cmp,
        erro=erro,
    )


if __name__ == "__main__":
    app.run(debug=True, threaded=False)  # threaded=False evita crashes do PySwip
