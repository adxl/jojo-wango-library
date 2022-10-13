1 - Avant de commencer une fonctionnalité:  
- `$ git checkout develop`
- `$ git fetch && git pull`

2 - Créer votre branche `$ git checkout -b <type>/<task>`
- type : feature, bugfix, doc, etc.
- task : tâche en cours ou numero du ticket  
Exemples : `feature/authentication`, `bugfix/form-error`, `feature/135`
<br>  

3 - Commit : `$ git commit -S -m '<type>:<subjet>`
- type : `[Feat|Fix|Refactor|Style|Build|Doc]`
- subjet : inférieur à 40 chars, lowercase
- Exemples :  
  - `Feat: implement login`
  - `Fix: request timeout`
<br>    

4 - Push la branche: `$ git push -u origin <branch>`  
**PS**: l'option `-u` seulement la première fois que la branch est pushed.  

5 - Une fois la fonctionnalité terminée:
- `$ git checkout develop`
- `$ git fetch && git pull`
- `$ git checkout <branch>` 
- `$ git rebase develop`  

Si besoin de fusionner ([Squash](https://www.internalpointers.com/post/squash-commits-into-one-git)) des commits: `$ git rebase -i HEAD~n`.   

6 - Push ou force push si squash : `git push [-f]`
     
7 - Créer une [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) `(feature -> develop)` 
