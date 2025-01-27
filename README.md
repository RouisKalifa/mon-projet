Bienvenue dans ce parcours pratique pour apprendre Docker ! Ce projet a pour objectif de déployer une application web simple à l'aide de Docker et Docker Compose.
Objectif final

Déployer une application web simple (basée sur Flask) et une base de données MySQL dans un environnement conteneurisé à l'aide de Docker et Docker Compose.
Prérequis

Avant de commencer, assurez-vous que Docker et Docker Compose sont installés sur votre machine.
Exercices Docker pour Débutants

Bienvenue dans ce parcours pratique pour apprendre Docker ! Ce projet a pour objectif de déployer une application web simple à l'aide de Docker et Docker Compose.
Objectif final

Déployer une application web simple (basée sur Flask) et une base de données MySQL dans un environnement conteneurisé à l'aide de Docker et Docker Compose.
Prérequis

Avant de commencer, assurez-vous que Docker et Docker Compose sont installés sur votre machine.

    Docker : Installation Docker
    Docker Compose : Installation Docker Compose

Étapes d'exécution
1. Cloner ce projet

Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

git clone https://github.com/votre-utilisateur/mon-projet.git
cd mon-projet

2. Vérifier l'installation de Docker

Avant de commencer à utiliser Docker, assurez-vous qu'il est installé et fonctionne correctement sur votre machine. Vérifiez la version de Docker avec la commande suivante :

docker --version

3. Construction de l'image Docker pour l'application Flask

Une fois le projet cloné, vous devez construire l'image Docker de l'application Flask.

    Créer l'image Docker : Pour cela, vous devez avoir un fichier Dockerfile dans votre répertoire. Exécutez la commande suivante pour construire l'image :

docker build -t flask-app .

Tester l'image Docker : Après la construction de l'image, vous pouvez tester l'application Flask en exécutant un conteneur basé sur cette image. Utilisez la commande suivante pour lancer le conteneur :

sudo docker run -p 8000:8000 flask-app

Accéder à l'application : Ouvrez votre navigateur et allez à l'adresse suivante pour tester l'application :

    http://localhost:8000/

4. Utiliser Docker Compose pour gérer les services

    Créer un fichier docker-compose.yml : Ce fichier permet de configurer les services nécessaires à votre projet (comme l'application Flask et la base de données MySQL). Assurez-vous d'avoir un fichier docker-compose.yml dans votre répertoire.

    Lancer les services : Exécutez tous les services définis dans votre fichier docker-compose.yml avec la commande suivante :

docker-compose up

Vérifier l'application Flask et la base de données : Une fois les services lancés, l'application Flask devrait être accessible sur http://localhost:8000/, et elle doit être connectée à la base de données MySQL.

Vérifier les logs des conteneurs : Si vous rencontrez des problèmes, vous pouvez inspecter les logs des conteneurs pour déboguer. Utilisez les commandes suivantes pour voir les logs des conteneurs :

    docker logs mon-projet_flask-app_1
    docker logs mysql_db

5. Optimisation et nettoyage
Exercices Docker pour Débutants

Bienvenue dans ce parcours pratique pour apprendre Docker ! Ce projet a pour objectif de déployer une application web simple à l'aide de Docker et Docker Compose.
Objectif final

Déployer une application web simple (basée sur Flask) et une base de données MySQL dans un environnement conteneurisé à l'aide de Docker et Docker Compose.
Prérequis

Avant de commencer, assurez-vous que Docker et Docker Compose sont installés sur votre machine.

    Docker : Installation Docker
    Docker Compose : Installation Docker Compose

Étapes d'exécution
1. Cloner ce projet

Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

git clone https://github.com/votre-utilisateur/mon-projet.git
cd mon-projet

2. Vérifier l'installation de Docker

Avant de commencer à utiliser Docker, assurez-vous qu'il est installé et fonctionne correctement sur votre machine. Vérifiez la version de Docker avec la commande suivante :

docker --version

3. Construction de l'image Docker pour l'application Flask

Une fois le projet cloné, vous devez construire l'image Docker de l'application Flask.

    Créer l'image Docker : Pour cela, vous devez avoir un fichier Dockerfile dans votre répertoire. Exécutez la commande suivante pour construire l'image :

docker build -t flask-app .

Tester l'image Docker : Après la construction de l'image, vous pouvez tester l'application Flask en exécutant un conteneur basé sur cette image. Utilisez la commande suivante pour lancer le conteneur :

sudo docker run -p 8000:8000 flask-app

Accéder à l'application : Ouvrez votre navigateur et allez à l'adresse suivante pour tester l'application :

    http://localhost:8000/

4. Utiliser Docker Compose pour gérer les services

    Créer un fichier docker-compose.yml : Ce fichier permet de configurer les services nécessaires à votre projet (comme l'application Flask et la base de données MySQL). Assurez-vous d'avoir un fichier docker-compose.yml dans votre répertoire.

    Lancer les services : Exécutez tous les services définis dans votre fichier docker-compose.yml avec la commande suivante :

docker-compose up

Vérifier l'application Flask et la base de données : Une fois les services lancés, l'application Flask devrait être accessible sur http://localhost:8000/, et elle doit être connectée à la base de données MySQL.

Vérifier les logs des conteneurs : Si vous rencontrez des problèmes, vous pouvez inspecter les logs des conteneurs pour déboguer. Utilisez les commandes suivantes pour voir les logs des conteneurs :

    docker logs mon-projet_flask-app_1
    docker logs mysql_db

5. Optimisation et nettoyage

    Optimisation de l'image Docker : Vous pouvez réduire la taille de votre image Docker en utilisant des images de base légères, comme alpine. Assurez-vous également de nettoyer les fichiers temporaires et de combiner les instructions dans le Dockerfile pour réduire les couches.

    Nettoyage de votre environnement Docker : Après avoir travaillé avec Docker, vous pouvez nettoyer les images et les conteneurs inutilisés avec les commandes suivantes :

    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)

6. Publier l'image sur Docker Hub

    Créer un compte Docker Hub : Si ce n'est pas déjà fait, créez un compte Docker Hub ici : Docker Hub.

    Taguer et pousser l'image : Une fois l'image construite, vous pouvez la pousser sur Docker Hub. Utilisez les commandes suivantes pour taguer et pousser l'image vers votre dépôt Docker Hub :

    docker tag flask-app votre-utilisateur/mon-projet_flask-app:latest
    docker push votre-utilisateur/mon-projet_flask-app

7. Variables d'environnement et personnalisation

Si vous devez ajouter des variables d'environnement à votre application Flask, vous pouvez les passer au moment de l'exécution avec la commande -e. Par exemple :

sudo docker run -e PORT=8000 -p 8000:8000 flask-app

Conclusion

Vous avez maintenant une application Flask qui fonctionne dans un conteneur Docker, avec une base de données MySQL, et vous avez appris à utiliser Docker Compose pour gérer plusieurs services. Vous pouvez également pousser votre image sur Docker Hub pour la partager avec d'autres.
    Optimisation de l'image Docker : Vous pouvez réduire la taille de votre image Docker en utilisant des images de base légères, comme alpine. Assurez-vous également de nettoyer les fichiers temporaires et de combiner les instructions dans le Dockerfile pour réduire les couches.

    Nettoyage de votre environnement Docker : Après avoir travaillé avec Docker, vous pouvez nettoyer les images et les conteneurs inutilisés avec les commandes suivantes :

    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)

6. Publier l'image sur Docker Hub

    Créer un compte Docker Hub : Si ce n'est pas déjà fait, créez un compte Docker Hub ici : Docker Hub.

    Taguer et pousser l'image : Une fois l'image construite, vous pouvez la pousser sur Docker Hub. Utilisez les commandes suivantes pour taguer et pousser l'image vers votre dépôt Docker Hub :

    docker tag flask-app votre-utilisateur/mon-projet_flask-app:latest
    docker push votre-utilisateur/mon-projet_flask-app

7. Variables d'environnement et personnalisation

Si vous devez ajouter des variables d'environnement à votre application Flask, vous pouvez les passer au moment de l'exécution avec la commande -e. Par exemple :

sudo docker run -e PORT=8000 -p 8000:8000 flask-app

Conclusion

Vous avez maintenant une application Flask qui fonctionne dans un conteneur Docker, avec une base de données MySQL, et vous avez appris à utiliser Docker Compose pour gérer plusieurs services. Vous pouvez également pousser votre image sur Docker Hub pour la partager avec d'autres.
    Docker : Installation Docker
    Docker Compose : Installation Docker Compose

Étapes d'exécution
1. Cloner ce projet

Clonez ce dépôt sur votre machine locale en utilisant la commande suivante :

git clone https://github.com/votre-utilisateur/mon-projet.git
cd mon-projet

2. Vérifier l'installation de Docker

Avant de commencer à utiliser Docker, assurez-vous qu'il est installé et fonctionne correctement sur votre machine. Vérifiez la version de Docker avec la commande suivante :

docker --version

3. Construction de l'image Docker pour l'application Flask

Une fois le projet cloné, vous devez construire l'image Docker de l'application Flask.

    Créer l'image Docker : Pour cela, vous devez avoir un fichier Dockerfile dans votre répertoire. Exécutez la commande suivante pour construire l'image :

docker build -t flask-app .

Tester l'image Docker : Après la construction de l'image, vous pouvez tester l'application Flask en exécutant un conteneur basé sur cette image. Utilisez la commande suivante pour lancer le conteneur :

sudo docker run -p 8000:8000 flask-app

Accéder à l'application : Ouvrez votre navigateur et allez à l'adresse suivante pour tester l'application :

    http://localhost:8000/

4. Utiliser Docker Compose pour gérer les services

    Créer un fichier docker-compose.yml : Ce fichier permet de configurer les services nécessaires à votre projet (comme l'application Flask et la base de données MySQL). Assurez-vous d'avoir un fichier docker-compose.yml dans votre répertoire.

    Lancer les services : Exécutez tous les services définis dans votre fichier docker-compose.yml avec la commande suivante :

docker-compose up

Vérifier l'application Flask et la base de données : Une fois les services lancés, l'application Flask devrait être accessible sur http://localhost:8000/, et elle doit être connectée à la base de données MySQL.

Vérifier les logs des conteneurs : Si vous rencontrez des problèmes, vous pouvez inspecter les logs des conteneurs pour déboguer. Utilisez les commandes suivantes pour voir les logs des conteneurs :

    docker logs mon-projet_flask-app_1
    docker logs mysql_db

5. Optimisation et nettoyage

    Optimisation de l'image Docker : Vous pouvez réduire la taille de votre image Docker en utilisant des images de base légères, comme alpine. Assurez-vous également de nettoyer les fichiers temporaires et de combiner les instructions dans le Dockerfile pour réduire les couches.

    Nettoyage de votre environnement Docker : Après avoir travaillé avec Docker, vous pouvez nettoyer les images et les conteneurs inutilisés avec les commandes suivantes :

    docker rm $(docker ps -a -q)
    docker rmi $(docker images -q)

6. Publier l'image sur Docker Hub

    Créer un compte Docker Hub : Si ce n'est pas déjà fait, créez un compte Docker Hub ici : Docker Hub.

    Taguer et pousser l'image : Une fois l'image construite, vous pouvez la pousser sur Docker Hub. Utilisez les commandes suivantes pour taguer et pousser l'image vers votre dépôt Docker Hub :

    docker tag flask-app votre-utilisateur/mon-projet_flask-app:latest
    docker push votre-utilisateur/mon-projet_flask-app

7. Variables d'environnement et personnalisation

Si vous devez ajouter des variables d'environnement à votre application Flask, vous pouvez les passer au moment de l'exécution avec la commande -e. Par exemple :

sudo docker run -e PORT=8000 -p 8000:8000 flask-app

Conclusion

Vous avez maintenant une application Flask qui fonctionne dans un conteneur Docker, avec une base de données MySQL, et vous avez appris à utiliser Docker Compose pour gérer plusieurs services. Vous pouvez également pousser votre image sur Docker Hub pour la partager avec d'autres.
