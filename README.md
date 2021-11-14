# IWMA42-devops-crypto

Petite application flask utilisant une API coinsgeeko pour afficher des cryptomonnaies.

La CI/CD se déroule de la même manière pour la prod et la pré-prod : 
  - un build avec l'installation python et les requirements
  - un linter avec pylint
  - un test avec pytest
  - un deploy sur les app heroku
