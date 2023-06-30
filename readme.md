## Explication 
lancer l'application avec run.py
Suivez les instructions pour saisir les mots, la date et les options pour la génération des mots de passe.

## Options de génération des mots de passe

Les options suivantes sont disponibles pour générer les mots de passe :

### Options pour les mots

- Basculer toutes les lettres en minuscule
- Basculer toutes les lettres en majuscule
- Basculer la première lettre en majuscule
- Retirer les accents
- Utiliser le L33T (substitutions de lettres par des caractères spéciaux)

### Options pour la date

- Utiliser les nombres de la date
- Utiliser l'année sur 2 chiffres
- Utiliser l'année sur 4 chiffres

### Options caractères spéciaux

- Ajouter les caractères spéciaux les plus communs
- Ajouter tous les caractères spéciaux

## Remarques

- Les mots de passe générés seront affichés dans la console.
- Assurez-vous de ne pas enregistrer ou partager les mots de passe générés sans précaution, car ils peuvent ne pas être sécurisés.

# POO

## Utilisation du polymorphisme [Guesser.py](/Guesser.py)
Dans le code, le polymorphisme est utilisé à travers l'interface commune fournie par la classe `OptionGenerator`. Cette classe agit comme une interface générique pour la génération d'options, tandis que les classes spécifiques telles que `LowercaseOptionGenerator`, `UppercaseOptionGenerator`, etc., fournissent des implémentations spécifiques de chaque option. Ainsi, la méthode generate_option de la classe OptionGenerator est appelée de manière polymorphe pour générer différentes options en fonction du type spécifié.

Le polymorphisme est le principe qui permet à des objets de classes différentes de répondre de manière différente à la même méthode ou propriété. Cela permet d'écrire un code plus générique et flexible, où des objets de types différents peuvent être traités de manière uniforme par le biais d'une interface commune.

## Utilisation de l'encapsulation [lien](/Guesser.py)
L'encapsulation est utilisée dans le code pour encapsuler les fonctionnalités de génération d'options dans des classes distinctes. Chaque classe d'option, telle que `LowercaseOptionGenerator`, `UppercaseOptionGenerator`, etc., encapsule sa propre logique de génération d'option. L'interface commune fournie par la classe OptionGenerator permet d'accéder de manière encapsulée aux différentes implémentations d'options.

L'encapsulation est le principe qui consiste à regrouper des données et les méthodes qui les manipulent au sein d'une même entité, appelée classe. Cela permet de cacher les détails d'implémentation et de fournir une interface claire pour interagir avec l'objet, en limitant l'accès aux données internes et en exposant uniquement les méthodes appropriées.

## Utilisation de la composition [lien](/Guesser.py)
La composition est utilisée dans le code à travers la classe `PasswordGenerator`, qui utilise la classe OptionGenerator pour générer les différentes options. La classe `PasswordGenerator` intègre la classe OptionGenerator en tant que composant interne, lui permettant ainsi d'utiliser ses fonctionnalités de génération d'options.

La composition est le principe qui permet de construire des objets complexes en combinant plusieurs objets plus simples. Cela permet de créer des relations entre des objets de manière flexible et modulaire, en favorisant la réutilisabilité et la gestion des dépendances.

## Utilisation de l'héritage [lien](/Guesser.py)
L'héritage est utilisé dans le code pour les classes `UppercaseOptionGenerator` et `FirstUppercaseOptionGenerator`. La classe `FirstUppercaseOptionGenerator` hérite de la classe `UppercaseOptionGenerator`, ce qui lui permet de réutiliser la méthode de génération d'option de la classe parente.

L'héritage est le principe qui permet à une classe de prendre les caractéristiques (méthodes et attributs) d'une autre classe, appelée classe parente ou classe de base. Cela favorise la réutilisabilité du code et permet de créer des hiérarchies de classes, où les classes dérivées héritent des fonctionnalités communes de la classe de base.

## Utilisation d'interface [lien](/Guesser.py)
Dans le code, l'utilisation d'interface est représentée par la classe `OptionGenerator`. Cette classe définit une interface commune pour la génération d'options, avec la méthode `generate_option`. Les classes spécifiques, telles que `LowercaseOptionGenerator`, `UppercaseOptionGenerator`, etc., implémentent cette interface en fournissant leur propre logique de génération d'option.

Une interface représente un contrat entre une classe et les autres parties du code. Elle définit les méthodes qu'une classe doit implémenter pour être considérée comme satisfaisant cette interface. L'utilisation d'interfaces permet de garantir un comportement cohérent et d'assurer l'interchangeabilité des objets qui implémentent cette interface.

## Utilisation de méthodes et attributs d'objets [lien](/Guesser.py)
Le code utilise des méthodes et attributs d'objets pour encapsuler la logique de génération d'options dans des classes spécifiques. Chaque classe d'option, telle que `LowercaseOptionGenerator`, `UppercaseOptionGenerator`, etc., définit des méthodes de génération spécifiques et les utilise pour générer les options correspondantes.

Les méthodes sont des fonctions associées à des objets ou des classes, qui permettent d'effectuer des opérations spécifiques sur ces objets ou de fournir des fonctionnalités particulières. Les attributs sont des variables associées à des objets ou des classes, qui contiennent des données spécifiques liées à ces objets.

## Utilisation de méthodes et attributs statiques [lien](/Guesser.py)
Le code utilise des méthodes et attributs statiques dans les classes de génération d'options, telles que `LowercaseOptionGenerator`, `UppercaseOptionGenerator`, etc. Ces méthodes et attributs sont définis avec le décorateur `@staticmethod` et sont liés à la classe plutôt qu'à une instance spécifique.

Les méthodes et attributs statiques sont des éléments de classe qui peuvent être utilisés sans nécessiter la création d'une instance de la classe. Ils sont partagés par toutes les instances de la classe et peuvent être appelés directement à partir de la classe elle-même.

## Utilisation de méthodes et attributs de classe [lien](/Guesser.py)
Le code utilise des méthodes et attributs de classe dans la classe `UserOptionGenerator`. Ces méthodes et attributs sont définis avec le décorateur @classmethod et sont liés à la classe elle-même plutôt qu'à une instance spécifique.

Les méthodes et attributs de classe sont des éléments qui agissent sur la classe elle-même plutôt que sur les instances individuelles de cette classe. Ils peuvent être utilisés pour effectuer des opérations spécifiques liées à la classe ou pour fournir des données partagées par toutes les instances de la classe.

