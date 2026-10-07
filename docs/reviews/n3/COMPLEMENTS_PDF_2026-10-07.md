# Compléments après recoupement des PDF — 7 octobre 2026

Les lacunes du [recoupement PDF](RECOUPEMENT_PDF_2026-10-07.md) ont donné lieu à
**22 nouveaux QCM** : 10 secours, 6 orientation/milieu, 2 désaturation,
3 formation et 1 approfondissement hyperoxie. Le catalogue contient maintenant
**448 cartes : 308 dans N2 et 140 compléments dans N3**. La pertinence N3 est
explicitement portée par 344 cartes, dont 204 partagées avec N2.

Le [CSV du lot](COMPLEMENTS_PDF_2026-10-07.csv) relève l’ID, l’apport distinct et les
références de chaque ajout. Les cartes ont d’abord été rédigées en draft, puis relues
avant reviewed : contexte, chaque choix, réponse, explication et voisinage dans le
catalogue. Aucun objectif de nombre de cartes n’a été fixé.

## Décisions et vérifications factuelles

- RIFAP mai 2026 p.26 et PSE juillet 2026 p.273–274 : la ventilation initiale après
  noyade est distincte du refus des manœuvres destinées à vider les poumons. Le lot
  n’impose pas un nombre d’insufflations initiales que ces passages ne précisent pas.
- PSC p.27,30–33 : alternance adulte 30/2, cadence 100–120/min, profondeur environ
  5 cm sans dépasser 6 cm. Trois objectifs techniques différents, pas trois versions
  de la reconnaissance d’un arrêt cardiaque. Relâchement expliqué au verso.
- PSE p.113–115,143–145 : préparation du réservoir MHC et contrôle d’efficacité BAVU.
  Le débit RIFAP de 15 L/min pour l’accident subaquatique reste contextualisé ; les
  objectifs de SpO2 des autres situations ne le remplacent pas arbitrairement.
- PSC p.16–19,43–46 : garrot après compression inefficace sur un membre, objet pénétrant
  laissé en place, arrosage initial d’une brûlure thermique. Chaque cas précise la situation.
- PSE p.307 : rinçage initial à l’eau de mer pour les filaments de méduse. Le premier
  rinçage est distingué d’une application ultérieure de chaleur ; ni protocole universel
  d’envenimation ni traitement extrapolé pour tous les cnidaires.
- MFT décembre 2025 p.4,9,11,14 : formation, 3 m/tour d’horizon, profils inversés,
  nourrissage, discrétion et acclimatation. Le PDF officiel en ligne a confirmé l’édition
  locale. Les PDF PSC/PSE de juillet téléchargés le 6 octobre ont été relus localement ;
  l’outil web n’a pas pu rouvrir ces deux liens lors de ce lot.
- Acclimatation : distinction physiologique appuyée par la publication expérimentale
  *Influence of repeated daily diving on decompression stress* (2013, PMID 23771833)
  et la synthèse *Acclimatization to diving: a systematic review* (2021, PMID 33975403).
  La synthèse rapporte des résultats hétérogènes sur les bulles et des connaissances
  insuffisantes sur les mécanismes, la protection et la procédure optimale. Aucun
  nombre de plongées « protecteur », changement de demi-périodes ni préconditionnement
  opérationnel n’est prescrit. L’article Subaqua FFESSM de mai 2026 a été consulté,
  mais ses hypothèses mécanistiques ne sont pas présentées comme des certitudes.
- Milieu : trois nouvelles reconnaissances descriptives, vérifiées dans DORIS FFESSM :
  sar à tête noire (deux barres), livrée mâle de girelle commune et spirographe annélide.
  Les choix confrontent espèces voisines ou groupes confondus. Aucun média tiers n’a
  été copié : l’identification visuelle sur photos et la reconnaissance sur site restent
  des prolongements possibles, pas une compétence supposée acquise par ce lot.
- Hyperoxie : une carte de compréhension du risque neurologique aigu, recroisée avec
  DAN. Le cours Grenoble seul ne fait pas autorité. Aucun seuil de PO2 « sans risque »,
  procédure de crise en immersion ou qualification nitrox n’est extrapolé.

## Reprises et exclusions

Le corrigé de `n2-add-peau-001` nomme désormais le **cutis marmorata**, sans nouvelle
question. Les autres cartes existantes gardent leur contenu. Un contrôle contre HEAD
confirme la conservation des 426 IDs et des champs type, modèle Anki, niveaux et paquet.
Les trois modalités de certification ajoutées sont propres au parcours N3.
Les conditions d’accès aux qualifications isolées PA40/PE60, la totalité du PSC/PSE,
le CRR complet et la technique DEA ne sont pas ajoutés au programme du brevet N3.
Les raisonnements sur gaz, tables, GF et froid ne sont pas dupliqués.

## Portée de la clôture

Les objectifs théoriques prioritaires identifiés par l’audit sont désormais travaillés.
Le lot ne prétend pas transformer tous les PDF en cartes ni certifier les gestes pratiques.
Les notices fabricants demeurent contextuelles et le milieu appelle une adaptation locale.
La liste de lacunes de l’audit est un état avant implémentation ; consulter ce bilan pour
son traitement. Les IDs historiques et le préréglage du dépôt restent stables.

## Vérifications du lot

`make check` : 448 cartes valides, lint/format/types/schéma OK, 18 tests réussis
et un module optionnel ignoré. `make build` : 448 notes, aucun brouillon exclu.
Inspection des champs du `.apkg` : les 22 ajouts ont leurs choix et corrigés,
les paquets sont classiques et le préréglage conserve 10 nouvelles cartes par jour.
Aucun test ni modification dans l’interface d’Anki.
