import requests
from bs4 import BeautifulSoup
import traceback

base_url = "https://travaillerpour.be/fr/job"

codeString = 'AFG23'
for i in range(1, 999):
    try:
        num = "{:03}".format(i)
        codeFinal = codeString + str(num)
        job_url = f"{base_url}?jobcode={codeFinal}"

        # obtenir le contenu de la page de l'offre d'emploi
        response = requests.get(job_url)
        content = response.content
        wordFinder = '<a href="/fr/jobs" title="Jobs">Jobs</a>'
        # print("Content : " + str(content))

        if content is not None and wordFinder in str(content):
            # analyser le contenu HTML avec BeautifulSoup
            soup = BeautifulSoup(content, "html.parser")

            # extraire les informations souhaitées
            code = soup.find("div",
                             attrs="field field--name-field-job-selectioncode field--type-string field--label-above").find(
                "div", attrs="field__item")

            language = soup.find("div",
                                 attrs="field field--name-field-langcode field--type-entity-reference field--label-above").find(
                "div", attrs="field__item")
            rectrutement = soup.find("div",
                                     attrs="field field--name-field-job-recruitmentprocedures field--type-entity-reference field--label-above")

            niveau_fonction = soup.find("div",
                                        attrs="field field--name-field-job-functiondegree-clone field--type-entity-reference field--label-above").find(
                "div", attrs="field__item")

            fonction = soup.find("div",
                                 attrs="node__header--left").find("h1", attrs="node__title").find("span", attrs="")

            organisation = soup.find("span",
                                     attrs="organization-name")

            date = soup.find("p", attrs="apply-till")

            numberPoste = soup.find("div",
                                    attrs="field field--name-field-job-openvacancies field--type-integer field--label-visually_hidden") \
                .find("div", attrs="field__item")

            print(str(i) + ") URL : " + job_url)
            print("Code : " + code.text.upper())
            print("Organisation : " + organisation.text.strip())
            print("Fonction : " + fonction.text.strip())
            print("Niveau : " + niveau_fonction.text.replace("\n", " ").strip())
            print(numberPoste.text.replace("\n", "").strip())
            print(rectrutement.text.replace("\n", " ").strip())
            print("Langue : " + language.text.upper().replace("\n", " ").strip())
            print(date.text.replace("\n", "").replace("   ", "").strip())
            print("---------------------------------------")
        else:
            print(str(i) + ") No content : " "URL : " + job_url)
            print("")

    except AttributeError:
        traceback.print_exc()
        continue
