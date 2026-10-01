#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Monta as pastas do kit Rotina de PM com IA a partir dos arquivos "achatados" do repositorio.

No repositorio, cada arquivo fica na raiz com o caminho no nome:
    raiz_vault-modelo_.claude_skills_abrir-dia_SKILL.md  ->  vault-modelo/.claude/skills/abrir-dia/SKILL.md

Uso (rode na pasta onde estao os arquivos raiz_*):
    python3 montar_vault.py                         # monta ./kit-rotina-pm/
    python3 montar_vault.py --vault "CAMINHO"       # monta e copia vault-modelo/ para o seu vault
    python3 montar_vault.py --destino "CAMINHO"     # monta o kit em outro lugar

Nunca sobrescreve arquivos existentes: pula e avisa. Usa so a biblioteca padrao do Python 3.
"""
import argparse
import os
import shutil
import sys

# (nome no repositorio, caminho original)
MAPA = [
    ('raiz_guia_Prompts do Copilot.md', 'guia/Prompts do Copilot.md'),
    ('raiz_guia_Rotina de PM com IA.md', 'guia/Rotina de PM com IA.md'),
    ('raiz_guia_Setup passo a passo.md', 'guia/Setup passo a passo.md'),
    ('raiz_vault-modelo_.claude_skills_abrir-dia_SKILL.md', 'vault-modelo/.claude/skills/abrir-dia/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_comunicado_SKILL.md', 'vault-modelo/.claude/skills/comunicado/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_configurar-rubrica_SKILL.md', 'vault-modelo/.claude/skills/configurar-rubrica/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_configurar-template_SKILL.md', 'vault-modelo/.claude/skills/configurar-template/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_daily_SKILL.md', 'vault-modelo/.claude/skills/daily/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_demo_SKILL.md', 'vault-modelo/.claude/skills/demo/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_entrevista_SKILL.md', 'vault-modelo/.claude/skills/entrevista/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_fechar-dia_SKILL.md', 'vault-modelo/.claude/skills/fechar-dia/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_figjam_SKILL.md', 'vault-modelo/.claude/skills/figjam/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_historias_SKILL.md', 'vault-modelo/.claude/skills/historias/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_importar_SKILL.md', 'vault-modelo/.claude/skills/importar/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_metricas_SKILL.md', 'vault-modelo/.claude/skills/metricas/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_novo-tema_SKILL.md', 'vault-modelo/.claude/skills/novo-tema/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_okr_SKILL.md', 'vault-modelo/.claude/skills/okr/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_ppt_SKILL.md', 'vault-modelo/.claude/skills/ppt/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_prd_SKILL.md', 'vault-modelo/.claude/skills/prd/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_principio_SKILL.md', 'vault-modelo/.claude/skills/principio/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_refino_SKILL.md', 'vault-modelo/.claude/skills/refino/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_roadmap_SKILL.md', 'vault-modelo/.claude/skills/roadmap/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_semana_SKILL.md', 'vault-modelo/.claude/skills/semana/SKILL.md'),
    ('raiz_vault-modelo_.claude_skills_status_SKILL.md', 'vault-modelo/.claude/skills/status/SKILL.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema_Evidencias__modelo-evidencia.md', 'vault-modelo/02-Temas/_modelo-tema/Evidencias/_modelo-evidencia.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema_Metricas__dicionario.md', 'vault-modelo/02-Temas/_modelo-tema/Metricas/_dicionario.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema_OKRs__modelo-trimestre.md', 'vault-modelo/02-Temas/_modelo-tema/OKRs/_modelo-trimestre.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema_Principios__modelo-principio.md', 'vault-modelo/02-Temas/_modelo-tema/Principios/_modelo-principio.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema_Roadmap.md', 'vault-modelo/02-Temas/_modelo-tema/Roadmap.md'),
    ('raiz_vault-modelo_02-Temas__modelo-tema__contexto.md', 'vault-modelo/02-Temas/_modelo-tema/_contexto.md'),
    ('raiz_vault-modelo_04-Comunicacao_Exemplos__LEIA.md', 'vault-modelo/04-Comunicacao/Exemplos/_LEIA.md'),
    ('raiz_vault-modelo_04-Comunicacao_Power-Automate_exemplo-edicao.json', 'vault-modelo/04-Comunicacao/Power-Automate/exemplo-edicao.json'),
    ('raiz_vault-modelo_04-Comunicacao_Power-Automate_passo-a-passo.md', 'vault-modelo/04-Comunicacao/Power-Automate/passo-a-passo.md'),
    ('raiz_vault-modelo_04-Comunicacao_card-template.json', 'vault-modelo/04-Comunicacao/card-template.json'),
    ('raiz_vault-modelo_90-Config_config.md', 'vault-modelo/90-Config/config.md'),
    ('raiz_vault-modelo_90-Config_convencoes.md', 'vault-modelo/90-Config/convencoes.md'),
    ('raiz_vault-modelo_90-Config_ppt__LEIA.md', 'vault-modelo/90-Config/ppt/_LEIA.md'),
    ('raiz_vault-modelo_90-Config_ppt_como-gerar-ppt.md', 'vault-modelo/90-Config/ppt/como-gerar-ppt.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_01-lista-reunioes.md', 'vault-modelo/90-Config/prompts-copilot/01-lista-reunioes.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_02-extracao-diaria.md', 'vault-modelo/90-Config/prompts-copilot/02-extracao-diaria.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_03-daily.md', 'vault-modelo/90-Config/prompts-copilot/03-daily.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_04-revisao-documento.md', 'vault-modelo/90-Config/prompts-copilot/04-revisao-documento.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_05-respostas-comunicado.md', 'vault-modelo/90-Config/prompts-copilot/05-respostas-comunicado.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_06-extracao-historica.md', 'vault-modelo/90-Config/prompts-copilot/06-extracao-historica.md'),
    ('raiz_vault-modelo_90-Config_prompts-copilot_07-busca-documentos.md', 'vault-modelo/90-Config/prompts-copilot/07-busca-documentos.md'),
    ('raiz_vault-modelo_90-Config_rubrica-fontes__LEIA.md', 'vault-modelo/90-Config/rubrica-fontes/_LEIA.md'),
    ('raiz_vault-modelo_90-Config_rubrica-historias.md', 'vault-modelo/90-Config/rubrica-historias.md'),
    ('raiz_vault-modelo_90-Config_template-prd.md', 'vault-modelo/90-Config/template-prd.md'),
    ('raiz_vault-modelo_99-Templates_nota-diaria.md', 'vault-modelo/99-Templates/nota-diaria.md'),
    ('raiz_vault-modelo_99-Templates_reuniao-nao-prevista.md', 'vault-modelo/99-Templates/reuniao-nao-prevista.md'),
    ('raiz_vault-modelo_99-Templates_secao-reuniao.md', 'vault-modelo/99-Templates/secao-reuniao.md'),
    ('raiz_vault-modelo_A revisar.md', 'vault-modelo/A revisar.md'),
    ('raiz_vault-modelo_CLAUDE.md', 'vault-modelo/CLAUDE.md'),
]

# Pastas que existem vazias no kit (o vault usa)
PASTAS_VAZIAS = [
    'vault-modelo/00-Inbox/_entrada',
    'vault-modelo/00-Inbox/_processado',
    'vault-modelo/01-Diario',
    'vault-modelo/01-Diario/Semanas',
    'vault-modelo/02-Temas/_arquivo',
    'vault-modelo/02-Temas/_modelo-tema/Artefatos',
    'vault-modelo/02-Temas/_modelo-tema/Diagramas',
    'vault-modelo/02-Temas/_modelo-tema/Entregas',
    'vault-modelo/02-Temas/_modelo-tema/Historias',
    'vault-modelo/02-Temas/_modelo-tema/Historico',
    'vault-modelo/02-Temas/_modelo-tema/Metricas/Relatorios',
    'vault-modelo/02-Temas/_modelo-tema/PRDs',
    'vault-modelo/03-Backlog/Retratos',
    'vault-modelo/04-Comunicacao/Comunicados',
]


def copiar_sem_sobrescrever(origem, destino, relatorio):
    if os.path.exists(destino):
        relatorio["pulados"].append(destino)
        return
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    shutil.copy2(origem, destino)
    relatorio["criados"].append(destino)


def main():
    pasta_script = os.path.dirname(os.path.abspath(__file__))
    p = argparse.ArgumentParser(description="Monta as pastas do kit Rotina de PM com IA.")
    p.add_argument("--origem", default=pasta_script, help="pasta com os arquivos raiz_* (padrao: a pasta deste script)")
    p.add_argument("--destino", default=None, help="onde montar o kit (padrao: <origem>/kit-rotina-pm)")
    p.add_argument("--vault", default=None, help="raiz do seu vault do Obsidian: copia o conteudo de vault-modelo/ para la")
    p.add_argument("--forcar", action="store_true", help="aceita um --vault sem a pasta .obsidian")
    a = p.parse_args()

    origem = os.path.abspath(a.origem)
    destino = os.path.abspath(a.destino or os.path.join(origem, "kit-rotina-pm"))

    if a.vault:
        vault = os.path.abspath(a.vault)
        if not os.path.isdir(vault):
            sys.exit("ERRO: a pasta do vault nao existe: " + vault)
        if not os.path.isdir(os.path.join(vault, ".obsidian")) and not a.forcar:
            sys.exit("ERRO: nao achei a pasta .obsidian em " + vault +
                     "\nConfira se este e o caminho da raiz do vault. Se for mesmo, rode de novo com --forcar.")

    kit = {"criados": [], "pulados": []}
    faltando = []
    for nome, caminho in MAPA:
        arq = os.path.join(origem, nome)
        if not os.path.isfile(arq):
            faltando.append(nome)
            continue
        copiar_sem_sobrescrever(arq, os.path.join(destino, *caminho.split("/")), kit)
    for pasta in PASTAS_VAZIAS:
        os.makedirs(os.path.join(destino, *pasta.split("/")), exist_ok=True)

    conhecidos = {n for n, _ in MAPA}
    desconhecidos = sorted(f for f in os.listdir(origem) if f.startswith("raiz_") and f not in conhecidos)

    print("")
    print("KIT montado em: " + destino)
    print("  arquivos criados: %d | ja existiam (pulados): %d" % (len(kit["criados"]), len(kit["pulados"])))

    if a.vault:
        vm = {"criados": [], "pulados": []}
        base = os.path.join(destino, "vault-modelo")
        for nome, caminho in MAPA:
            if not caminho.startswith("vault-modelo/"):
                continue
            src = os.path.join(base, *caminho.split("/")[1:])
            if os.path.isfile(src):
                copiar_sem_sobrescrever(src, os.path.join(vault, *caminho.split("/")[1:]), vm)
        for pasta in PASTAS_VAZIAS:
            if pasta.startswith("vault-modelo/"):
                os.makedirs(os.path.join(vault, *pasta.split("/")[1:]), exist_ok=True)
        print("")
        print("VAULT atualizado: " + vault)
        print("  arquivos criados: %d | ja existiam (pulados): %d" % (len(vm["criados"]), len(vm["pulados"])))
        for f in vm["pulados"]:
            print("    pulado (ja existe): " + os.path.relpath(f, vault))

    if faltando:
        print("")
        print("ATENCAO: %d arquivo(s) nao encontrados na pasta de origem. Baixe e rode de novo:" % len(faltando))
        for f in faltando:
            print("    " + f)
    if desconhecidos:
        print("")
        print("Arquivos raiz_* que este script nao conhece (talvez de uma versao mais nova; baixe o montar_vault.py de novo):")
        for f in desconhecidos:
            print("    " + f)
    if not faltando:
        print("")
        print("Tudo certo. Proximo passo: plugins do Obsidian (Setup passo a passo, etapa 3).")


if __name__ == "__main__":
    main()
