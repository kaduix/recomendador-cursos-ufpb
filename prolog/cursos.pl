% BASE DE CONHECIMENTO — Cursos de Graduação da UFPB (v2)

% CURSOS
curso(ciencia_computacao).
curso(sistemas_informacao).
curso(engenharia_civil).
curso(engenharia_eletrica).
curso(medicina).
curso(enfermagem).
curso(farmacia).
curso(direito).
curso(administracao).
curso(psicologia).
curso(matematica).
curso(fisica).
curso(engenharia_computacao).
curso(arquitetura_urbanismo).
curso(odontologia).
curso(nutricao).
curso(fisioterapia).
curso(pedagogia).
curso(comunicacao_social).
curso(economia).

% ÁREAS
area(ciencia_computacao, exatas).
area(sistemas_informacao, exatas).
area(engenharia_civil, exatas).
area(engenharia_eletrica, exatas).
area(medicina, saude).
area(enfermagem, saude).
area(farmacia, saude).
area(psicologia, humanas).
area(direito, humanas).
area(administracao, humanas).
area(matematica, exatas).
area(fisica, exatas).
area(engenharia_computacao, exatas).
area(arquitetura_urbanismo, exatas).
area(odontologia, saude).
area(nutricao, saude).
area(fisioterapia, saude).
area(pedagogia, humanas).
area(comunicacao_social, humanas).
area(economia, humanas).

% TURNOS
turno(ciencia_computacao, integral).
turno(sistemas_informacao, noturno).
turno(engenharia_civil, integral).
turno(engenharia_eletrica, integral).
turno(medicina, integral).
turno(enfermagem, integral).
turno(farmacia, integral).
turno(direito, noturno).
turno(administracao, noturno).
turno(psicologia, integral).
turno(matematica, integral).
turno(fisica, integral).
turno(engenharia_computacao, integral).
turno(arquitetura_urbanismo, integral).
turno(odontologia, integral).
turno(nutricao, integral).
turno(fisioterapia, integral).
turno(pedagogia, noturno).
turno(comunicacao_social, noturno).
turno(economia, noturno).

% DURAÇÃO (anos)
duracao(ciencia_computacao, 4).
duracao(sistemas_informacao, 4).
duracao(engenharia_civil, 5).
duracao(engenharia_eletrica, 5).
duracao(medicina, 6).
duracao(enfermagem, 5).
duracao(farmacia, 5).
duracao(direito, 5).
duracao(administracao, 4).
duracao(psicologia, 5).
duracao(matematica, 4).
duracao(fisica, 4).
duracao(engenharia_computacao, 5).
duracao(arquitetura_urbanismo, 5).
duracao(odontologia, 5).
duracao(nutricao, 4).
duracao(fisioterapia, 5).
duracao(pedagogia, 4).
duracao(comunicacao_social, 4).
duracao(economia, 4).

% CAMPUS
campus(ciencia_computacao, campus1).
campus(sistemas_informacao, campus4).
campus(engenharia_civil, campus1).
campus(engenharia_eletrica, campus1).
campus(medicina, campus1).
campus(enfermagem, campus1).
campus(farmacia, campus1).
campus(direito, campus1).
campus(administracao, campus4).
campus(psicologia, campus1).
campus(matematica, campus1).
campus(fisica, campus1).
campus(engenharia_computacao, campus1).
campus(arquitetura_urbanismo, campus1).
campus(odontologia, campus1).
campus(nutricao, campus1).
campus(fisioterapia, campus1).
campus(pedagogia, campus4).
campus(comunicacao_social, campus1).
campus(economia, campus1).

% CENTRO ACADÊMICO
centro(ciencia_computacao, ci).
centro(sistemas_informacao, ccae).
centro(engenharia_civil, ct).
centro(engenharia_eletrica, ct).
centro(medicina, ccm).
centro(enfermagem, ccs).
centro(farmacia, ccs).
centro(direito, ccj).
centro(administracao, ccae).
centro(psicologia, cchla).
centro(matematica, ccen).
centro(fisica, ccen).
centro(engenharia_computacao, ci).
centro(arquitetura_urbanismo, ct).
centro(odontologia, ccs).
centro(nutricao, ccs).
centro(fisioterapia, ccs).
centro(pedagogia, ccae).
centro(comunicacao_social, ccta).
centro(economia, ccsa).

% GRAU
grau(ciencia_computacao, bacharelado).
grau(sistemas_informacao, bacharelado).
grau(engenharia_civil, bacharelado).
grau(engenharia_eletrica, bacharelado).
grau(medicina, bacharelado).
grau(enfermagem, bacharelado).
grau(farmacia, bacharelado).
grau(direito, bacharelado).
grau(administracao, bacharelado).
grau(psicologia, bacharelado).
grau(matematica, licenciatura).
grau(fisica, licenciatura).
grau(engenharia_computacao, bacharelado).
grau(arquitetura_urbanismo, bacharelado).
grau(odontologia, bacharelado).
grau(nutricao, bacharelado).
grau(fisioterapia, bacharelado).
grau(pedagogia, licenciatura).
grau(comunicacao_social, bacharelado).
grau(economia, bacharelado).

% CARGA HORÁRIA (horas)
carga_horaria(ciencia_computacao, 3000).
carga_horaria(sistemas_informacao, 3000).
carga_horaria(engenharia_civil, 3600).
carga_horaria(engenharia_eletrica, 3600).
carga_horaria(medicina, 7200).
carga_horaria(enfermagem, 4000).
carga_horaria(farmacia, 4000).
carga_horaria(direito, 3700).
carga_horaria(administracao, 3000).
carga_horaria(psicologia, 4000).
carga_horaria(matematica, 2800).
carga_horaria(fisica, 2800).
carga_horaria(engenharia_computacao, 3800).
carga_horaria(arquitetura_urbanismo, 3600).
carga_horaria(odontologia, 4200).
carga_horaria(nutricao, 3200).
carga_horaria(fisioterapia, 4000).
carga_horaria(pedagogia, 3200).
carga_horaria(comunicacao_social, 2800).
carga_horaria(economia, 3000).

% NOTA DE CORTE SIMULADA (ENEM, escala 0-1000)
nota_corte(ciencia_computacao, 680).
nota_corte(sistemas_informacao, 620).
nota_corte(engenharia_civil, 690).
nota_corte(engenharia_eletrica, 700).
nota_corte(medicina, 810).
nota_corte(enfermagem, 660).
nota_corte(farmacia, 670).
nota_corte(direito, 720).
nota_corte(administracao, 600).
nota_corte(psicologia, 660).
nota_corte(matematica, 610).
nota_corte(fisica, 600).
nota_corte(engenharia_computacao, 710).
nota_corte(arquitetura_urbanismo, 680).
nota_corte(odontologia, 730).
nota_corte(nutricao, 640).
nota_corte(fisioterapia, 650).
nota_corte(pedagogia, 580).
nota_corte(comunicacao_social, 610).
nota_corte(economia, 630).

% INTERESSES
indicado_para(ciencia_computacao, tecnologia).
indicado_para(ciencia_computacao, matematica).
indicado_para(ciencia_computacao, raciocinio_logico).

indicado_para(sistemas_informacao, tecnologia).
indicado_para(sistemas_informacao, gestao).
indicado_para(sistemas_informacao, organizacao).

indicado_para(engenharia_civil, matematica).
indicado_para(engenharia_civil, fisica).
indicado_para(engenharia_civil, construcao).

indicado_para(engenharia_eletrica, tecnologia).
indicado_para(engenharia_eletrica, matematica).
indicado_para(engenharia_eletrica, fisica).

indicado_para(medicina, biologia).
indicado_para(medicina, saude).
indicado_para(medicina, cuidado_com_pessoas).

indicado_para(enfermagem, biologia).
indicado_para(enfermagem, saude).
indicado_para(enfermagem, cuidado_com_pessoas).

indicado_para(farmacia, biologia).
indicado_para(farmacia, quimica).
indicado_para(farmacia, saude).

indicado_para(direito, leitura).
indicado_para(direito, argumentacao).
indicado_para(direito, leis).

indicado_para(administracao, negocios).
indicado_para(administracao, gestao).
indicado_para(administracao, organizacao).

indicado_para(psicologia, comportamento).
indicado_para(psicologia, escuta).
indicado_para(psicologia, cuidado_com_pessoas).

indicado_para(matematica, matematica).
indicado_para(matematica, raciocinio_logico).
indicado_para(matematica, ensino).

indicado_para(fisica, fisica).
indicado_para(fisica, matematica).
indicado_para(fisica, raciocinio_logico).

indicado_para(engenharia_computacao, tecnologia).
indicado_para(engenharia_computacao, matematica).
indicado_para(engenharia_computacao, fisica).

indicado_para(arquitetura_urbanismo, construcao).
indicado_para(arquitetura_urbanismo, artes).
indicado_para(arquitetura_urbanismo, matematica).

indicado_para(odontologia, saude).
indicado_para(odontologia, biologia).
indicado_para(odontologia, cuidado_com_pessoas).

indicado_para(nutricao, saude).
indicado_para(nutricao, biologia).
indicado_para(nutricao, quimica).

indicado_para(fisioterapia, saude).
indicado_para(fisioterapia, biologia).
indicado_para(fisioterapia, cuidado_com_pessoas).

indicado_para(pedagogia, ensino).
indicado_para(pedagogia, cuidado_com_pessoas).
indicado_para(pedagogia, leitura).

indicado_para(comunicacao_social, leitura).
indicado_para(comunicacao_social, argumentacao).
indicado_para(comunicacao_social, artes).

indicado_para(economia, matematica).
indicado_para(economia, negocios).
indicado_para(economia, organizacao).
